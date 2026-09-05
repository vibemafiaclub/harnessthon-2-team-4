#!/usr/bin/env python3
"""check_contracts.py — 디자인 하네스 계약 검사기 (PLAN P0 초판).

검사 항목
  1. project.json 경로 실재 + PRD가 비어 있지 않은가
  2. target 단일 원장: brief.md / _system/brief.md / 과제 전용 스킬 안의 Figma file key가 서로 어긋나지 않는가
     (전용 스킬에 file key 상수가 있으면 경고 — 원장 참조로 바꿔야 한다)
  3. brief.md A단계 기준값 YAML에 TODO가 남은 항목 목록 (SKIP으로 처리될 항목을 사람에게 보여 준다)
  4. 도메인 누출: 코어(SKILL.md, templates/)에 프로젝트 domain_terms가 들어갔는가
  5. 다른 프로젝트 용어 유입: project.json의 forbidden_inherited_terms_from 프로젝트 용어가 이 프로젝트 문서에 있는가
  6. decisions.md의 GATE 블록 필수 키 + 제작/검증 producer 동일 여부

사용:  python scripts/harness/check_contracts.py [project-id ...]   (인자 없으면 docs/projects/* 전부)
종료코드: 0 = 위반 없음, 1 = 위반 있음(경고만이면 0)
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE_FILES = [ROOT / ".claude/skills/oss-design-harness/SKILL.md", *sorted((ROOT / "templates").rglob("*"))]
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
    for g in gates:
        kv = dict(re.findall(r"^(\w+):\s*(.*)$", g, re.M))
        missing = [k for k in GATE_REQUIRED if k not in kv]
        if missing:
            errors.append(f"{tag} GATE '{kv.get('stage','?')}' 필수 키 누락: {missing}")
        if kv.get("status") == "PASS" and kv.get("output_refs", "[]").strip() in ("[]", ""):
            errors.append(f"{tag} GATE '{kv.get('stage')}' status=PASS인데 output_refs가 비어 있다")
        st = kv.get("stage", "")
        if st.startswith("build"):
            producers.setdefault("build", kv.get("producer", ""))
        if st.startswith("verify") and producers.get("build") and kv.get("producer") == producers["build"]:
            errors.append(f"{tag} GATE '{st}' producer가 제작 producer와 같다 — 검증 입력 거부")
    if decisions and not gates:
        warnings.append(f"{tag} decisions.md에 GATE 블록 없음 (템플릿 상태이거나 구버전)")


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
