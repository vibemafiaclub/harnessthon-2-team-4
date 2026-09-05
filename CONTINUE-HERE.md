# CONTINUE-HERE — 다음 세션이 여기서 이어받는다

작성 2026-09-05 · 브랜치 `dev`(원격 최신 `4440761`) · 백업 `feat/helee`(합병 전 dev) · 원격 push 권한 있음(`HanEol-Lee77`)

## 1. 지금 상태 한눈에

| 것 | 상태 | 위치 |
|---|---|---|
| 코어 하네스 | dev + feat/yj1 + iceberg **합병 완료**. SKILL.md는 라우터(156줄), 방법론은 `references/` 13파일 | `.claude/skills/oss-design-harness/`, `.claude/skills/design-verify/` |
| 검사기 | ERROR 0 (경고 4: family-trip 원장 미생성 3, 청첩장 target 파일 3개) | `python scripts/harness/check_contracts.py` |
| 청첩장 프로젝트 | 4막 중 **I 완료(LOCK-I)**, M·W LOCK 없음, U 11화면 존재 | `design/invitation-scheduler/` |
| 청첩장 U 검증 1.3 | **A 불통과 · C 불통과**(PM 초안, 사람 판결 대기) | `decisions.md` 검증 로그 1.3 행 + GATE verify-A/C |
| 가족 여행 프로젝트 | 설정·도메인 메모·fixture PRD만(plan-only). 다른 세션의 레퍼런스 조사 있음 | `docs/projects/family-trip/`, `design/research/family-travel/` |
| 사주 | 보류 | `docs/backlog/saju/` |
| 스크래치 워크트리 | yj1·iceberg 체크아웃(참조용, 삭제 가능) | `git worktree list` |

## 2. 읽는 순서 (10분)

1. `CLAUDE.md` — 불변 규칙 11개
2. `.claude/skills/oss-design-harness/SKILL.md` — 라우터·모드·게이트·라우팅 표
3. `design/invitation-scheduler/onboarding.md` → `brief.md`(원장·A 기준값 YAML) → `decisions.md`(1.3 행·GATE) → `interview.md`
4. `docs/harness-lessons.md` L1~L40 — 왜 이런 규칙이 생겼나
5. `docs/PLAN-merge-feat-yj1.md` — 합병에서 무엇을 채택·버렸나

## 3. 사람 결정 — 2026-09-05 오후 결과 (D1만 남음)

| # | 결정 | 결과 | 반영 위치 |
|---|---|---|---|
| D1 | C-5 맥락 적합 판결 | **미결 — 사용자가 병렬 세션에서 처리 중** | decisions GATE verify-C blockers |
| D2 | grid 4 vs 캘린더 점 2px | 점·아이콘 내부 간격 2px 예외 허용 | brief `layout.grid_exceptions` |
| D3 | 가운뎃점·날짜 슬래시 | 날짜 슬래시 허용, 가운뎃점·분수·대시·기호 아이콘은 말로 풀기 | brief `copy.*` |
| D4 | text/tertiary 대비 | 토큰 값 유지. 12~14px 라벨은 secondary, tertiary는 큰 글자에만 | brief `text_color_usage` |
| D5 | A-4 산식·하한 | REUSE-B(반복 패턴 중 인스턴스 비율)로 변경, 하한은 1.4 실측 후 사람이 정함(TODO → SKIP) | brief `thresholds` |
| D6 | 온보딩 화면 | **UNLOCK-I 승인** → S00 역할 선택·내 정보·배우자 초대 + 게스트 랜딩 추가. 라운드 2 개시 | decisions unlock_request |
| D7 | 렌즈 승격 묶음 1 | (a) "목록 전 항목 상태 라벨 = 실패" **확정**. (b)(c) 미선택 → 후보 유지 | brief 판단기준 원장 C-4 행 |
| D8 | 제출본 | **xMsSA… Designthon-Figma-1** | brief `target.submission` |

원문은 `decisions.md` 「피드백 원문 로그」 FB-01~08.

## 4. 다음 할 일 — 라운드 2 (UNLOCK-I 승인으로 라운드 +1, 하위 2.0)

1. ~~기준값 YAML 갱신~~ 완료(D2~D5). 남은 것: REUSE-B 산식을 사실 파일 계산기에 구현하고 1.4/2.0 실측값으로 하한을 사람에게 받기
2. 더미 데이터 정합: `docs/screen-map.md` §4 fixtures를 단일 진실로 재정비(구성원·배정 상태·요일·집계) → S01/S02/S04/S06/S07/S08/S09/S10/S11 문구·아바타 수정
3. 국소 결함: S05·S09 달력 셀 폭(글리프 절단), S06 매트릭스 헤더-열 정렬, S04 배너 줄바꿈, S08 행 절단, S11 날짜 열 폭, 프레임 높이 844 통일, S10 카드 3장 이하 또는 scroll 선언
4. 측 라벨: S06·S07·S08에 `Tag/Side` 인스턴스 배치(색+텍스트)
5. A-F: 프로토타입 reactions 연결(13 CTA), S12 게스트 제출 완료 화면, **S00 온보딩 3화면 + 게스트 랜딩(D6 승인)** — 요구 계약에 REQ 신설 후 W(그레이박스) → U 순서
6. 컴포넌트: `Calendar/Day` 마스터 gap, `Response/Cell` pending "–"를 아이콘으로, ZVyw에만 있는 4종(SectionHeader·StatusTile·AckRow·ShareTile) xMsSA에 재생성
7. `contracts/requirements.json` 작성(CE-n 포함) → A-T 검증 가능하게
8. 재검: 사실 파일 재계산 → A Agent → 렌더 → Critic/Advocate → PM → 사람 판결. **라운드 2 하위 2.0**. 상한: 라운드 3, 하위 3. C-5는 D1 결과를 받아 반영

## 5. 진행 중·알아둘 것

- **다른 세션**이 청첩장 I막 시뮬레이션 인터뷰를 수행하고 U(`xMsSA…`)에 GAP-02~06을 반영했다. `brief.md`·`interview.md`·`onboarding.md`는 그 세션이 편집한다 — 충돌 주의, 편집 전 `git status` 확인.
- 검증 Agent는 오후에 조직 월 한도(429)로 1회 중단된 적 있다. 한도 걸리면 `BLOCKED`로 기록하고 재시도하지 않는다.
- Figma MCP: 읽기·속성·렌더·쓰기·변수 전부 실측 통과. `use_figma` 반환 20KB 제한 → 사실 파일 방식. `docs/figma-mcp.md`.
- ooo interview MCP는 이 세션에서 미연결(경로 B: CLI). `docs/integrations/ooo-interview.md`.
- 렌더: `renders/r2-S01..S11.png`(1.3 입력). 사실 파일: `.cache/facts-xmssa-r2.json`. 둘 다 gitignore.

## 6. 가족 여행 프로젝트 다음 단계

O단계 온보딩(`templates/onboarding.md`) → M막(레퍼런스 갤러리 `design/research/family-travel/gallery.html`이 이미 있음 — 되묻기로 LOCK-M) → W막 HTML 로우파이. target Figma 파일은 아직 없음(plan-only).

## 7. 미해결 결정 이름 (절대 규칙 5)

"C-5 판결(병렬 세션)", "A-4 REUSE-B 하한(1.4 실측 후)", "렌즈 (b) 사용자 언어·(c) 반복 요소 메인 색 — 후보 유지", "S10 세로 리스트: 카드 3장 제한 vs scroll 선언"
