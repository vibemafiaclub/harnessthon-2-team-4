<!--
B단계(발산·수렴) 산출물 템플릿. 산출물 루트로 복사해서 채운다.
빈 템플릿입니다 — 아래는 전부 TODO/형식 예시이며 실제 내용이 아닙니다.

★ 이 파일은 append 전용이다. 새 라운드는 아래에 덧붙이고, 이전 라운드를 덮어쓰지 않는다.
  구현할 때 Write로 파일 전체를 다시 쓰지 말고 Edit로 끝에 삽입한다.
  이전 라운드를 지우면 반복실패 판정 근거와 재시도 카운터가 동시에 사라진다.
★ 이 파일은 C단계 검증 Agent에게 주지 않는다 (제작 의도를 알면 자기변호를 한다).
-->

# Decisions

## 라운드 로그

> C-라우팅이 이 표를 읽는다. **"C 탈락 항목" 열을 라운드 간 비교해** 반복 실패를 판정한다.
> 라운드 수(N)와 하위 라운드 수(N.k)가 그대로 재시도 카운터다. 기본 상한 각 3.
> 비워 두면 무한루프 방지가 작동하지 않는다.

| 라운드 | 시작 사유 | baseline | C 탈락 항목 | 라우팅 판정 | 하위 라운드 최대 |
|---|---|---|---|---|---|
| 1 | 최초 발산(축 분기 불필요) | 웜 아이보리 캔버스 · 모바일 390 · 밀도 중간 · Noto Sans KR | (제작 후 기입) | (제작 후 기입) | 1.0 |

---

## 라운드 1

### 시작 사유

`최초 발산` — **축 분기 불필요 — 사유**: 사용자가 실시간으로 후보를 선택할 수 없는 자율 실행이며(지시 원문 "figma page에 구현해줘"), 사람이 고르지 않는 후보를 병렬 생성하면 선택 권한 규칙(B-4)을 지킬 수 없다. 대신 단일 방향을 baseline으로 명시하고 근거를 brief.md 가정 #A3에 남긴다. 사람이 후속 라운드에서 축을 열면 여기부터 재발산한다.

### 식별된 독립 축과 baseline

> 축을 나누지 않고 화면 전체를 통째로 비교하면, 상대가 무엇 때문에 골랐는지 뒤섞여 판단 근거가 안 남는다.
> **독립성 검사**: 한 축의 값을 바꿔도 다른 축이 따라 바뀌지 않아야 한다. 따라 바뀌면 한 축이다 — 합친다.
>
> ★ **baseline이 반드시 필요하다.** 비교 축 외의 축을 고정해 주지 않으면 각 후보 Agent가 임의로
>   고르고 그 순간 축이 오염된다. 눈가림은 앵커링을 막지만 미지정 축의 임의 선택은 막지 못한다.

