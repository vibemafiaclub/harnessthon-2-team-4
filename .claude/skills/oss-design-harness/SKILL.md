---
name: oss-design-harness
description: Figma 파일 안에서 화면을 만들거나 기존 Figma 화면을 검수·개선할 때 사용한다. 디자인 프로세스 4막(M 무드 → W 와이어프레임(HTML→Figma) → I 기능 인터뷰 → U UI 상세)과 단계별 확정 잠금(LOCK) 위에 현업 디자이너의 판단 기준을 0/B/A/C/V 단계(요구사항 정렬 → 병렬 발산·수렴 → 구조 검증 → 미적 검증 → 실재·흐름 검증)로 적용하고, Figma MCP로 실제 파일의 컴포넌트·오토레이아웃·배리언트·변수를 조작한다. "Figma 화면 만들어줘", "Figma로 UI 시안 뽑아줘", "이 Figma 파일 검수해줘", "Figma 디자인 시스템 지켜서 만들어줘" 같은 요청에 발동한다. Figma MCP가 미인증·미연결 상태여도 이 스킬을 먼저 발동한다 — 연결 확인과 인증 요청·폴백은 스킬 내부의 게이트(G-4)가 처리하므로, MCP가 안 붙어 있다는 이유로 스킬 없이 답하지 않는다. 코드(HTML/CSS/React)로 UI를 만드는 작업에는 발동하지 않는다 — 이 하네스는 Figma 파일을 직접 조작하는 경우에만 쓴다.
---

# oss-design-harness — 라우터

이 파일은 **규칙·게이트·라우팅**만 담는다. 방법론은 `references/`에, 프로젝트 값은 `docs/projects/<id>/`·`design/<id>/`에 있다. 방법론 파일에 프로젝트 답을 쓰면 다음 프로젝트가 베낀다(검사기 `scripts/harness/check_contracts.py`가 잡는다).

## 대원칙 — 좋은 디자인의 정의 (`references/design-principle.md`)

> 좋은 디자인이란, 주어진 규칙과 구조를 지켜서(①) 심미적으로 안정적인 UI를 구현하여(②) 유저의 핵심경험을 서포트하는 것(③)이다. 세 축은 AND다. ③은 화면만 봐서는 알 수 없으므로 **요구 계약으로의 추적성**으로만 검증되고, 추적 근거가 없으면 `Pass`가 아니라 `검증 불가`다.

## 이 파일의 상태 — 무엇이 채워졌고 무엇이 비었는가

- **채워진 것 = 구조.** 게이트, 라우터, 서브에이전트 배선, 검증자 격리, 판정 규칙, 라우팅, 카운터. 손대지 않아도 실행된다.
- **빈 것 = 판단기준.** `TODO`로 표시된 곳. **이걸 채우는 것이 곧 당신의 안목을 코드화하는 작업이다.**

## 절대 규칙 — 모든 단계에 적용

### 1. `TODO`는 세 종류다. 반드시 구분한다

| 종류 | 어디에 있나 | 행동 |
|---|---|---|
| **판단기준·기준값** | SKILL.md의 A단계 기준값, C단계 6항목, 후보 개수 등 | **사람에게 묻고 멈춘다.** 추측 금지. |
| **절차** | SKILL.md에서 "어떻게 할지"가 빈 곳 (레퍼런스 소싱, 역추출 방법, 축 식별, 라우팅 판별) | **기본 절차로 진행한다.** 멈추지 않는다. 사람이 나중에 조정한다. |
| **산출물** | `brief.md`·`decisions.md` 안의 모든 TODO | **각 단계가 채운다.** 정상 작업이다. |

- **판단기준을 추측해서 채우면** 이 하네스의 목적(사람의 안목 추출)이 그 자리에서 무너지고, **무너진 것이 성공처럼 보인다** — 그럴듯한 화면과 채워진 문서가 남으므로 사람은 작동했다고 믿는다.
- **절차 TODO에서 멈추면** 하네스가 첫 실행에서 진행 불가가 된다. 절차는 하네스의 일이고, 판단기준은 사람의 일이다.
- ★ **`TODO`라는 글자는 "비어 있음"과 같다.** `tokens.color.allowed: [TODO]`를 유효한 허용 목록으로 읽지 않는다. `TODO`·`TBD`·빈 값은 전부 미기입으로 간주해 `SKIP` 처리한다. 값으로 읽으면 화면의 모든 색이 FAIL이 되고 수치 비교는 크래시한다.
- 어느 종류인지 애매하면 사람에게 묻는다.

### 2. 최종 "이 정도면 됐다" 판단은 항상 사람이 낸다
에이전트가 완료를 자체 선언하지 않는다. 축별 후보 선택도 사람이 한다(B-4 참조).

