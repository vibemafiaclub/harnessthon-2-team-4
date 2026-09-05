# PLAN — `dev`(현재) × `origin/feat/yj1` 하네스 합병

작성일: 2026-09-05 · 상태: 계획(실행 전). 실측 근거: `git fetch` 후 `origin/feat/yj1` 5커밋(`3eb287c`~`7ea5cc8`)을 스크래치 워크트리로 체크아웃해 전 파일을 읽었다. `origin/harness/layer-split`은 yj1의 앞 2커밋과 동일하므로 별도 취급하지 않는다.

## 0. 한 줄 결론

두 브랜치는 **같은 뼈대(0/B/A/C, 사람 승격, 층 분리)**에서 출발해 **서로 다른 방향으로 깊어졌다.**
- `feat/yj1`: **판정의 디테일** — 디자이너 실피드백에서 역추출한 C단계 13항목, A단계 기능 커버리지(사용자 설정·역할 결정 지점·흐름 연결·프로토타입), Foundation(색) 유도 규칙, 레퍼런스 리서치 절차, Figma 함정 5종, "기준 오류" 판정, 결정충돌 라우팅.
- `dev`: **운영의 뼈대** — O단계 온보딩, 4막(M/W/I/U)+LOCK, 되묻기, ooo interview 어댑터, GATE 인수인계, V단계, 프로젝트 설정+검사기, 소스 5종, 스냅샷 계약, A-4 산식, 429/격리 규칙, 두 번째 도메인(family-trip).

겹치는 부분은 표현만 다를 뿐 모순이 거의 없다. **충돌은 파일 배치와 용어 3곳**이다(§3). 합병은 "텍스트 머지"가 아니라 **yj1의 방법론을 dev의 구조 안에 이식**하는 방식이 안전하다.

## 1. 양쪽 인벤토리

| 영역 | feat/yj1 | dev | 합병 후 |
|---|---|---|---|
| 코어 스킬 | `oss-design-harness/SKILL.md`(짧은 라우터) + `references/` 4파일(stage-0, reference-research, stage-b, figma-playbook) | `oss-design-harness/SKILL.md` 단일 대형 파일(O·4막·LOCK·게이트·0/B/제작/A/C/V/라우팅) | **dev 구조 유지 + yj1의 `references/` 분할 방식 채택** — SKILL.md는 라우터·규칙만, 방법론은 `references/`로 |
| 검증 스킬 | 별도 `design-verify` 스킬(A/C + 진단 4종 정본) | SKILL.md 안 A/C/V + `wedding-scheduler-figma` §3 브리프 템플릿 | `design-verify`를 **얇은 진입점**으로 유지("검증해줘" 트리거), 판정 방법은 `references/stage-a/c/v.md`, 정본은 하나 |
| 검증 이력 | `verify-log.md`(화면별 C 시도 횟수 + 기준 정정 기록) | `decisions.md` 검증 로그 하위 라운드 + GATE | `decisions.md`에 **화면별 시도 횟수 표**와 **기준 정정 기록 표** 추가(yj1 포맷 이식). 파일 하나 유지 |
| 기준값 위치 | `projects/<슬러그>/criteria.md`(기능 커버리지 표 + A/C 합격선) | `brief.md` A단계 기준값 YAML + 판단기준 원장 | `brief.md` 유지 + **`contracts/requirements.json`에 기능 커버리지 표**(yj1 criteria §A단계 기능 커버리지 ↔ dev V-1/V-2). criteria.md는 만들지 않음(원장 이원화 방지) |
| 프로젝트 폴더 | `projects/cheongchup-scheduler/` | `docs/projects/<id>/project.json` + `design/<id>/` | **dev 배치 유지**. yj1 프로젝트는 `design/invitation-scheduler/runs/yj1/`로 보존(§4) |
| 템플릿 위치 | `.claude/skills/oss-design-harness/templates/` | 루트 `templates/` | 루트 `templates/` 유지(검사기 `CORE_FILES` 경로·README 참조). yj1의 `verify-log.md` 내용은 decisions 템플릿에 흡수 |
| 진입 문서 | `CLAUDE.md`(불변 규칙 7개, 층 분리) | `AGENTS.md`(팀 배선·MCP 규약·보고 형식) | **둘 다 유지**. CLAUDE.md는 Claude 진입점(불변 규칙 + dev의 O단계·LOCK 추가), AGENTS.md는 다중 에이전트 계약 |
| .gitignore | `harness-status.html`, `tools/` | 비밀·`.cache/`·`renders/` | 합집합 |

