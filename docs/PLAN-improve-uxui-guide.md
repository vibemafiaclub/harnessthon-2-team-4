# PLAN — `docs/PLAN_IMPROVE.md`(Figma Design Guide 25절)를 하네스 UX/UI 과정에 반영

작성일: 2026-09-05 · 상태: 계획(실행 전). 근거: `PLAN_IMPROVE.md` 전문 + `SKILL.md`·`references/` 12파일·`templates/brief.md`·`templates/contracts/requirements.json`·`harness-lessons.md`를 대조했다.

## 0. 한 줄 결론

`PLAN_IMPROVE.md`는 **"화면 하나를 어떻게 읽히게 만드는가"의 원칙 가이드**이고, 현 하네스는 **"그 원칙을 누가 언제 어떤 근거로 판정하는가"의 절차**다. 25절 중 **약 60%는 이미 하네스에 더 정밀한 형태로 있다**(3초 테스트, P0 1개, 위계 대비, 메인 컬러 범위, 관성 진단, 토큰 닫힌 어휘). **진짜 빈 곳은 6개**다 — ① 화면 메시지 구조(Primary Message/Action) 필드, ② One Page = One Step + 단계 진행 표시, ③ 점진적 노출, ④ 타이포·반경·간격 **스케일** 유도(색만 있음), ⑤ **제작 화면 간 상호 일관성**(기존 소스와의 비교만 있음), ⑥ 동일 크기 카드 그리드 금지. 나머지(Warm+Calm+Modern, Warm Ivory, 오행, 한자 히어로)는 **프로젝트 값**이므로 코어에 넣으면 검사기가 잡고 다음 프로젝트가 베낀다 — `design/<id>/brief.md` 시각 언어로 간다.

가이드의 세 가지 성질을 먼저 고정한다:
- **수신자가 "Codex"다.** 하네스는 Claude Agent 배선이다. 절차 절(§21·§22)은 이미 O단계·관성 진단·제작-L/S가 대체하므로 문구 이식이 아니라 매핑만 한다.
- **라벨형 서술이 많다.** 하네스 규칙(`stage-c` "라벨 금지, 합격선 필수")에 따라 각 항목을 **렌즈(무엇을 보면 실패인가)** 로 다시 쓰고, 숫자 합격선은 프로젝트 원장에서 사람이 승격한다.
- **Bento Grid를 "주요 레이아웃 시스템"으로 고정한다.** 이것은 B단계 축 선택이지 범용 규칙이 아니고, `forbidden-patterns.md` §4 카드 규칙과 부분 충돌한다(§3 참조).

## 1. 25절 매핑 인벤토리

상태: **있음**(그대로) / **부분**(렌즈·필드 보강 필요) / **없음**(신설) / **값**(프로젝트 원장으로)