### 3. 확정 안 된 정보는 침묵하지 않고 `brief.md` 가정 로그에 명시한다
`brief.md`가 아직 없는 시점의 가정은, 파일을 만든 직후 첫 항목으로 옮겨 적는다.

### 4. 검증하는 에이전트 ≠ 만든 에이전트
문장이 아니라 배선으로 지킨다 — 아래 「검증 Agent 배선」 참조.

### 5. 멈출 때는 미해결 결정의 이름을 남긴다
정지·차단·에스컬레이션 사유를 "상한 도달"·"라운드 소진"·"기준값 없음" 같은 상태 서술로 끝내지 않는다. **무엇이 안 풀렸는지를 이름으로 쓴다** — 예: "C-1 색온도 기준 미확정 — 디자이너 확인 필요", "라운드 2·3 연속 C-4 탈락". 재개하는 사람이 보고만 읽고 무엇을 풀어야 하는지 알아야 한다.

---

## 프로젝트 설정 — 코어는 값을 갖지 않는다

이 스킬은 **절차만** 담는다. 도메인 값(화면 이름·상태 enum·토큰·더미 데이터·대상 파일)은 전부 프로젝트 설정에서 읽는다.

- 프로젝트 설정: `docs/projects/<project-id>/project.json` — `prd_path`, `brief_path`, `system_brief_path`, `artifact_root`, `domain_terms`(코어 누출 검사용)만 둔다. **target(파일 URL·페이지·프레임)은 여기에 복제하지 않는다** — target의 권위 있는 원장은 `brief.md`의 `target` 블록 하나다.
- 과제 전용 스킬(예 `wedding-scheduler-figma`)은 project-id를 고르는 얇은 래퍼다. 전용 스킬 안에 파일 키·노드 ID를 상수로 적지 않는다 — 원장과 어긋나는 순간 다른 파일에 쓴다.
- **도메인 누출 금지**: 이 파일과 `templates/`에는 특정 프로젝트의 화면명·상태값·색·인명이 들어가면 안 된다. `scripts/harness/check_contracts.py`가 `domain_terms`로 검사한다. 예시가 필요하면 "예: …"로 표시하고 프로젝트 문서로 옮긴다.
- 다른 도메인으로 바꿀 때는 project.json·PRD·원장·`_system`을 새로 만들고 코어는 그대로 쓴다. 이전 프로젝트의 `_system/brief.md`(색·상태 어휘)를 상속하지 않는다. 등록된 프로젝트 목록은 `docs/projects/`.

## 워크플로 한눈에 — 어디서 무엇을 읽나

| 단계 | 무엇 | 방법론 파일 | 산출물 |
|---|---|---|---|
| O 온보딩 | 누가·무엇으로·어디서부터 | `references/process-acts.md` | `onboarding.md`, GATE onboarding |
| 게이트 G-1~G-4 | 루트·템플릿·target·MCP 실측 | 이 파일 | — |
| M 무드 | 레퍼런스 되묻기 → 무드 어휘 잠금 | `process-acts.md`, `reference-research.md`, `stage-0-alignment.md` | brief 시각 언어, LOCK-M |
| 0 원장 | 요구·판단기준 수렴, 소스 5종 | `stage-0-alignment.md` | `brief.md`, `contracts/requirements.json` |
| 0 핵심경험 | 페르소나·`CE-n` **초안**·인접 경험 (축 ③의 근거) | `experience-definition.md` | brief 핵심경험 섹션, `core_experiences[]` |
| B 발산·수렴 | 축 분리·후보 3개·교차 비평·사람 선택 | `stage-b-diverge.md` | `decisions.md` |
| W 기획 | 화면 목록·IA 3안·Userflow·블록 위계·추적성 계획 | `screen-specification.md` | `screens[]`, `flow.edges[]`, `edge_states_planned[]` |
| W 와이어프레임 | HTML 로우파이 → 컨펌 → Figma W | `process-acts.md` | W 화면, LOCK-W |
| I 기능 인터뷰 | 시나리오 과제, ooo interview, **`CE-n` 승격** | `process-acts.md`, `experience-definition.md`, `docs/integrations/ooo-interview.md` | `interview.md`, LOCK-I |
| U 제작-L/S | 토큰 유도 → 컴포넌트 → 화면 | `foundation-derivation.md`, `figma-playbook.md` | Figma, 스냅샷, `contracts/components.json` |
| A 구조 검증 | A-F 커버리지 → A-T 추적성 → A-0 하한선 → A-1~A-9 | `stage-a-structural.md` | decisions 검증 로그 |
| C 미적 검증 | 스크린샷, C-1~C-7·C-X·C-S, Critic/Advocate/PM | `stage-c-aesthetic.md` | decisions 검증 로그 |
| V 최종 재확인 | 최신 revision 실재 | `stage-v-flow.md` | GATE verify-V |
| 라우팅·상한 | 반복실패>결정충돌>방향오류>국소 | `verify-routing.md` | decisions 라운드 |