## 2. 시너지 — yj1에서 가져올 것 (우선순위 순)

### 2-1. C단계 판단 항목 13종 (최고 가치)
yj1 `stage-c-aesthetic.md`의 항목은 **디자이너 실피드백에서 역추출**된 것이고 각각 "무엇을 보면 실패인가"가 적혀 있다. dev의 C-1~C-6은 태그 6개뿐이라 대부분 SKIP이었다.
- 이식: `references/stage-c-aesthetic.md`를 그대로 들여오고, dev의 C태그 체계와 매핑한다.
  - C-2 위계 ← 시각적 위계(상시 요소가 1순위 금지, 그룹 헤더 강도), 상태 구분의 대비 강도, 누를 수 있는 것이 눌러 보이는가
  - C-4 밀도 ← 정보 밀도, 기본 상태 표시 금지, 압축 표기 자립성
  - C-5 클리셰 ← 메인 컬러 사용 범위, 반복 요소 색(장식/회피 대칭 실패), 클리셰/AI슬롭, 더미 데이터 현실 분포
  - C-6 엣지케이스 ← 엣지케이스 완성도, 파괴적 행동 구분, 이진 선택 컨트롤 하나, 색 부호화 범례, 중복 입구
  - 신설 **C-7 문구·라벨**: 상태 라벨이 사용자 언어인가(yj1) + UI 문구 표기용 기호 금지(yj1 A항목이지만 판단이 갈리므로 C)
- 원장 처리: 이 항목들은 dev 소스 어휘로 **`사람-원문`(yj1 디자이너 피드백)** 이다. 다만 **어느 디자이너의 어떤 원문인지 yj1에 남아 있지 않다** → 합병 시 `brief.md` 판단기준 원장에 "출처: feat/yj1 stage-c 2026-09-05 디자이너 피드백(원문 미보존)"으로 적고 상태는 **후보**. 현 프로젝트에서 사람이 승격해야 확정.

### 2-2. A단계 기능 커버리지 → dev V단계와 합친다
yj1 A-0 "기능 커버리지"(요구 1:1 대조, 유저스토리 역할 누락, **사용자 설정 지점·역할 결정 지점**, 흐름 끊김 3지점, **프로토타입 연결 `reactions` 검사**, 난제가 결정 시점 화면에 있는가, 엣지케이스 존재) = dev V-1/V-2/V-3/V-4와 같은 관심사.
- yj1은 이걸 **A단계 맨 앞**에 둔다("없는 화면은 스크린샷에 안 찍힌다"). dev는 C 뒤 V단계. **yj1 순서가 맞다** — dev의 V-1~V-6을 **A-F(기능 커버리지)로 A단계 맨 앞에 이동**하고, V는 "C 통과 후 최종 실재 재확인"으로 축소한다.
- 추가 항목 이식: **사용자 설정 지점**(앱 온보딩 화면 — "역할선택 → 내정보 → 파트너 초대"; dev 청첩장 U에는 이것이 없다 → GAP), **역할별 내비게이션 분리**, **프로토타입 연결 0개 = 실패**(dev V-3의 "표현됨/연결됨"을 판정으로 승격), **난제가 결정 시점 화면 안에 있는가**.

### 2-3. "기준 오류" 판정 (A단계 실패 시)
yj1: 위반이 **파일 전반에 일관**되면 산출물이 아니라 기준이 틀린 것 → 기준을 고치고 기록. dev A-라우팅 4("2회 연속 FAIL이면 사람 확인")보다 정교하다. 이식하되 dev 규칙 추가: **기준 정정은 사람 승인 후**, `decisions.md` "기준 정정 기록" 표에 남기고 `brief.md` YAML을 고친다. 조용히 느슨하게 바꾸기 금지(양쪽 동일 원칙).