| 가이드 절 | 내용 | 하네스 현재 위치 | 상태 | 보완 |
|---|---|---|---|---|
| §1 Core Principles 순서 | User Goal→Message→Action→Support→Layout→Visual | 4막 M→W→I→U, `experience-definition` §8~9, `screen-specification` §4~5 | 부분 | 순서는 있으나 화면당 **Primary Message / Primary Action / Secondary Info** 필드 없음 → B1 |
| §2 Main Screen 3~5초 | 핵심 메시지·Primary Information 하나 | CX1 3초 테스트(Blocker), P0 화면당 1개 | 있음 | — |
| §3 Primary CTA | Primary/Secondary 강도 구분 | C-2(상시 요소 1순위 금지·어포던스), AS6, 메인 컬러 범위 | 부분 | "Primary CTA 화면당 1개 + Secondary와 강도 차" 렌즈를 C-2에 명시, A 기계 검사(Accent 바인딩 버튼 수)로 내려보내기 → B2 |
| §3 One Page = One Step | 여러 단계 행동을 한 화면에 금지, 3요소(현재 단계/할 일/다음) | P0 1개 권장(간접) | 없음 | SP8 구조 관성 신설 + W막 §3 단계형 플로우 규칙 → B3 |
| §4 Screen Message 형식 | Screen Purpose 블록 | `screens[].purpose` 한 문장 | 부분 | B1과 동일 |
| §5 Visual Hierarchy P/S/T | 3단 위계·강조 수단 6종 | C-2, AS2(1.15배), AS6(≤3) | 있음 | Tertiary "필요할 때 읽는 정보" 한 줄만 C-2에 추가 |
| §6~7 Bento Grid | 카드 크기 = 정보 중요도, 동일 크기 금지 | 없음. `forbidden-patterns` §4 "카드는 독립 조작 단위에만" | 없음+충돌 | 범용화: "동일 크기·동일 강조 컨테이너 나열 = 위계 소실" 렌즈(C-2) + SP9. Bento 자체는 B단계 레이아웃 축 후보 → §3 결정 |
| §8 Emotional Direction | Warm+Calm+Modern | M막 무드 어휘 LOCK-M | 값 | 프로젝트 `brief.md` 시각 언어. 코어에는 "LOCK-M 어휘가 스크린샷에서 읽히는가" 렌즈만 → B6 |
| §9 Color Direction | Warm Ivory·Cream·Sand·오행 재해석 | `foundation-derivation` 유도 절차 | 값 | 프로젝트 원장. 유도 절차는 이미 더 엄격(스테레오타입 금지, 근거 한 줄) |
| §10 Typography 방향·6레벨 | Display/H1/H2/Body/Caption/Label, 임의 사이즈 금지 | A-2(스타일 참조), AS2(비율) — **스케일을 만드는 절차 없음** | 부분 | `foundation-derivation`에 타이포 스케일 유도 절 신설 → B4 |
| §11 Subject Typography | 한자 히어로 | — | 값 | 프로젝트 원장(사주 백로그) |
| §12 Component Consistency | 14요소 동일 규칙 | 닫힌 어휘, A-1~A-6, `components.json` | 있음 | — |
| §13 Layout Consistency | 화면마다 다른 디자인 문법 금지 | C-S Source-Fidelity(기존 소스·레퍼런스 대비만) | 부분 | **제작 화면 간 상호 비교** 없음 → B5 |
| §14 Design Tokens | 색 역할 토큰·radius ≤4·spacing 스케일 | `brief.md` YAML: color/type/spacing.grid만 | 부분 | YAML에 `radius.allowed`·`shadow.allowed`·`spacing.scale` 추가, A-3 판정 범위 확장 → B4 |
| §15 Component Variants | 상태 Variant | A-6 `required_states` | 있음 | — |
| §16 Hero Component 1개 | Hero + 지원 컴포넌트 | P0 1개, AS6 | 있음 | — |
| §17 Composition 순서 | Context→Message→Action→Support→Detail | W막 §4 블록 순서(위→아래) | 부분 | 기본 순서 템플릿으로 §4에 한 줄 |
| §18 Cognitive Load | Primary 버튼 5개·동일 카드 10개·다단 폼 | C-4 밀도, AS6 | 부분 | 구체 실패 예를 C-4 렌즈에 추가(라벨→렌즈) |
| §19 Progressive Disclosure | Summary→Insight→Details→Deep Dive | CE5 깊이 ≤3(반대 방향 제약만) | 없음 | W막 IA 규칙에 "상세는 진입점 안쪽, 요약이 먼저" + C-4 렌즈 → B3 |
| §20 Workflow Visualization | 현재 단계 표시 | 없음 | 없음 | B3(단계 인디케이터 블록 + A-F 존재 검사) |
| §21 Implementation Rule | 기존 Flow·Token·Component 먼저 확인 | O-3·O-6 자산 인벤토리, W막 §1-1 관성 진단 | 있음 | — |
| §22 Codex Workflow 7단계 | Understand→…→Check Consistency | 4막 + 제작-L/S + A/C/V | 있음 | Step 7만 B5로 |
| §23 Review Checklist 6묶음 | Information/Workflow/Hierarchy/Emotion/Bento/Components/Product | A-F·A-T·C-2~C-5·C-S에 분산 | 부분 | 체크 항목 ↔ 하네스 ID 대응표를 가이드 문서 끝에 부록으로(사람이 읽는 용) |
| §24 Things to Avoid 5종 | Generic AI Dashboard·장식 우선·스타일 혼용·과다 액센트·화면별 최적화 | FP1(그라디언트)·C-5 클리셰·C-S·메인 컬러 범위 | 부분 | "카드 8개 동일 크기·아이콘 8개" → SP9. "화면별 최적화" → B5 |
| §25 Final Acceptance 5문 | 5초 이해·할 일 명확·강약·감성·단일 시스템 | CX1·C-2·AS·(감성 없음)·C-S | 부분 | Q4 감성 → B6, Q5 → B5. 사람 최종 판단 질문지로 `decisions.md` 템플릿에 |