`design-verify` 스킬은 "검증해줘" 요청의 **얇은 진입점**이며 같은 `references/`를 읽는다. 진단 정본은 `verify-routing.md` 하나다.

## 모드 — 무엇을 할 세션인지 먼저 정한다

| 모드 | 하는 일 | 게이트 | Figma 쓰기 |
|---|---|---|---|
| `plan-only` | PRD → 요구 계약·화면 지도·원장 초안. 대상 파일이 없어도 된다 | G-1·G-2만 | 없음 |
| `build` | 선택된 후보를 Figma에 제작 | G-1~G-4 전부 | 있음 (worker 1명) |
| `review` | 기존 프레임을 A/C/V로 검수만 | G-1·G-3·G-4 | 없음 |
| `improve` | 기존 run의 GAP 목록을 받아 수정·재검 | G-1~G-4 | 있음. **라운드 카운터를 이어 쓴다** — 새 run ID로 상한을 초기화하지 않는다 |

모드는 `decisions.md` 라운드 헤더에 적는다. `plan-only`에서 만든 문서를 "제작 완료"로 보고하지 않는다.

## 게이트 — 라우터보다 먼저 통과시킨다

라우터가 파일 존재로 분기하므로, 무엇을 어디서 볼지 먼저 확정해야 한다. 넷 다 통과하지 못하면 다음으로 가지 않는다.

**G-1. 산출물 루트 확정.**
기본값 `<cwd>/design/<project-id>/`(project.json의 `artifact_root`). 이미 있으면 그것을 쓰고, 없으면 사람에게 확인하고 만든다.
★ **이 경로를 세션 내내 고정한다.** 중간에 바뀌면 이전 `decisions.md`를 못 찾아 라운드 1로 재시작하고, 그 순간 재시도 카운터와 반복실패 판정 근거가 함께 사라진다.

**G-2. 템플릿 복사.**
산출물 루트에 `brief.md`·`decisions.md`가 없으면 이 스킬 레포 루트의 `templates/`에서 복사한다(스킬 파일 기준 상위 경로다 — `.claude/skills/` 아래가 아니다). **이미 있으면 복사하지 않는다.**

**G-3. 대상 Figma 파일 확정.**
파일 URL·페이지·프레임을 사람에게 묻고 `brief.md`의 `target` 키에 기록한다. 이게 없으면 제작·A·C단계가 무엇을 대상으로 하는지 알 수 없다.
- 사용자가 URL을 주지 않아 에이전트가 새 파일을 만들었으면 **가정 로그에 "확인 필요: 높음"으로 남기고, 첫 보고에서 URL을 사용자에게 보여 준다.** 제작이 한참 진행된 뒤 사용자가 다른 파일을 지정하면 재현 비용이 두 배가 된다(실제 발생: 1차 제작본과 사용자 지정 파일이 갈라져 두 파일에 나뉘어 존재).
- **같은 파일에 쓰는 세션은 하나만.** 다른 에이전트·세션이 같은 파일에 쓰고 있다는 징후(내가 만들지 않은 노드가 생김, 컴포넌트가 이미 존재)가 보이면 쓰기를 멈추고 사람에게 어느 세션이 소유자인지 묻는다. 두 세션이 같은 스크립트를 병렬로 돌리면 컴포넌트가 중복 생성되고 하나는 크기 버그를 안은 채 남는다.
- target이 바뀌면 이전 파일의 node ID를 재사용하지 않는다. `brief.md`에 `backup:`으로 이전 파일을 남기고 어느 파일이 제출본인지 **미해결 결정의 이름**으로 적는다.

**G-4. Figma MCP 스모크 테스트.**
`docs/figma-mcp.md`의 실측 절차를 통과시킨다. **미통과면 여기서 멈춘다.** 인증은 `/mcp` 슬래시 커맨드로만 가능해 **에이전트가 수행할 수 없다** — 사람에게 요청한다. 0·B단계를 먼저 돌고 나서 인증 벽에 부딪히면 그 작업이 낭비된다.
- 실측 결과는 `docs/figma-mcp.md`의 표에 **읽기 / 노드 속성 / 렌더 / 쓰기 / 변수·스타일 조작** 다섯 능력으로 나눠 기록한다. 하나라도 없으면 해당 단계의 폴백을 함께 적는다.
- **429·한도 초과는 자동 재시도하지 않는다.** 원인·시각·재개 조건을 `decisions.md`에 적고 사람에게 보고한다. 검증 Agent가 한도로 중단되면 그 항목은 `BLOCKED`(판정 불가)다 — PASS도 FAIL도 아니다.