### 2-4. 진단 4종 — `결정충돌` 추가
yj1의 결정충돌(0단계 결정 vs B단계 결정이 모순 — 예: "카드 3요소" vs "마감은 1급 정보") = dev에 없는 분류. dev의 반복실패>방향오류>국소결함 순서에 **결정충돌을 방향오류 앞**에 넣는다: 반복실패 > 결정충돌 > 방향오류 > 국소결함. 결정충돌은 LOCK 체계에서 **UNLOCK 요청**으로 처리된다(사람 재논의) — 두 체계가 자연스럽게 맞물린다.

### 2-5. Foundation(색·타이포) 유도 규칙 + 팔레트 파생
yj1 `stage-0-alignment.md` §4: 과업 정서 → 채도 상한, 페르소나 환경 → 대비 하한, 상태색 개수 = 요구 상태 수, 메인 1개에서 파생, 색가족 3개 초과 금지, **도메인 스테레오타입 금지("결혼이니까 핑크")**, 토큰마다 근거 한 줄 필수.
- dev M막(무드)과 정확히 이어진다: **M막 = 무드 어휘·레퍼런스 잠금(LOCK-M)**, **yj1 §4 = LOCK-M 어휘에서 U막 토큰 값을 유도하는 절차**. `references/foundation-derivation.md`로 이식하고 U막 제작-L 첫 단계로 연결.
- dev L5(대비율 61건)의 사후 규칙("소프트 배경 위 라벨 대비 미리 계산")을 이 문서에 합친다.

### 2-6. 레퍼런스 리서치 절차
yj1 `reference-research.md`: 3축 검색(과업 구조/도메인/정서), 소스별 성격(정보구조는 실서비스, 마감은 컨셉샷), **"봤는가" 열**(이미지 미확인 레퍼런스로 톤 판단 금지), 반례 1~2개 의도적 보존, 조합 판단 5단계, **클라이언트 부재는 스킵 사유가 아님**.
- dev 0-2 루프의 "레퍼런스 소싱 TODO(절차)"를 이것으로 채운다. dev `templates/reference-review.md`(다른 세션 산출)와 yj1 `references.md` 양식을 대조해 하나로.
- dev 되묻기 규칙(유사 변형 2~3개)은 yj1에 없다 → 유지.

### 2-7. Figma 함정 합집합
yj1 `figma-playbook.md`: `setBoundVariableForPaint`가 opacity를 떨어뜨림(→ solid 틴트 토큰), 렌더 캐시 지연(속성 정상·그림 깨짐), 아이콘+라벨 묶음, 컴포넌트 기본값=최소 상태, 인스턴스 자식 `remove()` 불가, 로컬 컴포넌트 `importComponentByKeyAsync` 불가 → `swapComponent(노드)`, 속성 변경 후 인스턴스 재조회.
dev 제작단계 함정: FRAME description 없음, resize→hug 해제, combineAsVariants 같은 페이지, 원본 삭제 전 텍스트 복사, content 높이 검사, 음수 gap 배수, 대비율 사전 계산, 20KB 스냅샷.
→ `references/figma-playbook.md` 하나로 합친다(dev L7~L11 + yj1 6종). 중복 0.

### 2-8. A단계 신규 기계 검사 2종
yj1: **UI 문구 표기용 기호(·, /, —) 금지**(→ 말로 풀기), **아이콘 자리에 이모지·문자 기호 금지**(VECTOR/INSTANCE만). 둘 다 `findAll` 조회로 판정 가능 → dev 사실 파일(facts) 계산기에 `A1x.symbolsInCopy`, `A1x.emojiIcons` 필드 추가.

### 2-9. 온보딩 화면(앱 UX) — dev 청첩장 U의 실제 GAP
yj1 verify-log #13: "사용자 설정·역할 결정 지점 부재 → 온보딩 3화면 신설(역할선택 → 내정보 → 파트너 초대)". dev 청첩장 U(S01~S11)에도 **커플 연결·역할 진입 화면이 없다**. 합병 후 청첩장 I막 인터뷰 과제에 넣고, W에 S00 계열로 추가 대상.

## 3. 충돌 — 결정이 필요한 3곳