## 2. 보완 항목 B1~B6 (우선순위 순)

### B1. 화면 메시지 구조 — `screens[]`에 필드 3개 추가 (축 ③ 정밀화)
- `templates/contracts/requirements.json` `screens[]`에 `primary_message`, `primary_action`(→ `flow.edges[]`의 어느 cta인지 참조), `secondary_info[]` 추가. `purpose`는 유지(한 문장 목적).
- `screen-specification.md` §5 화면 단위 명세 표에 세 행 추가. **W막에서 채운다**(구조·순서만, 시각 아님 — 이 파일 금지 사항과 정합).
- 판정 연결: `primary_action`이 가리키는 블록 = P0 블록이어야 한다. 불일치면 W막 완료 조건 위반. C-2 렌즈 "2초 뒤 눈이 가는 곳 = `primary_message`인가"로 CX1을 구체화.
- 왜: 지금은 `purpose` 한 문장만 있어 "이 화면이 가장 강하게 전달할 것"이 명세에 없다. CX1 검증자가 무엇과 대조해 3초 테스트를 하는지 기준이 없었다.

### B2. Primary CTA 단일성 — C-2 렌즈 + A 기계 검사
- `stage-c-aesthetic.md` 판단 항목에 추가: **"Primary CTA가 화면당 하나이고 Secondary와 강도가 다른가"** — 실패: 채움 버튼 2개 이상 / Primary와 Secondary가 같은 채움·같은 크기. 통과: 채움 1 + 테두리·텍스트형.
- `stage-a-structural.md`에 A-10 신설(기존 "A단계로 내려보내는 렌즈" 목록 실행): Accent 토큰 바인딩된 **버튼 컴포넌트 인스턴스 수 = 1**(화면당). 기준값 없이도 이진 판정 가능하므로 A-0처럼 SKIP 불가로 두지 말고, `brief.md` YAML `thresholds.primary_cta_per_screen: 1`을 기본값 명시(사람이 "켤 것인가"만 답).
- 상충 처리: 빈 상태에서 FAB+본문 CTA 중복 입구(C-6)와 같은 뿌리 — 중복 카운트 금지 규칙에 C-6 우선으로 적는다.

### B3. One Page = One Step · 단계 진행 표시 · 점진적 노출 — W막 구조 규칙
- `forbidden-patterns.md` §0에 추가:
  - **SP8** 한 화면에 둘 이상의 입력 단계(다단 폼·"입력→선택→분석→결과"를 한 화면에). 왜: 사용자가 "여기서 뭘 해야 하지"를 묻게 된다. 예외: 사람이 원장에 "단일 화면 폼"을 명시 결정한 경우.
  - **SP9** 동일 크기·동일 강조의 컨테이너 반복 나열(Generic Dashboard). 왜: 카드 크기·강조가 같으면 위계가 사라진다. 카드 자체의 사용 조건은 §4(독립 조작 단위)가 우선.
- `screen-specification.md` §3 Userflow에 **단계형 플로우 규칙** 신설: 화면 3개 이상이 순서로 이어지는 흐름은 각 화면에 ① 현재 위치 블록(고정 우선순위) ② 다음 전이(`flow.edges[]`) ③ 뒤로 경로(CE6)를 갖는다. `screens[].blocks[]`에 `role: "step-indicator"` 예약. A-F에 "단계형 플로우인데 위치 블록 없음 → FAIL" 한 줄.
- `screen-specification.md` §2 IA 규칙에 **점진적 노출**: 화면 위계는 요약(P0) → 핵심 근거(P1) → 상세(P2, 진입점 안쪽). 상세가 첫 화면 스크롤 없는 영역에 있으면 P0 1개 규칙 위반으로 잡힌다(기존 규칙 재사용, 신설 ID 없음).
- C-4 렌즈에 §18의 구체 실패 예 추가(Primary 버튼 5개, 동일 카드 10개, 중요도 없는 숫자 나열).

