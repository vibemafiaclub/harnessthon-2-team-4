#!/usr/bin/env python3
"""test_check_contracts.py — 요구 계약 검사기 fixture 테스트.

PLAN-design-process-import.md §8이 나열한 실패 사례를 fixture로 고정한다.
검사기가 **무엇을 잡아야 하는지**가 아니라 **무엇을 통과시켜야 하는지**도 함께 고정한다 —
과잉 검사로 정상 계획 계약을 막으면 하네스가 첫 실행에서 진행 불가가 된다.

사용:  python scripts/harness/test_check_contracts.py
종료코드: 0 = 전부 통과, 1 = 실패 있음
"""
from __future__ import annotations
import copy, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_contracts import validate_contract, is_stub  # noqa: E402


def base() -> dict:
    """정상 계획 단계 계약 — node_id가 전부 null인 상태가 정상이다."""
    return {
        "schema_version": 2,
        "revision": "1.0",
        "requirements": [
            {"id": "REQ-01", "kind": "feature", "status": "confirmed",
             "text_verbatim": "요구 원문", "screens": ["SCR-01"], "states": []},
        ],
        "states": [],
        "personas": [{"id": "PER-01", "label": "역할 A"}],
        "adjacent_experiences": [
            {"id": "ADJ-01", "persona_refs": ["PER-01"], "kind": "before",
             "flow_link": "진입 시점에 불러오기 필요"},
        ],
        "core_experiences": [
            {"id": "CE-01", "priority": "primary", "status": "candidate",
             "statement": "유저는 목적을 달성하고 싶다",
             "success_condition_observable": "목록에 항목이 나타나면 성공",
             "persona_refs": ["PER-01"], "requirement_refs": ["REQ-01"],
             "source_kind": "사람-원문", "approval_ref": None, "screens": ["SCR-01", "SCR-02"]},
        ],
        "screens": [
            {"id": "SCR-01", "name": "S01", "ce_refs": ["CE-01"], "entry_from": [],
             "primary_cta_to": "SCR-02", "primary_persona_ref": "PER-01",
             "blocks": [{"id": "BLK-01", "priority": "P0", "node_id": None}], "node_id": None},
            {"id": "SCR-02", "name": "S02", "ce_refs": ["CE-01"], "entry_from": ["SCR-01"],
             "blocks": [{"id": "BLK-01", "priority": "P0", "node_id": None}], "node_id": None},
        ],
        "flow": {
            "edges": [
                {"id": "EDG-01", "from": "SCR-01", "to": "SCR-02", "cta": "다음", "kind": "forward"},
                {"id": "EDG-02", "from": "SCR-02", "to": "SCR-01", "cta": "뒤로", "kind": "back"},
            ],
            "paths": [
                {"id": "PTH-01", "ce_ref": "CE-01", "persona_ref": "PER-01",
                 "start_screen": "SCR-01", "end_screen": "SCR-02",
                 "edge_refs": ["EDG-01"], "recovery_edge_refs": ["EDG-02"],
                 "success_at": "SCR-02의 BLK-01"},
            ],
        },
        "edge_states_planned": [{"state": "empty", "screen": "SCR-01"}],
        "evidence": {"revision": None, "coverage_scope": "전수"},
    }


def built(c: dict) -> dict:
    """제작 완료 상태로 바꾼다 — node_id를 채우고 증거 revision을 맞춘다."""
    c["screens"][0]["node_id"] = "1:10"
    c["screens"][1]["node_id"] = "1:20"
    c["evidence"]["revision"] = c["revision"]
    return c


CASES: list[tuple[str, dict, list[str], list[str]]] = []


def case(name, mutate, expect_err=(), expect_warn=(), snapshot=None, comps=None):
    CASES.append((name, mutate, list(expect_err), list(expect_warn), snapshot, comps))


def _m(fn):
    def go():
        c = base()
        fn(c)
        return c
    return go


# ── 통과해야 하는 것 ──────────────────────────────────────────────
case("정상 계획 계약 — node_id null은 정상", _m(lambda c: None),
     expect_err=[], expect_warn=["C-REV"])
case("v1 계약 — 구조 검사 대상 아님, 소급 적용 금지",
     _m(lambda c: c.update(schema_version=1)),
     expect_err=[], expect_warn=["C-SCHEMA"])
case("제작 완료 + 스냅샷 일치 — 통과",
     lambda: built(base()), expect_err=[], snapshot={"1:10", "1:20"})