| # | 충돌 | yj1 | dev | 권고 |
|---|---|---|---|---|
| C1 | 프로젝트 산출물 위치 | `projects/<슬러그>/` | `docs/projects/<id>/project.json` + `design/<id>/` | **dev** — project.json·검사기·GATE가 이 경로에 묶여 있다. yj1 파일은 `design/invitation-scheduler/runs/yj1/`로 이동 보존 |
| C2 | 기준값 파일 | `criteria.md`(제작 **전** 작성 강제) | `brief.md` YAML(원장 하나) | **dev 위치 + yj1 원칙** — "제작 전에 기준을 적는다"를 GATE `build-library` 진입 조건에 추가 |
| C3 | 검증 정본 위치 | `design-verify` 스킬이 진단 정본 | SKILL.md 단일 | **`references/`가 정본**, 두 스킬(oss-design-harness, design-verify)은 모두 그것을 참조. 정본이 두 곳이면 어긋난다(yj1 자신의 원칙) |
| 용어 | 진단 3종 vs 4종 / A-0 의미(dev: 고정 하한선, yj1: 기능 커버리지) | | | 진단 4종 채택. dev A-0 이름은 유지하고 yj1 기능 커버리지는 **A-F**로 명명 |
| 데이터 | 청첩장 팔레트 두 벌(yj1 로즈 `#B84A6B` "사람 지정" vs dev 아이보리·레드 "가정") | | | **둘 다 LOCK 없음.** yj1의 "사람 지정 핑크"는 소스 `사람-원문`이지만 되묻기(probe) 없음 → M막에서 두 벌을 레퍼런스로 나란히 제시하고 되묻기로 결정 |

## 4. 실행 순서 (P0~P5) — 각 단계 끝에 검사기 ERROR 0 + 커밋

### P0. 준비 (30분)
- [x] fetch, 워크트리 체크아웃, 전 파일 읽기 (완료 — 이 문서)
- [ ] dev에 `merge/yj1` 브랜치 생성. **`git merge`를 바로 쓰지 않는다** — SKILL.md·README·templates가 양쪽에서 크게 바뀌어 텍스트 머지가 의미 없다. yj1 파일을 **경로별로 골라 가져오는(ours 전략 + 수동 이식)** 방식.

### P1. 코어 구조 재편 — SKILL.md 분할 (1시간)
- [ ] dev SKILL.md에서 방법론 본문을 `references/`로 이동: `stage-0-alignment.md`(dev 0단계 + yj1 §1~3,5 + 되묻기), `foundation-derivation.md`(yj1 §4 + dev 대비율 규칙), `reference-research.md`(yj1 그대로 + dev 갤러리 제시·되묻기 변형 cue), `stage-b-diverge.md`(yj1 + dev baseline 고정·B-1.5 시안 3개 메모), `figma-playbook.md`(2-7 합집합), `stage-a-structural.md`(dev A-0~A-6 + yj1 A-F 기능 커버리지 + 2-8 신규 2종 + 기준 오류 판정), `stage-c-aesthetic.md`(2-1 매핑), `stage-v-flow.md`(dev V 축소판), `process-acts.md`(O·M/W/I/U·LOCK·GATE), `snapshot-contract.md`.
- [ ] SKILL.md는 라우터·절대 규칙·게이트·진입 조건표(yj1 "순서가 아니라 함수다" 표 채택)·라우팅·상한만 남긴다. 목표 300줄 이하.
- [ ] 검사기 `CORE_FILES`에 `references/` 추가(도메인 누출 검사 범위 확장). yj1 references에 `cheongchup`·`청첩장` 언급이 있으면 lessons로 옮긴다.

### P2. 검증 체계 합병 (1시간)
- [ ] `design-verify/SKILL.md`를 가져와 **얇은 진입점**으로 고친다: 트리거("검증해줘") → `references/stage-a/c/v` 참조, 기준값은 `brief.md` YAML, 이력은 `decisions.md`. `criteria.md`·`verify-log.md` 언급 제거.
- [ ] `templates/decisions.md`에 yj1 verify-log의 두 표(화면별 C 시도 횟수 / 기준 정정 기록) 추가. 진단 열 값에 `결정충돌` 추가.
- [ ] `templates/contracts/requirements.json`에 yj1 criteria "기능 커버리지" 표의 열(요구 → 담당 프레임 → 상태 ✅/⚠️/❌, 유저스토리 역할별, 흐름 끊김 시작/중간/끝, 사용자 설정 지점, 역할 결정 지점)을 추가.
- [ ] 라우팅 표: 반복실패 > 결정충돌(→UNLOCK 요청) > 방향오류 > 국소결함.