## 라우터 — 위에서부터 첫 번째로 맞는 행

| 조건 | 진입 |
|---|---|
| `onboarding.md` 없음 또는 GATE `stage: onboarding` 미PASS | **O단계** (온보딩) |
| 게이트 미통과 | **정지** — 사람에게 요청 |
| 사람이 **검수·검증만** 요청 + 대상 프레임 있음 | **A단계** (0·B·제작 건너뜀) |
| `brief.md` 없음 / 원장 미수렴(수렴 판정표에 열린 갭) / 무엇을 만들지 불확실 | **0단계** |
| `brief.md` 있고 `contracts/requirements.json`에 `core_experiences[]` 없음 | **0단계 핵심경험** (`experience-definition.md`) |
| `brief.md` 있고 `decisions.md`에 선택된 후보 없음 | **B단계** |
| 후보 선택됨, `W Wireframes` 페이지에 화면 없음 | **W막** (`screen-specification.md` 기획 → `process-acts.md` 매체) |
| W 있음, `interview.md` 없음 또는 GATE `stage: interview` 미PASS | **I막** (기능 인터뷰) — 생략은 사람 결정 + 가정 로그 |
| I막 PASS, 대상 프레임(U) 없음 | **제작단계** (U막) |
| 대상 프레임 있음, A단계 미실시 | **A단계** |
| A단계 FAIL | **A-라우팅** |
| A단계 통과 | **C단계** |
| C단계 FAIL | **C-라우팅** |
| C단계 통과, V 미실시 | **V단계** (실재·흐름 검증) |
| V단계 통과 | **사람 최종 판단** |

상태 저장소를 따로 두지 않는다 — **산출물 파일이 곧 상태다.**

## 재시도 상한 — 두 층위

`decisions.md`가 카운터를 겸한다. 별도 저장소를 만들지 않는다.

| 층위 | 무엇을 세는가 | 기록 위치 | 기본 상한 |
|---|---|---|---|
| **라운드** `N` | B단계 재발산 횟수 | `decisions.md` 라운드 헤더 | 3 |
| **하위 라운드** `N.k` | 같은 라운드 안의 국소 수정·A재검 횟수 | 해당 라운드의 재검 로그 | 3 |

★ **하위 카운트가 없으면 국소 결함 루프와 A-라우팅은 무한 반복 가능하다.** 둘 다 B단계를 거치지 않아 라운드가 늘지 않기 때문이다. 반드시 `N.k`를 증가시킨다.

**상한 도달 판정**: 라운드 3이 **C단계에서 탈락한 시점**에 멈춘다 — "라운드 3을 시작할 때"가 아니다(그러면 실질 상한이 2가 된다). 하위 라운드도 같다: `N.3`이 실패한 시점.

상한에 닿으면 사람에게 에스컬레이션하고 **멈춘다. 에이전트가 상한을 스스로 늘리지 않는다.** 보고 사유는 "상한 도달"이 아니라 **미해결 결정의 이름**이다(절대 규칙 5) — 어떤 항목이 어느 라운드에서 계속 탈락했고 어떤 기준이 미확정인지.
- **TODO**: 이 프로젝트의 상한 (기본 3에서 바꿀 경우)

## 참조 파일 목록

- `references/design-principle.md` — 3축 정의·결합 규칙·충돌 우선순위 (iceberg 이식)
- `references/process-acts.md` — O단계, 4막, LOCK/UNLOCK, GATE, 재개
- `references/stage-0-alignment.md`, `reference-research.md`, `foundation-derivation.md`
- `references/experience-definition.md` — 🔴 **축 ③의 입력 생산.** 페르소나·`CE-n`·인접 경험 (iceberg P단계 이식). 이게 없으면 A-T·C-X가 판정할 대상이 없어 축 ③이 상시 `검증 불가` → FAIL
- `references/stage-b-diverge.md`
- `references/screen-specification.md` — W막 기획 방법론. 화면 목록·IA 3안·Userflow·블록 위계·추적성 계획 (iceberg S단계 이식). `process-acts.md` W막 규칙은 **매체**, 이 파일은 **무엇을 기획하나**
- `references/figma-playbook.md` — 제작-L/S, 스냅샷 계약, Plugin API 함정 합집합
- `references/stage-a-structural.md`, `stage-c-aesthetic.md`, `stage-v-flow.md`, `verify-routing.md`
- `references/forbidden-patterns.md` — FP1~FP6 (iceberg 이식)
- `references/platform-hig-ios.md` — iOS 프로젝트에서만
- 어댑터: `docs/integrations/ooo-interview.md`