### B4. 스케일 유도 — 타이포·반경·간격·그림자 (색만 있던 `foundation-derivation`)
- `foundation-derivation.md`에 절 신설 **"5. 스케일 유도 — 타이포·간격·반경·그림자"**:
  - 타이포: 레벨 수는 W막 블록 우선순위 종류 + 라벨/캡션에서 도출(최소 Display/Heading/Body/Caption/Label 5, 근거 한 줄). 인접 비율 ≥ 1.15(AS2와 같은 자). 화면에서 임의 크기 생성 금지 = A-2가 판정.
  - 간격: 등비/등차 스케일 1벌(예시는 "예: 4·8·12·16·24·32"처럼 표기), W막이 넘긴 **간격 종류 개수**(≤4)에 값을 배정.
  - 반경: **3~4개 이하**. 그림자: 단계 ≤2, 무채색(FP2와 정합).
  - 모든 값에 근거 한 줄(색과 같은 규칙).
- `templates/brief.md` A단계 기준값 YAML 확장: `tokens.type.scale_ratio_min`, `tokens.spacing.scale[]`, `tokens.radius.allowed[]`, `tokens.effect.shadow_allowed[]`. **키 추가만, 기존 키 이름 변경 없음**(A단계가 키를 읽는다).
- `stage-a-structural.md` A-3을 "Spacing 그리드"에서 **"Spacing·Radius·Shadow 닫힌 집합"** 으로 확장(하위 A-3a/b/c). 기준값 비면 SKIP 규칙 그대로.

### B5. 제작 화면 간 상호 일관성 — C-S 확장 + 컨택트 시트 렌더
- `stage-c-aesthetic.md` C-S에 **비교 기준 0순위** 추가: "이번 run에서 제작된 화면들 서로" — 기존 소스가 없는 greenfield에서도 `해당 없음`으로 빠지지 않게 한다. 5축(색·밀도·형태·탐색·전체 인상) 그대로 적용.
- 렌더 배선: 화면 전부를 한 프레임에 나열한 **컨택트 시트**를 `renders/r<라운드>-sheet.png`로 저장, C 검증자에 개별 스크린샷과 함께 경로 전달. §22 Step 7 "모든 Screen을 한 번에 펼쳐놓고"의 하네스 대응.
- `stage-v-flow.md`에는 새 판정을 만들지 않는다(역할 축소 원칙 유지). C-S 결과를 V가 최신 revision으로 1회 재확인만.
- `decisions.md` 템플릿의 사람 최종 판단 블록에 §25 5문항을 **질문지**로 넣는다(판정 규칙 아님 — 사람이 낸다, 절대 규칙 2).

### B6. 무드 전달 렌즈 — C-1 확장
- C-1 색온도·조명에 렌즈 추가: **"LOCK-M 무드 어휘가 스크린샷만 보고 읽히는가"** — 검증자에게 어휘 3~5단어만 주고(레퍼런스 이미지·결정 이유는 주지 않음, 격리 유지) 화면에서 받은 인상 단어 3개를 쓰게 한 뒤 겹침을 본다. 합격선(몇 개 겹쳐야 통과)은 프로젝트 원장에서 사람이 승격. 승격 전엔 OBSERVE.
- 가이드의 Warm/Calm/Modern·Warm Ivory 등은 **사주 프로젝트 값** → `docs/backlog/saju/`에 시각 언어 후보로 보관(현 활성 도메인은 family-trip, L27).

## 3. 충돌·결정 필요 3곳