# ── 잡아야 하는 것 ────────────────────────────────────────────────
case("ID 중복", _m(lambda c: c["screens"].append(dict(c["screens"][0]))),
     expect_err=["C-DUP"])
case("없는 화면 참조", _m(lambda c: c["core_experiences"][0]["screens"].append("SCR-99")),
     expect_err=["C-REF", "C-BIDIR"])
case("없는 컴포넌트 참조",
     _m(lambda c: c["screens"][0].update(required_component_refs=["CMP-99"])),
     expect_err=["C-REF"], comps={"CMP-01"})
case("단방향 매핑만 존재 — CE는 가리키는데 화면은 모름",
     _m(lambda c: c["screens"][1].update(ce_refs=[])),
     expect_err=["C-BIDIR"])
case("어떤 CE에도 연결되지 않은 화면",
     _m(lambda c: (c["screens"].append({"id": "SCR-03", "name": "S03", "ce_refs": [], "blocks": []}))),
     expect_err=["C-BIDIR"])
case("CTA 목적지 부재", _m(lambda c: c["flow"]["edges"][0].update(to=None)),
     expect_err=["C-CTA"])
case("confirmed인데 자리표시자",
     _m(lambda c: c["core_experiences"][0].update(
         status="confirmed", approval_ref="LOCK-I", statement="<유저는 ___하고 싶다>")),
     expect_err=["C-PLACEHOLDER"])
case("CE 이중 관리", _m(lambda c: c["requirements"][0].update(kind="core_experience")),
     expect_err=["C-CE-DUAL"])
case("primary인데 근거가 사람-해석",
     _m(lambda c: c["core_experiences"][0].update(source_kind="사람-해석")),
     expect_err=["C-PRIMARY-SRC"])
case("confirmed인데 승격 기록 없음",
     _m(lambda c: c["core_experiences"][0].update(status="confirmed", approval_ref=None)),
     expect_err=["C-APPROVAL"])
case("node_id는 있는데 스냅샷에 없음",
     lambda: built(base()), expect_err=["C-SNAPSHOT"], snapshot={"9:99"})
case("다른 revision의 증거",
     lambda: (lambda c: (built(c), c["evidence"].update(revision="1.1"), c)[-1])(base()),
     expect_err=["C-REV"], snapshot={"1:10", "1:20"})
case("복구 경로 없음 — CE6 근거 부재",
     _m(lambda c: c["flow"]["paths"][0].update(recovery_edge_refs=[])),
     expect_err=[], expect_warn=["C-RECOVERY"])
case("없는 edge 참조",
     _m(lambda c: c["flow"]["paths"][0]["edge_refs"].append("EDG-99")),
     expect_err=["C-REF"])


def codes(msgs):
    return {m.split()[0] for m in msgs}


def main() -> int:
    failed = 0
    for name, make, exp_e, exp_w, snap, comps in CASES:
        c = make()
        err, warn = validate_contract(c, comps, snap)
        ec, wc = codes(err), codes(warn)
        problems = []
        for code in exp_e:
            if code not in ec:
                problems.append(f"기대한 에러 {code} 미발생")
        for code in exp_w:
            if code not in wc:
                problems.append(f"기대한 경고 {code} 미발생")
        if not exp_e and err:
            problems.append(f"발생하면 안 되는 에러: {sorted(ec)}")
        if problems:
            failed += 1
            print(f"FAIL  {name}")
            for p in problems:
                print(f"        {p}")
            for m in err:
                print(f"        err: {m}")
        else:
            print(f"ok    {name}")

    # is_stub — 제목만 있는 산출물은 빈 파일과 같다
    stub_cases = [
        ("제목만", "# 제목\n\n## 절\n\n", True),
        ("주석·인용만", "# 제목\n<!-- TODO -->\n> 안내\n", True),
        ("표 구분선만", "# 제목\n| --- | --- |\n", True),
        ("실질 내용 있음", "# 제목\n\n값: 3\n", False),
    ]
    for name, text, expect in stub_cases:
        got = is_stub(text)
        if got != expect:
            failed += 1
            print(f"FAIL  is_stub({name}) — 기대 {expect}, 실제 {got}")
        else:
            print(f"ok    is_stub({name})")

    total = len(CASES) + len(stub_cases)
    print(f"\n{total - failed}/{total} 통과")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
