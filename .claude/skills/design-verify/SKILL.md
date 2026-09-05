---
name: design-verify
description: 이미 만들어진 Figma 화면을 A단계(구조적 사실 — 기능 커버리지·추적성·하한선·토큰·FP·IC)와 C단계(미적·게슈탈트 — 반드시 스크린샷, Critic/Advocate/PM), V단계(최종 실재)로 검증하고 실패를 반복실패/결정충돌/방향오류/국소결함으로 진단한다. "검증해줘", "이 화면 어때", "디자인 검수", 화면 수정 후 재검 요청 시 사용. oss-design-harness와 같은 references/를 읽는 얇은 진입점이다.
---

# design-verify — A/C/V 검증 진입점

**정본은 `../oss-design-harness/references/`다.** 이 파일은 순서와 입력만 정한다. 판정 방법·항목·라우팅을 여기에 다시 쓰지 않는다(두 곳에 쓰면 어긋난다 — feat/yj1 원칙).

## 시작 전 확인
1. `docs/projects/<id>/project.json` → `brief_path`·`decisions_path`. `python scripts/harness/check_contracts.py <id>` ERROR 0.
2. `brief.md` A단계 기준값 YAML이 있는가. 없으면 검증을 시작하지 않고 먼저 만들라고 알린다 — 기준 없는 통과/실패는 그때그때 다른 답이 된다.
3. `decisions.md` 검증 로그를 **먼저 읽는다** — 같은 화면을 몇 번 시도했고 무엇이 실패했는지. 라운드 상한(3)·하위 상한(3) 확인.
4. 제작 세션과 다른 **신규 컨텍스트 Agent**로 검증한다(`references/verify-routing.md` 배선 ①~⑥). 격리 강제 수준을 보고 머리에 적는다.

## 순서
1. **A-F 기능 커버리지 → A-T 추적성** (`stage-a-structural.md`) — 없는 화면·끊긴 흐름·연결 0개를 먼저 잡는다. FAIL이면 나머지 전에 보고.
2. **A-0 고정 하한선 → A-1~A-9** — 사실 파일(`.cache/nodes-after.json`) 1회 계산. 위반이 파일 전반에 일관되면 기준 오류 판정 절차.
3. **C-1~C-7, C-X, C-S** (`stage-c-aesthetic.md`) — `get_screenshot` 렌더 필수. Critic·Advocate 각각 신규 컨텍스트, PM 판결은 사람/master.
4. **V** (`stage-v-flow.md`) — 최신 revision 재확인.
5. 3축 결합 판정(`design-principle.md`): ③ `검증 불가`는 FAIL.
6. 실패 라우팅 (`verify-routing.md`): 반복실패 > 결정충돌(UNLOCK 요청) > 방향오류 > 국소결함.

## 기록
- 판정 원문을 `decisions.md` 검증 로그에 **요약 없이** append. 화면별 C 시도 횟수 표·기준 정정 기록 표 갱신.
- GATE `stage: verify-A|verify-C|verify-V` 블록 append (`templates/contracts/gate.yaml`). 검증 Agent가 한도(429)로 죽으면 `BLOCKED`.
- 최종 "됐다"는 사람이 낸다.