### P3. 프로젝트 데이터 합병 — 청첩장 (1시간)
- [ ] yj1 `projects/cheongchup-scheduler/*` → `design/invitation-scheduler/runs/yj1/` 이동(내용 무수정, 헤더에 "yj1 run, 별도 Figma 파일, LOCK 없음" 추가). yj1 Figma 파일 키는 문서에 없다 → 사람에게 확인, `brief.md` target에 `runs.yj1.file_url`로 기록.
- [ ] yj1 `references.md`(캘링·언제볼까·모여봐요 반례 등)를 dev `brief.md` 레퍼런스 표에 **`봤는가=아니오`** 그대로 이식 — 구조 근거로만, 톤 근거 금지.
- [ ] yj1 verify-log 15건 중 **범용 교훈**을 `harness-lessons.md` L28~로 추가(이모지 아이콘, 앰버 vs 로즈 색가족, 아바타 전원 브랜드색, 기본 상태 라벨 노이즈, 상태 라벨 조어, 표기 기호 26곳, 검색 없는 100명 리스트, 온보딩 부재, 12px 일관 위반 → 기준 정정).
- [ ] dev 청첩장 GAP 등록: 온보딩 3화면 부재(2-9), 프로토타입 연결 0(V-3), 표기 기호(S06 "3/5" 등)·이모지 여부 재검. → I막 과제 T5 "처음 앱을 열었다" 추가.
- [ ] 팔레트 두 벌은 M막 레퍼런스로 등록(§3 데이터 충돌).

### P4. 진입 문서·설정 (30분)
- [ ] `CLAUDE.md` 가져오기 + dev 규칙 3줄 추가(O단계 없이 시작 금지 / LOCK 없이 뒤 막 금지 / 검증자 신규 컨텍스트). 구조 블록을 dev 경로로.
- [ ] `README.md`: dev 본문 유지 + yj1 "층 분리 규칙" 문단 이식.
- [ ] `.gitignore` 합집합. `docs/projects/*/project.json`에 `runs` 필드(선택) 추가.

### P5. 검증·리허설 (30분)
- [ ] `check_contracts.py` 전 프로젝트 ERROR 0. `references/` 도메인 누출 0.
- [ ] 청첩장 U 화면 1개(S06)에 신규 A 항목(기호·이모지·프로토타입 연결) 사실 계산 → 새 검사가 실제로 잡는지 확인.
- [ ] family-trip PRD로 `references/` 방법론만 읽고 M막 질문지가 생성되는지(도메인 값 없이) 확인.
- [ ] 머지 커밋 + `harness-lessons.md`에 "합병에서 배운 것" 1건.

## 5. 합병에서 버리는 것 (이유 함께)
- yj1 `projects/` 경로, `criteria.md`, `verify-log.md` **파일**(내용은 전부 흡수) — 원장 이원화 방지.
- yj1 SKILL.md의 "실제 클라이언트가 없는 세션에서는 근거 있는 가정으로 채운다" — dev 절대 규칙 1(판단기준 추측 금지)과 충돌. **가정은 사람이 명시적으로 위임한 경우에만**. 대신 yj1의 "PRD 원문의 상황 묘사를 반응 원문으로 취급"은 `사람-원문` 소스로 허용.
- yj1의 팔레트 값 자체 — 프로젝트 값이므로 코어에 들어가지 않는다(yj1도 같은 원칙).

## 6. 이 계획을 실행하기 전에 사람이 정할 것
1. 합병 브랜치 이름과 푸시 권한(현재 `HanEol-Lee77`은 push 불가).
2. yj1 run의 Figma 파일 URL(문서에 없음).
3. 팔레트 두 벌 중 M막에서 어떻게 다룰지(둘 다 레퍼런스로 제시 — 권고) 또는 하나를 사람 지정으로 확정할지.
4. `design-verify`를 별도 스킬로 남길지(권고: 얇은 진입점으로 유지) 아니면 삭제할지.