| 축 | 이 라운드에서 비교하는가 | baseline 값 (비교 안 하는 축은 이 값으로 고정) |
|---|---|---|
| 비주얼 무드 | 아니오 | 웜 아이보리 캔버스(#F7F3EE) + 봉인도장 레드 액센트(#B8433A) + 측 구분색(신랑 블루/신부 로즈/양가 골드). 청첩장 종이를 연상시키되 핑크·하트 클리셰 회피 |
| 정보 밀도 | 아니오 | 중간 — 리스트 한 행 2줄(이름+메타), 카드 패딩 16, 한 화면에 1차 정보 3개 이하 |
| 내비게이션 구조 | 아니오 | 하단 탭 4개(홈·지인·모임·일정) + 게스트는 탭 없는 단일 웹 뷰 |

### 축별 후보·비평·선택

> 후보는 서로를 모르는 Agent가 병렬로 만든다(산출 형태 = 텍스트 스펙, Figma에 쓰지 않는다).
> 비평은 서로의 평가를 모르는 페르소나 Agent가 낸다. 후보를 만든 Agent가 그 후보를 비평하지 않는다.
> **선택은 사람이 한다** — 에이전트가 고르면 "사람의 안목 추출"이라는 목적이 여기서 무너진다.

#### 축: (분기 없음)

| 후보 | 스펙 요지 | 페르소나 A 비평 | 페르소나 B 비평 | 선택 |
|---|---|---|---|---|
| 1 | baseline 단일 방향 (위 표) | — | — | ✓ (사람 부재로 baseline 채택) |

**선택 이유 (사람이 적는다)**: (미기입 — 사람이 후속 확인)

**남은 트레이드오프**: 무드·밀도 대안을 비교하지 않았으므로 C단계 C-4/C-5 탈락 시 곧바로 방향 오류(B 회귀)로 판정할 근거가 부족하다 → 첫 탈락은 국소 결함 절차부터 밟는다.

### 제작 기록

| 항목 | 내용 |
|---|---|
| 대상 파일 | `ZVyw1SdDMqtHemggKOAbgd` (1차 제작본) — 사용자 지정 파일 `xMsSA6ndIWBXEANJ0Ycphf`에는 다른 에이전트가 동시에 같은 스크립트로 재현 중이어서 충돌 회피를 위해 화면 쓰기를 하지 않았다(토큰 값 갱신·원자 컴포넌트 크기 버그 수정만 적용). |
| 생성/수정한 노드 ID | 페이지: 00 README(0:1) 01 Foundations(2:2) 02 Components(2:3) 03 Screens(2:4). 변수 컬렉션 `Tokens` VariableCollectionId:2:5(38개). 아이콘 4:4~4:68(18). 컴포넌트 세트: Avatar 5:18 · Badge/Status 5:31 · Chip/Filter 5:36 · Tag/Side 5:43 · Tag/Group 5:48 · Button 6:14 · Form/Input 6:27 · Form/Toggle 6:32 · Form/Checkbox 6:37 · Response/Cell 6:47 · Calendar/Day 6:111 · Nav/TopBar 7:20 · Nav/TabBar 7:105 · Segment/Control 7:127 · Banner/Alert 7:151 · List/PersonRow 8:101 · Card/Meeting 8:102. 화면: S01 11:2 · S02 13:144 · S03 15:228 · S04 16:259 · S05 16:400 · S06 21:415 · S07 21:585 · S08 25:489 · S09 26:523 · S10 26:742 · S11 27:775. README 29:2 · Foundations 29:23 |
| 제작 전 스냅샷 | `.cache/nodes-before.json` (신규 파일, Page 1 children=0) |
| 제작 후 스냅샷 | `.cache/nodes-after.json` — Plugin API로 계산한 사실 파일(위반 목록·카운트·인벤토리). MCP 출력 20KB 제한으로 원본 트리 전체 대신 계산 결과를 저장 |
| 렌더 | `renders/r1-S01..S11.png`(C 1.0 입력, 토큰 조정 전) · `renders/r1.1-S01..S11.png`(A-0·데이터 정합 수정 후) |

### 검증 로그 — 하위 라운드

> 국소 수정 재검과 A단계 재검은 B단계를 거치지 않으므로 라운드가 늘지 않는다.
> **여기에 한 줄씩 추가해 하위 카운트를 올린다.** 이 표가 없으면 그 두 루프는 무한 반복 가능하다.
> 판정 원문을 요약하지 않는다 — 라우팅 1/2 구분이 C단계 서술에 전적으로 의존한다.

| 하위 | 무엇을 했는가 | A단계 판정 원문 | C단계 판정 원문 | 결과 |
|---|---|---|---|---|
| 1.0 | 최초 제작 (renders/r1-*.png, 토큰 조정 전 사실 계산) | **제작자 사전 계산(검증자 판정 아님)**: A-0 대비율 위반 61건 — 소프트 배경 위 12~13px 라벨(waiting #C98A1C on #FBEFD6 2.58, bride #C2607A on #F7E3E9 3.26, both 3.4, done 3.1, confirmed 4.21, danger 4.2, brand 4.35), tertiary #9C928A on white 3.05 ; A-0 넘침 1건 S10 status-tabs 5번째 칩(x 342~412) ; A-3 off-grid 3건(gap -10, -6, -6) ; A-1/A-2/A-5 위반 0 ; A-4 231/561=41.2% (<70%) | **C 검증 Agent(격리 컨텍스트) 판정 원문**: C-2a 흐름 PASS — "각 화면의 주 CTA 문구가 바로 다음 단계를 명시하고, S04→S05→S06의 대상(서연 대학 동기·후보 9/12·9/13·9/20)과 S07→S08→S10의 대상(도윤 직장 동료·9/14 19:30)이 화면 간 동일하게 이어진다" / C-2b 마무리 PASS — "11장 전체에서 미완성 플레이스홀더·잘린 텍스트·겹침·빈 박스·정렬 어긋남 없음 … S10 상단 필터 칩 우측 '다…' 절단은 가로 스크롤 칩 행의 관례적 잘림" / C-2c 측 구분 PASS — "신랑(도윤)=파랑, 신부(서연)=핑크, 양가=베이지/탠 3색 체계가 전 화면에서 유지됨 … S11 게스트 화면에서도 도(파랑)/서(핑크) 유지, 타 커플 민·현은 무채색" / C-5 맥락 적합 PASS — "웜 오프화이트 배경·벽돌색 프라이머리 단일 톤, 그라데이션·장식 일러스트·과한 카드 중첩 없음 … 범용 SaaS 대시보드 인상 없음" / C-6 까다로운 경우 PASS — ① 중복 소속 S02 서지민 행 태그 2개·S03 헬퍼·S04 파란 안내 박스+세그먼트+'중복 소속' 라벨 ② 늦은 회신·마감 S05 마감 칩·S06 'D-2', 미회신 회색 대시, 비활성 CTA·S07 '마감 지남' 배너+분기 버튼·S01·S10 ③ 겹침 S01 빨간 카드·S05 9/20 행 빨간 테두리·S09 '모임 2건'+빨간 박스+두 카드·S11 같은 날 경고 / C-1·C-3·C-4 SKIP(판단기준 미기재) / **종합: 통과**. 참고 관찰(판정 아님): "S07 상단 노란 박스는 미회신 2명을 '최민재, 한지훈'으로 명시하는데 … 1위 후보 카드에는 아바타 최·정·이·한이 가능 인원으로 표시되고, S08 … 최민재가 '확인함'으로 나온다" ; "S01 '다가오는 모임'에는 9/20 상견례(D-15)만 보이고 … 9/16 강태양 1:1(D-11)이 더 가까운 일정임에도 나오지 않는다" ; "S06 매트릭스가 다른 화면보다 촘촘하다" ; "S10은 '전체 7'인데 카드 3장 아래로 여백만 남고" | C 통과 · A는 제작자 사전 계산에서 A-0 FAIL 예상 → 1.1로 수정 |
| 1.1 | A-0 국소 수정: 토큰 8개 값 어둡게(대비율), S10 5번째 칩 제거→탭 행 2줄 wrap+'전체 7' 복원, gap -10/-6→-8 · C 참고 관찰 반영: S07 순위 카드 아바타→오·신·문·배, S08 구성원·확인 현황 이름 정합, S10 카드 아바타 정합, S01 카드→가장 가까운 확정 모임(강태양 1:1 9/16) · 렌더 r1.1 | (A 검증 Agent 판정 대기 — 아래 행에 원문 기입) | (재검 미실시 — C 1.0 통과 유지, 변경은 데이터 정합·색 명도만) | 대기 |
| 1.2 | A-4 국소 수정: 반복 패턴 4종 컴포넌트 승격(Layout/SectionHeader ×5, Card/StatusTile ×4, List/AckRow ×4, Action/ShareTile ×3) → 인스턴스 치환. 사실 파일 v1.2 재계산: A-0 대비율 위반 0(비활성 버튼 라벨 1건 면제 표기), 넘침 0, A-1/2/3/5 위반 0, A-4 232/517=**0.449** (<0.70) | **BLOCKED** — A 재검 Agent가 조직 월 한도(HTTP 429)로 중단, 판정 없음. 자동 재시도 안 함 | 미실시 | BLOCKED · 미해결 결정: "A-4 산식(REUSE-A)·하한 70% 재확인", "검증 Agent 재개(한도 리셋 후)" |

### 인수인계 GATE 블록

```yaml
stage: build-screens
mode: build
project_id: invitation-scheduler
run_id: 2026-09-05-r1
revision: "1.2"
producer: claude-master-session-d71411b8
target_ref: ZVyw1SdDMqtHemggKOAbgd / 03 Screens (2:4)
input_refs: [design/invitation-scheduler/brief.md, docs/screen-map.md, design/_system/brief.md]
output_refs: ["11:2","13:144","15:228","16:259","16:400","21:415","21:585","25:489","26:523","26:742","27:775", design/invitation-scheduler/.cache/nodes-after.json, design/invitation-scheduler/renders/r1.1-S01..S11.png]
status: PASS
blockers: ["제출본 파일 결정 (ZVyw… vs xMsSA…)"]
next_stage: verify-A
```

```yaml
stage: verify-A
mode: build
project_id: invitation-scheduler
run_id: 2026-09-05-r1
revision: "1.2"
producer: subagent-a-review-isolated-2
target_ref: ZVyw1SdDMqtHemggKOAbgd / 03 Screens (2:4)
input_refs: [design/invitation-scheduler/.cache/nodes-after.json, "design/invitation-scheduler/brief.md#A단계 기준값"]
output_refs: []
status: BLOCKED
blockers: ["검증 Agent 한도 중단(429) — 재개 조건: 한도 리셋", "A-4 산식·하한 재확인"]
next_stage: verify-A
```

```yaml
stage: verify-C
mode: build
project_id: invitation-scheduler
run_id: 2026-09-05-r1
revision: "1.0"
producer: subagent-c-review-isolated-1
target_ref: ZVyw1SdDMqtHemggKOAbgd / 03 Screens (2:4)
input_refs: [design/invitation-scheduler/renders/r1-S01..S11.png, "brief.md 판단기준 원장 확정 5행"]
output_refs: ["decisions.md 검증 로그 1.0 C 판정 원문"]
status: PASS
blockers: ["C-1/C-3/C-4 판단기준 승격 대기", "C-2c 색 구분 기준이 사람-해석으로 정정됨 → 승격 거부 시 재검"]
next_stage: verify-V
```

```yaml
stage: wireframe
mode: build
project_id: invitation-scheduler
run_id: 2026-09-05-r1
revision: "1.3"
producer: claude-master-session-9fdfb61b
target_ref: xMsSA6ndIWBXEANJ0Ycphf / W Wireframes (58:2)
input_refs: [docs/prd.md, docs/screen-map.md, "03 Screens S01~S11 (역추출)"]
output_refs: ["WF/* 컴포넌트 세트 7종 59:8 59:15 59:22 59:27 59:45 59:53 59:106", "W 화면 S01 60:2 · S02 60:51 · S03 60:118 · S04 60:163 · S05 61:118 · S06 61:234 · S07 61:287 · S08 61:321 · S09 62:186 · S10 62:313 · S11 62:379", "화면별 notes 텍스트 11개(인터뷰 질문 포함)", design/invitation-scheduler/interview.md]
status: PASS
blockers: ["3막 순서 뒤집힘 — W는 U(03 Screens)에서 역추출한 것이라 U와 1:1 대응은 보장되지만 W가 흐름의 원장이 되려면 인터뷰 후 W→U 방향으로 수정해야 함", "W는 xMsSA…에, 검증된 U는 ZVyw…에 있음 — 제출본 파일 결정 필요"]
next_stage: interview
```

### 오버라이드 로그 — 사람이 Agent 판정을 뒤집은 사건

> 각 행의 "이유 원문"에서 판정을 가른 기준을 증류해 brief.md 「판단기준 원장」에 후보로 보낸다.
> 승격은 사람만 한다. **완화 방향 자동 증류 금지** — 통과가 목적이 되는 순간 검증이 무너진다.

| 하위 | 항목 | Agent 판정 | 사람 판정 | 이유 원문 | 증류된 후보 |
|---|---|---|---|---|---|
| 1.0 | TODO (예: C-4) | TODO | TODO | "TODO — 들은 말 그대로" | TODO |

### 라운드 종결

- **최종 C 탈락 항목**: 없음 — 통과 (1.0, 확정 5행 기준)
- **최종 A 상태**: 1.2 BLOCKED (재검 Agent 한도 중단). 제작자 사전 계산으로는 A-4만 미달(0.449 < 0.70)
- **V단계**: 미실시
- **라우팅 판정**: 해당 없음 (C 통과) / A-4는 국소 결함 절차 2회째 → 3회째 전에 산식·하한 재확인 필요
- **미해결 결정**: ① 제출본 파일(ZVyw… / xMsSA…) ② A-4 산식(REUSE-A)·하한 70% 재확인 ③ C-1/C-3/C-4 승격 ④ C-2c "색으로 구분" 해석 승격 여부 ⑤ 검증 Agent 재개(한도)
- **다음 행동**: 사람이 ①~④ 결정 → improve 모드로 라운드 1 이어서(revision 1.3) A 재검 + V 실시

---

<!--
## 라운드 2

새 라운드는 위를 지우지 않고 여기에 라운드 1과 같은 형식으로 덧붙인다.
라운드 3이 C단계에서 탈락한 시점에 사람에게 에스컬레이션하고 멈춘다
(라운드 3을 "시작할 때"가 아니다 — 그러면 실질 상한이 2가 된다).
에이전트가 상한을 스스로 늘리지 않는다.
-->

## 인수인계 메모

> 드라이버 스위치 시 이어 쓴다. 별도 파일을 만들지 않는다.

| 시각 | 누가 → 누구로 | 어디까지 했는가 | 다음은 무엇인가 |
|---|---|---|---|
| 2026-09-05 | Claude(이 세션, master+worker 겸임) → 사용자 | target 파일을 xMsSA6ndIWBXEANJ0Ycphf로 확정 후 P1~P7 전체 제작 완료(토큰·아이콘18·컴포넌트17종·화면11개·README·Foundations), 스크린샷 육안 검증 및 3종 버그 수정(아이콘 왜곡·오토레이아웃 클리핑·세그먼트 컨트롤) 완료 | 독립 reviewer Agent A/C 정식 검증, A-4 계산방법론 확정, 제출(Figma 링크 공개 설정) |

## 라운드 1 미해결 결정 ① 해소 (2026-09-05, 이 세션)

**제출본 파일 결정**: `xMsSA6ndIWBXEANJ0Ycphf` (Designthon-Figma-1)로 확정. 사용자가 세션 중간에 이 URL을 직접 제시하며 "지금 피그마 …로 올라가고 있는 거 맞는지 확인"이라고 물었고, 실제로는 그때까지 `ZVyw1SdDMqtHemggKOAbgd`에 작업 중이었음을 확인 → 사용자가 "xMsSA…로 이사(Recommended)"를 선택. `ZVyw…`는 참고용 1차 제작본으로 남긴다(위 라운드 1 로그가 그 파일 기준 상세 검증 결과다).

`xMsSA6ndIWBXEANJ0Ycphf`에서의 진행 상태(이 세션 자체 계산, 독립 reviewer 미실시):
- P1~P7 전체 완료: 토큰 38개(색 26·간격 8·모서리 4)+텍스트스타일 9종, 아이콘 18개, 원자 컴포넌트 11종, 복합 컴포넌트 6종, 화면 11개(S01~S11), README+Foundations.
- A-0 자동기본명 0건 · A-1 팔레트 외 색상 0건 · A-3 4pt그리드(space/*만 사용) · A-5 네이밍 위반 0건 — 전부 자체 계산상 PASS.
- A-4 재사용률: 전체 노드(408) 대비 인스턴스(174) = **42.6%**, 기준 70% 미달. 단 `ZVyw…` 라운드 1.2 로그도 동일 이슈(0.449)를 보고했으므로, 두 파일 독립 제작에서 같은 결과가 나온 것 — 계산 산식 자체(분모에 레이아웃 컨테이너·텍스트 라벨 포함 여부)를 사람이 재확인해야 한다는 신호로 본다.
- C단계 육안 확인(독립 reviewer 미실시): C-2 흐름·측 색 구분, C-5 맥락 적합, C-6 까다로운 경우 3종(중복소속 S02/S04, 늦은회신 S05/S06/S07/S01, 겹침 S09/S01) 전부 화면에 실존.
- 스냅샷: `.cache/nodes-after-summary.json`(집계 통계, 원본 트리는 20KB 응답 한도로 미보존).

**다음 행동**: `ZVyw…`의 A-4 검증 Agent(429로 BLOCKED)와 동일하게, `xMsSA…`도 독립 reviewer Agent의 정식 A/C 검증을 아직 받지 않았다. 제출 전 (1) A-4 산식 사람 확정 (2) 독립 reviewer 브리핑 (3) Figma 파일 보기 권한 공개 설정이 남았다.