| # | 충돌 | 가이드 | 하네스 | 권고 |
|---|---|---|---|---|
| D1 | Bento Grid를 기본 레이아웃으로 | "주요 레이아웃 시스템으로 활용" | `forbidden-patterns` §4 "독립 조작 단위에만 카드, 리스트 행은 카드 아님" / 카드 불변 규칙 | **하네스 규칙 유지.** Bento는 B단계 "레이아웃 문법" 축의 후보 하나로 등록하고, 가이드의 범용 부분("컨테이너 크기 = 중요도", "동일 크기 나열 금지")만 SP9·C-2 렌즈로 이식. 카드 사용 조건은 §4가 우선 |
| D2 | 가이드 문서의 성격과 위치 | 절차+원칙+프로젝트 값이 한 파일 | 층 분리(방법론 ↔ 값), `docs/`는 검사기 범위 밖 | `PLAN_IMPROVE.md`는 **입력 원문으로 보존**(수정 금지). 방법론은 references에 이식, 값은 `docs/backlog/saju/design-guide-values.md`로 분리. 이식 후 파일 머리에 "반영 위치 표" 추가 |
| D3 | 소스 라벨 | 저자·출처 미기재 | 원장 소스 5종 — 승격 전 후보 | 가이드 항목은 **디자이너 발화 원문이 아니라 정리된 원칙문**이므로 기본 `사람-해석`(후보). 사람이 "내가 쓴 기준이다"라고 확인한 항목만 `사람-원문`으로. 사람에게 저자 확인 필요(§6-1) |

## 4. 실행 순서 P0~P4 — 각 단계 끝에 `python scripts/harness/check_contracts.py <id>` ERROR 0 + 커밋

### P0. 준비 (20분)
- [x] 25절 대조·매핑표 (이 문서)
- [ ] §6 결정 3개를 사람에게 받는다. D3(저자)가 미답이면 전부 `사람-해석`으로 진행하고 가정 로그에 남긴다.
- [ ] `git stash` 여부 확인 — 현재 미커밋 변경(`SKILL.md`, `experience-definition.md` rename, `screen-specification.md`, `requirements.json`)을 먼저 커밋해 이 작업과 분리한다.

### P1. 계약·템플릿 (40분) — B1·B4 데이터 층
- [ ] `templates/contracts/requirements.json` `screens[]`: `primary_message`, `primary_action_edge`, `secondary_info[]` 추가 + `$comment`. `blocks[].role` 예약값에 `step-indicator` 주석.
- [ ] `templates/brief.md` YAML: `type.scale_ratio_min`, `spacing.scale`, `radius.allowed`, `effect.shadow_allowed`, `thresholds.primary_cta_per_screen` 추가. 수렴 판정표 9행 "C-1~C-6" → "C-1~C-7·C-X·C-S"로 갱신(이미 어긋난 상태).
- [ ] `templates/decisions.md` 사람 최종 판단 블록에 §25 5문항 질문지.
- [ ] 검사기: `TODO` 값 처리 규칙이 새 키에도 적용되는지 확인(키 추가만이라 코드 변경 없을 가능성 높음 — 실행해 확인).

### P2. 방법론 references (1시간) — B2·B3·B4·B5·B6
- [ ] `screen-specification.md`: §2 점진적 노출 규칙, §3 단계형 플로우 규칙, §4 기본 블록 순서 한 줄, §5 표에 메시지 3행, 완료 조건·금지 사항에 SP8/SP9 반영.
- [ ] `forbidden-patterns.md` §0: SP8·SP9 행 + 표 헤더 "SP1~SP9". `stage-a` A-8 표는 FP만이므로 변경 없음.
- [ ] `foundation-derivation.md`: "5. 스케일 유도" 절 신설.
- [ ] `stage-a-structural.md`: A-3 확장(a/b/c), A-10 Primary CTA 수, A-F에 단계 인디케이터 존재 검사 한 줄. 종합 판정표의 "A-1~A-6" 범위를 "A-1~A-6·A-10"로.
- [ ] `stage-c-aesthetic.md`: 항목 지도 갱신(C-1 무드 어휘 / C-2 Primary CTA 단일성·Tertiary / C-4 구체 실패 예 / C-S 0순위 상호 비교), 스크린샷 배선에 컨택트 시트 경로, 중복 판정 규칙(A-10↔C-2, C-6↔B2).
- [ ] `SKILL.md` 워크플로 표: U 제작-L 행 산출물에 "스케일 4종", C 행에 "컨택트 시트" 추가. 참조 파일 목록 변경 없음(새 파일 안 만듦).
- [ ] 각 이식 절 머리에 `> 출처: docs/PLAN_IMPROVE.md §n (2026-09-05, 소스=사람-해석)` 표기 — 기존 합병 노트 관례.

