#!/usr/bin/env python3
"""check_contracts.py — 디자인 하네스 계약 검사기.

검사 항목
  1. project.json 경로 실재 + PRD가 비어 있지 않은가
  2. target 단일 원장: brief.md / _system/brief.md / 과제 전용 스킬 안의 Figma file key가 서로 어긋나지 않는가
     (전용 스킬에 file key 상수가 있으면 경고 — 원장 참조로 바꿔야 한다)
  3. brief.md A단계 기준값 YAML에 TODO가 남은 항목 목록 (SKIP으로 처리될 항목을 사람에게 보여 준다)
  4. 도메인 누출: 코어(SKILL.md, templates/)에 프로젝트 domain_terms가 들어갔는가
  5. 다른 프로젝트 용어 유입: project.json의 forbidden_inherited_terms_from 프로젝트 용어가 이 프로젝트 문서에 있는가
  6. decisions.md의 GATE 블록 필수 키 + 제작/검증 producer 동일 여부
  7. 요구 계약 v2 정합 (PLAN-design-process-import.md §5·§7): ID 중복, dangling ref,
     CE↔화면 양방향 누락, CTA 목적지 부재, 미해결 자리표시자, CE 이중 관리,
     primary CE의 근거 소스, 승격 기록, 증거 revision·스냅샷 대조
  8. 산출물 실질 내용: 제목만 있는 brief/decisions는 빈 파일과 같다
  9. 검증 GATE 소급 PASS: primary CE가 미확정인데 verify-C/V가 PASS인가

이 검사기는 **자동 승인자가 아니다.** 자료 준비 여부와 기계적 정합만 검사하고
사람의 선택·기준 승격을 대신하지 않는다 (PLAN §6).

사용:  python scripts/harness/check_contracts.py [project-id ...]   (인자 없으면 docs/projects/* 전부)
종료코드: 0 = 위반 없음, 1 = 위반 있음(경고만이면 0)
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE_FILES = [ROOT / ".claude/skills/oss-design-harness/SKILL.md", ROOT / ".claude/skills/design-verify/SKILL.md", *sorted((ROOT / ".claude/skills/oss-design-harness/references").rglob("*.md")), *sorted((ROOT / "templates").rglob("*"))]
FILE_KEY_RE = re.compile(r"figma\.com/design/([0-9A-Za-z]{22,128})|file_key:\s*([0-9A-Za-z]{22,128})|fileKey\s*`?([0-9A-Za-z]{22,128})")
GATE_REQUIRED = ["stage", "mode", "project_id", "run_id", "revision", "producer", "target_ref", "output_refs", "status", "next_stage"]

errors: list[str] = []
warnings: list[str] = []


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def file_keys(text: str) -> set[str]:
    return {k for m in FILE_KEY_RE.finditer(text) for k in m.groups() if k}


PLACEHOLDER_RE = re.compile(r"<[^>\n]{2,}>|\bTODO\b|\bTBD\b")


def is_stub(text: str) -> bool:
    """제목·주석·빈 줄만 있으면 빈 파일과 같다. 최소 한 줄의 실질 내용이 있어야 한다."""
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("<!--") or s.startswith(">"):
            continue
        if set(s) <= set("-|= *_`"):  # 표 구분선·수평선
            continue
        return False
    return True


def _ids(rows, key="id"):
    return [r.get(key) for r in rows if isinstance(r, dict) and r.get(key)]


def _dups(seq):
    seen, dup = set(), []
    for x in seq:
        if x in seen and x not in dup:
            dup.append(x)
        seen.add(x)
    return dup


def validate_contract(c: dict, component_ids: set[str] | None = None,
                      snapshot_nodes: set[str] | None = None) -> tuple[list[str], list[str]]:
    """요구 계약 하나를 검사한다. (errors, warnings) — 태그 없는 순수 메시지.

    각 메시지는 안정적인 코드로 시작한다(C-SCHEMA / C-DUP / C-REF / C-BIDIR /
    C-CTA / C-PLACEHOLDER / C-CE-DUAL / C-PRIMARY-SRC / C-APPROVAL / C-REV /
    C-SNAPSHOT / C-RECOVERY). fixture 테스트가 이 코드로 단언한다.
    """
    err: list[str] = []
    warn: list[str] = []

    ver = c.get("schema_version")
    if ver == 1:
        warn.append("C-SCHEMA schema_version=1 — v2 필드가 미작성이다. 마이그레이션 시 기존 ID·target·LOCK·승격 원문을 보존하고 새 필드만 초안으로 추가한다")
        return err, warn  # v1은 구조 검사 대상이 아니다. 소급 적용하지 않는다.
    if ver != 2:
        err.append(f"C-SCHEMA schema_version이 2가 아니다: {ver!r}")

    reqs = c.get("requirements") or []
    ces = c.get("core_experiences") or []
    scrs = c.get("screens") or []
    pers = c.get("personas") or []
    adjs = c.get("adjacent_experiences") or []
    sts = c.get("states") or []
    flow = c.get("flow") or {}
    edges = flow.get("edges") or []
    paths = flow.get("paths") or []

    req_ids, ce_ids, scr_ids = set(_ids(reqs)), set(_ids(ces)), set(_ids(scrs))
    per_ids, st_ids, edg_ids = set(_ids(pers)), set(_ids(sts)), set(_ids(edges))

    # B. ID 중복
    for label, rows in (("requirements", reqs), ("core_experiences", ces), ("screens", scrs),
                        ("personas", pers), ("states", sts), ("adjacent_experiences", adjs),
                        ("flow.edges", edges), ("flow.paths", paths)):
        d = _dups(_ids(rows))
        if d:
            err.append(f"C-DUP {label}에 중복 ID: {d}")
    for s in scrs:
        d = _dups(_ids(s.get("blocks") or []))
        if d:
            err.append(f"C-DUP screens[{s.get('id')}].blocks에 중복 ID: {d}")

    # C. dangling ref
    def ref(where, values, pool, poolname):
        for v in (values or []):
            if v and v not in pool:
                err.append(f"C-REF {where} → 없는 {poolname}: {v!r}")

    for ce in ces:
        i = ce.get("id")
        ref(f"core_experiences[{i}].persona_refs", ce.get("persona_refs"), per_ids, "persona")
        ref(f"core_experiences[{i}].requirement_refs", ce.get("requirement_refs"), req_ids, "requirement")
        ref(f"core_experiences[{i}].screens", ce.get("screens"), scr_ids, "screen")
    for s in scrs:
        i = s.get("id")
        ref(f"screens[{i}].ce_refs", s.get("ce_refs"), ce_ids, "core_experience")
        ref(f"screens[{i}].entry_from", s.get("entry_from"), scr_ids, "screen")
        if s.get("primary_persona_ref"):
            ref(f"screens[{i}].primary_persona_ref", [s["primary_persona_ref"]], per_ids, "persona")
        if s.get("primary_cta_to"):
            ref(f"screens[{i}].primary_cta_to", [s["primary_cta_to"]], scr_ids, "screen")
        if component_ids is not None:
            ref(f"screens[{i}].required_component_refs", s.get("required_component_refs"), component_ids, "component")
    for r in reqs:
        ref(f"requirements[{r.get('id')}].screens", r.get("screens"), scr_ids, "screen")
        ref(f"requirements[{r.get('id')}].states", r.get("states"), st_ids, "state")
    for a in adjs:
        ref(f"adjacent_experiences[{a.get('id')}].persona_refs", a.get("persona_refs"), per_ids, "persona")
    for t in (c.get("tricky_cases") or []):
        ref(f"tricky_cases[{t.get('id')}].must_appear_in", t.get("must_appear_in"), scr_ids, "screen")
    for e in edges:
        ref(f"flow.edges[{e.get('id')}].from", [e.get("from")], scr_ids, "screen")
    for p in paths:
        i = p.get("id")
        if p.get("ce_ref"):
            ref(f"flow.paths[{i}].ce_ref", [p["ce_ref"]], ce_ids, "core_experience")
        if p.get("persona_ref"):
            ref(f"flow.paths[{i}].persona_ref", [p["persona_ref"]], per_ids, "persona")
        ref(f"flow.paths[{i}].edge_refs", p.get("edge_refs"), edg_ids, "edge")
        ref(f"flow.paths[{i}].recovery_edge_refs", p.get("recovery_edge_refs"), edg_ids, "edge")
        for k in ("start_screen", "end_screen"):
            if p.get(k):
                ref(f"flow.paths[{i}].{k}", [p[k]], scr_ids, "screen")
        if not (p.get("recovery_edge_refs") or []):
            warn.append(f"C-RECOVERY flow.paths[{i}]에 복구 경로(recovery_edge_refs)가 없다 — CE6(이탈 경로) 근거 부재")
    for esp in (c.get("edge_states_planned") or []):
        if esp.get("screen"):
            ref("edge_states_planned[].screen", [esp["screen"]], scr_ids, "screen")
    for rep in ((c.get("setup_points") or {}).get("role_entry_points") or []):
        if rep.get("persona_ref"):
            ref("setup_points.role_entry_points[].persona_ref", [rep["persona_ref"]], per_ids, "persona")

    # D. 역방향 누락 — 단방향 매핑만 존재하면 A-T CE1~CE3가 자기 자신과 비교하게 된다
    fwd = {(ce.get("id"), s) for ce in ces for s in (ce.get("screens") or [])}
    bwd = {(ce, s.get("id")) for s in scrs for ce in (s.get("ce_refs") or [])}
    for ce_id, scr_id in sorted(fwd - bwd):
        err.append(f"C-BIDIR core_experiences[{ce_id}].screens는 {scr_id}를 가리키는데 screens[{scr_id}].ce_refs에 {ce_id}가 없다")
    for ce_id, scr_id in sorted(bwd - fwd):
        err.append(f"C-BIDIR screens[{scr_id}].ce_refs는 {ce_id}를 가리키는데 core_experiences[{ce_id}].screens에 {scr_id}가 없다")
    for s in scrs:
        if not (s.get("ce_refs") or []):
            err.append(f"C-BIDIR screens[{s.get('id')}]가 어떤 CE에도 연결되지 않았다 — 근거 없는 화면(A-T CE3)")

    # E. CTA 목적지 부재
    for e in edges:
        if not e.get("to"):
            err.append(f"C-CTA flow.edges[{e.get('id')}] CTA {e.get('cta')!r}의 목적지(to)가 없다")

    # F. 미해결 자리표시자 — confirmed 항목에만 적용(초안은 자리표시자가 정상)
    for label, rows, fields in (
        ("core_experiences", ces, ("statement", "success_condition_observable")),
        ("requirements", reqs, ("text_verbatim",)),
    ):
        for r in rows:
            if r.get("status") != "confirmed":
                continue
            for f in fields:
                v = r.get(f)
                if isinstance(v, str) and PLACEHOLDER_RE.search(v):
                    err.append(f"C-PLACEHOLDER {label}[{r.get('id')}].{f}가 confirmed인데 자리표시자다: {v!r}")

    # G/H. CE 관리 규칙
    for r in reqs:
        if r.get("kind") == "core_experience":
            err.append(f"C-CE-DUAL requirements[{r.get('id')}].kind=core_experience — CE 본문 이중 관리 금지. 정본은 core_experiences[]이고 여기서는 requirement_refs로 참조한다")
    for ce in ces:
        i = ce.get("id")
        if ce.get("priority") == "primary" and ce.get("source_kind") == "사람-해석":
            err.append(f"C-PRIMARY-SRC core_experiences[{i}]가 primary인데 source_kind=사람-해석 — primary는 사람-원문 또는 실측 근거가 필요하다")
        if ce.get("status") == "confirmed" and not ce.get("approval_ref"):
            err.append(f"C-APPROVAL core_experiences[{i}]가 confirmed인데 approval_ref가 없다 — 승격 기록 없이 확정으로 올리지 않는다(LOCK-I)")

    # I/J. 증거 묶음
    ev = c.get("evidence") or {}
    planned = [s for s in scrs if not s.get("node_id")]
    built = [s for s in scrs if s.get("node_id")]
    if built:
        if ev.get("revision") and c.get("revision") and ev["revision"] != c["revision"]:
            err.append(f"C-REV evidence.revision({ev['revision']})가 계약 revision({c['revision']})과 다르다 — 다른 revision의 증거로 판정하지 않는다")
        if snapshot_nodes is not None:
            for s in built:
                if s["node_id"] not in snapshot_nodes:
                    err.append(f"C-SNAPSHOT screens[{s.get('id')}].node_id={s['node_id']}가 스냅샷에 없다 — 기록만 있고 실물이 없다")
        if ev.get("coverage_scope") in (None, "", "집계만"):
            warn.append("C-SNAPSHOT evidence.coverage_scope가 전수 증거가 아니다 — 제작자 자체 집계를 독립 실물 검증으로 승격하지 않는다")
    elif planned:
        warn.append(f"C-REV 계획 단계 계약이다(node_id 미기입 {len(planned)}개) — 문서 단계는 통과하지만 제작 증거 게이트는 통과하지 않는다")

    return err, warn


def _ref_exists(ref_path: str, pj: dict) -> bool:
    """output_refs 한 항목이 실재하는가.

    `renders/r1.1-S01..S11.png` 같은 **범위 표기**와 `*` 글롭을 경로로 오해하지 않는다.
    범위·글롭은 하나라도 매칭되면 통과 — 개수까지 세지는 않는다(사람이 쓰는 축약 표기다).
    """
    bases = [ROOT, ROOT / (pj.get("artifact_root") or "")]
    if ".." in ref_path or "*" in ref_path:
        stem = re.split(r"\.\.|\*", ref_path)[0]
        parent, _, prefix = stem.rpartition("/")
        for b in bases:
            d = b / parent if parent else b
            if d.is_dir() and any(f.name.startswith(prefix) for f in d.iterdir()):
                return True
        return False
    return any((b / ref_path).exists() for b in bases)


def check_contract(tag: str, pj: dict) -> dict:
    """프로젝트의 요구 계약을 읽어 검사하고, GATE 교차검사용으로 계약 dict를 돌려준다."""
    root = pj.get("artifact_root")
    if not root:
        return {}
    cpath = ROOT / root / "contracts/requirements.json"
    if not cpath.exists():
        warnings.append(f"{tag} 요구 계약 없음: {cpath.relative_to(ROOT)} (plan-only 초기면 정상)")
        return {}
    try:
        c = json.loads(cpath.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errors.append(f"{tag} 요구 계약 JSON 파싱 실패: {e}")
        return {}

    comp_ids = None
    comp_path = ROOT / root / "contracts/components.json"
    if comp_path.exists():
        try:
            comp = json.loads(comp_path.read_text(encoding="utf-8"))
            rows = comp.get("components") if isinstance(comp, dict) else comp
            comp_ids = set(_ids(rows or []))
        except json.JSONDecodeError:
            warnings.append(f"{tag} components.json 파싱 실패 — 컴포넌트 참조 검사 생략")

    snap_nodes = None
    snap_rel = (c.get("evidence") or {}).get("snapshot_ref")
    if snap_rel and not PLACEHOLDER_RE.search(str(snap_rel)):
        spath = ROOT / root / snap_rel if not Path(snap_rel).is_absolute() else Path(snap_rel)
        if spath.exists():
            try:
                snap = json.loads(spath.read_text(encoding="utf-8"))
                snap_nodes = set(re.findall(r"\b\d+:\d+\b", json.dumps(snap, ensure_ascii=False)))
            except json.JSONDecodeError:
                warnings.append(f"{tag} 스냅샷 파싱 실패 — node_id 실재 검사 생략")
        else:
            warnings.append(f"{tag} evidence.snapshot_ref가 가리키는 파일이 없다: {snap_rel}")

    e, w = validate_contract(c, comp_ids, snap_nodes)
    errors.extend(f"{tag} {m}" for m in e)
    warnings.extend(f"{tag} {m}" for m in w)
    return c


def check_project(pj_path: Path) -> None:
    pj = json.loads(pj_path.read_text(encoding="utf-8"))
    pid = pj["project_id"]
    tag = f"[{pid}]"

    # 1. 경로 실재 + PRD 비어 있지 않음
    for key in ("prd_path", "brief_path", "decisions_path", "system_brief_path"):
        rel = pj.get(key)
        if not rel:
            continue
        p = ROOT / rel
        if not p.exists():
            (warnings if key != "prd_path" else errors).append(f"{tag} {key} 없음: {rel}")
        elif key == "prd_path" and p.stat().st_size < 200:
            errors.append(f"{tag} PRD가 비어 있거나 너무 짧다({p.stat().st_size}B): {rel} — 이름만 보고 정상 입력으로 처리하지 않는다")

    brief = read(ROOT / pj["brief_path"]) if pj.get("brief_path") else ""
    system = read(ROOT / pj["system_brief_path"]) if pj.get("system_brief_path") else ""
    skill = read(ROOT / pj["task_skill"]) if pj.get("task_skill") else ""

    # 2. target 단일 원장
    def target_block(text: str) -> str:
        m = re.search(r"target:\s*\n((?:[ \t]+.*\n?)+)", text)
        return m.group(1) if m else ""

    brief_keys = file_keys(target_block(brief))
    system_keys = file_keys(target_block(system))
    skill_keys = file_keys(skill)
    if brief and not brief_keys:
        warnings.append(f"{tag} brief.md target에 file key 없음 (plan-only면 정상)")
    if brief_keys and system_keys and not (brief_keys & system_keys):
        errors.append(f"{tag} target 불일치: brief={sorted(brief_keys)} vs _system={sorted(system_keys)} — 쓰기 차단")
    if skill_keys:
        errors.append(f"{tag} 전용 스킬에 file key 상수 {sorted(skill_keys)} — 원장(brief.md target) 참조로 바꿔라")
    if len(brief_keys) > 1:
        warnings.append(f"{tag} brief.md target에 file key가 2개 이상({sorted(brief_keys)}) — backup 표기인지 확인, 제출본 결정 필요")

    # 3. A단계 기준값 TODO
    m = re.search(r"## A단계 기준값.*?```yaml\n(.*?)```", brief, re.S)
    if m:
        todo_lines = [ln.strip() for ln in m.group(1).splitlines() if re.search(r"\bTODO\b|\bTBD\b", ln)]
        if todo_lines:
            warnings.append(f"{tag} A단계 기준값 미기입 → SKIP 예정: " + " | ".join(todo_lines))
        if "component_reuse_min" in m.group(1) and "component_reuse_formula" not in m.group(1):
            warnings.append(f"{tag} component_reuse_min은 있는데 산식(component_reuse_formula)이 없다 — 어느 산식의 하한인지 확정 필요")

    # 4. 도메인 누출 → 코어
    terms = pj.get("domain_terms", [])
    for cf in CORE_FILES:
        if not cf.is_file():
            continue
        text = read(cf)
        hits = [t for t in terms if t in text]
        if hits:
            errors.append(f"{tag} 코어 파일 {cf.relative_to(ROOT)} 에 도메인 용어 유입: {hits}")

    # 5. 다른 프로젝트 용어 유입
    src = pj.get("forbidden_inherited_terms_from")
    if src:
        src_pj_path = ROOT / "docs/projects" / src / "project.json"
        if src_pj_path.exists():
            src_terms = json.loads(src_pj_path.read_text(encoding="utf-8")).get("domain_terms", [])
            for rel in (pj.get("prd_path"), pj.get("domain_doc_path"), pj.get("brief_path"), pj.get("system_brief_path")):
                if not rel or not (ROOT / rel).exists():
                    continue
                text = read(ROOT / rel)
                hits = [t for t in src_terms if t in text]
                if hits:
                    errors.append(f"{tag} {rel} 에 {src} 용어 유입: {hits}")

    # 6. GATE 블록
    decisions = read(ROOT / pj["decisions_path"]) if pj.get("decisions_path") else ""
    gates = re.findall(r"```yaml\n(stage:.*?)```", decisions, re.S)
    producers: dict[str, str] = {}
    verify_pass_stages: list[str] = []
    for g in gates:
        kv = dict(re.findall(r"^(\w+):\s*(.*)$", g, re.M))
        missing = [k for k in GATE_REQUIRED if k not in kv]
        if missing:
            errors.append(f"{tag} GATE '{kv.get('stage','?')}' 필수 키 누락: {missing}")
        if kv.get("status") == "PASS" and kv.get("output_refs", "[]").strip() in ("[]", ""):
            errors.append(f"{tag} GATE '{kv.get('stage')}' status=PASS인데 output_refs가 비어 있다")
        for ref_path in re.findall(r"[\w./*-]+\.(?:md|json|png)", kv.get("output_refs", "")):
            if _ref_exists(ref_path, pj):
                continue
            errors.append(f"{tag} GATE '{kv.get('stage')}' output_refs가 없는 경로를 가리킨다: {ref_path}")
        st = kv.get("stage", "")
        if st.startswith("build"):
            producers.setdefault("build", kv.get("producer", ""))
        if st.startswith("verify"):
            if producers.get("build") and kv.get("producer") == producers["build"]:
                errors.append(f"{tag} GATE '{st}' producer가 제작 producer와 같다 — 검증 입력 거부")
            if kv.get("status") == "PASS":
                verify_pass_stages.append(st)
    if decisions and not gates:
        warnings.append(f"{tag} decisions.md에 GATE 블록 없음 (템플릿 상태이거나 구버전)")

    # 7. 요구 계약 v2 정합
    contract = check_contract(tag, pj)

    # 8. 산출물 실질 내용 — 제목만 있는 파일은 빈 파일과 같다
    for key, text in (("brief_path", brief), ("decisions_path", decisions)):
        rel = pj.get(key)
        if rel and (ROOT / rel).exists() and is_stub(text):
            errors.append(f"{tag} {key}({rel})에 제목·주석 말고 실질 내용이 없다 — 진행 차단")

    # 9. 검증 GATE 소급 PASS — primary CE가 미확정인데 C/V가 PASS일 수 없다
    if contract and verify_pass_stages:
        unconfirmed = [ce.get("id") for ce in (contract.get("core_experiences") or [])
                       if ce.get("priority") == "primary" and ce.get("status") != "confirmed"]
        late = [s for s in verify_pass_stages if s in ("verify-C", "verify-V")]
        if unconfirmed and late:
            errors.append(f"{tag} GATE {late}가 PASS인데 primary CE {unconfirmed}가 미확정이다 — 축 ③이 검증 불가인 채로 최종 승인으로 진행하지 않는다")


def main(argv: list[str]) -> int:
    ids = argv or [p.parent.name for p in (ROOT / "docs/projects").glob("*/project.json")]
    for pid in ids:
        pj_path = ROOT / "docs/projects" / pid / "project.json"
        if not pj_path.exists():
            errors.append(f"[{pid}] project.json 없음: {pj_path.relative_to(ROOT)}")
            continue
        check_project(pj_path)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