### P3. 프로젝트 값 분리 + 원문 보존 (20분) — D2
- [ ] `docs/backlog/saju/design-guide-values.md` 신설: §8·§9·§11의 감성·색·타이포 방향을 M막 시각 언어 **후보**(소스 `사람-해석`, probe 없음)로 정리. 활성 프로젝트(family-trip·invitation-scheduler) 원장에는 넣지 않는다.
- [ ] `docs/PLAN_IMPROVE.md` 머리에 "반영 위치 표"(§n → 파일·ID) 블록만 추가, 본문 무수정.
- [ ] `check_contracts.py` 실행 — `docs/`는 CORE 밖이라 통과해야 정상. references에 "사주·오행·Warm Ivory" 유입 0 확인(`domain_terms`에 없으면 grep으로 수동 확인).

### P4. 리허설·기록 (30분)
- [ ] 청첩장 run(`design/invitation-scheduler/`) 기존 `requirements.json` 화면 1개에 `primary_message`·`primary_action_edge`를 채워 보고, 그 화면 렌더로 C-2 신규 렌즈·A-10이 판정을 내는지(OBSERVE/PASS/FAIL 중 무엇이 나오는지) 확인. **판정 결과로 기준을 고치지 않는다** — 배선 확인만.
- [ ] `harness-lessons.md` L41 추가: "원칙 가이드는 라벨이 많아 그대로 넣으면 검증자가 매번 다른 답을 낸다 → 렌즈+합격선 분리로 이식, 값은 프로젝트로".
- [ ] 커밋 메시지에 B1~B6·SP8/SP9·A-10 ID 명시.

## 5. 이식하지 않는 것 (이유 함께)
- **§6~7 Bento Grid 레이아웃 자체** — 레이아웃 문법은 B단계 축 선택. 코어에 넣으면 모든 프로젝트가 Bento가 된다(D1).
- **§8·§9·§11 감성·색·한자 값** — 프로젝트 값. 검사기 원칙.
- **§21·§22 Codex 절차문** — O단계·관성 진단·제작-L/S가 이미 더 세밀. 중복 정본 금지.
- **§23 체크리스트를 별도 체크리스트 파일로** — A/C 렌즈에 흡수. 정본 두 벌 금지(L40).
- **"Codex" 수신자 표기** — 하네스는 검증자 격리 배선으로 판정 주체를 정한다. 특정 모델 이름을 방법론에 쓰지 않는다.
- **가이드 §25를 자동 판정 규칙으로** — "이 정도면 됐다"는 사람이 낸다(절대 규칙 2). 질문지로만.

## 6. 실행 전에 사람이 정할 것
1. **D3 저자·소스**: `PLAN_IMPROVE.md`를 누가 썼는가. 본인 기준이면 해당 항목을 `사람-원문`으로 승격 가능. 외부 정리문이면 전부 `사람-해석`(후보).
2. **D1 Bento**: B단계 레이아웃 축 후보로만 둘지(권고), 아니면 특정 프로젝트의 사람 지정 결정으로 그 원장에 잠글지.
3. **B2 A-10 기본값**: `primary_cta_per_screen: 1`을 기본 ON으로 둘지, 프로젝트마다 사람이 켤지(권고: 기본 ON — 가이드 §3과 C-6 중복 입구 규칙이 같은 방향).
4. **B4 스케일 하한**: 타이포 레벨 최소 개수(가이드 6, 권고 5)와 반경 상한(가이드 3~4)을 코어 기본값으로 둘지, 원장 TODO(사람 입력)로 둘지. 판단기준·기준값 TODO는 원칙상 사람 몫이므로 **원장 TODO + 가이드 값을 "예:"로 표기**를 권고.
5. **§8~11 값의 목적지**: `docs/backlog/saju/`(권고, 도메인 일치) 또는 폐기.
