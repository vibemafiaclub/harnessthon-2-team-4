---
name: wedding-scheduler-figma
description: 청첩장모임 스케줄러 PRD(docs/prd.md)를 Figma MCP(use_figma)로 구현할 때 쓰는 과제 전용 하네스. 범용 절차(oss-design-harness)의 게이트·A/C 검증 위에, 이 과제의 화면 지도·더미 데이터·제작 스크립트 규약·검증 브리프 템플릿을 고정한다. "청첩장 스케줄러 화면 만들어/이어서 만들어/검증해줘" 요청, 또는 design/invitation-scheduler/ 아래 산출물을 다룰 때 발동. oss-design-harness와 함께 쓴다(대체 아님).
---

# wedding-scheduler-figma — 과제 전용 제작·검증 하네스

**원칙**: 절차 원본은 `oss-design-harness/SKILL.md`(게이트·라우터·A/C 판정 규칙). 이 스킬은 그 절차의 **빈칸을 이 과제의 값으로 채운 것**이다. 충돌하면 원본이 우선한다.

## 0. 입력 문서 (읽는 순서)

1. `docs/prd.md` — 무엇을 해결하는가 (사람 소스)
2. `docs/screen-map.md` — 화면 11개·흐름·까다로운 경우 커버리지·더미 데이터
3. `design/_system/brief.md` — 토큰(변수·텍스트 스타일)·상태 어휘·네이밍 (실측 소스)
4. `design/invitation-scheduler/brief.md` — 원장·가정 로그·A/C 기준값
5. `design/invitation-scheduler/decisions.md` — 라운드·검증 로그 (append 전용)

## 1. 대상 Figma 파일 — 이 스킬은 값을 갖지 않는다

- 프로젝트 설정: `docs/projects/invitation-scheduler/project.json` (경로만).
- **target의 유일한 원장은 `design/invitation-scheduler/brief.md`의 `target` 블록이다.** 파일 키·페이지 ID·컬렉션 ID를 이 스킬에 적지 않는다 — 여기 적힌 상수가 원장과 어긋나 두 파일에 나뉘어 제작된 사고가 있었다(`decisions.md` 라운드 1 제작 기록).
- 세션 시작 시 `python scripts/harness/check_contracts.py invitation-scheduler`를 돌려 target 불일치·기준값 TODO·도메인 누출을 확인한다. ERROR가 있으면 Figma 쓰기를 시작하지 않는다.
- 페이지 구조는 `_system/brief.md` target 블록(`00 README` / `01 Foundations` / `02 Components` / `03 Screens`)을 따른다. 페이지 ID는 세션마다 `figma.root.children`로 읽는다.
- 다른 파일 URL이 주어지면 `brief.md` target을 먼저 바꾸고 가정 #A1을 갱신한 뒤, 이전 파일을 `backup:`으로 남기고 "제출본 파일 결정"을 미해결 결정으로 적는다.

## 1.5 프로세스 상태 — 이 프로젝트는 3막 중 어디에 있나 (2026-09-05)

코어의 4막(M 무드 → W 와이어프레임 → I 기능 인터뷰 → U UI 상세)이 도입되기 **전에** U(하이파이)를 먼저 만들었다. 그래서 순서가 뒤집혀 있고 **LOCK은 하나도 없다** — 현재 U의 무드(아이보리·봉인 레드)와 UX는 전부 미확정 가정이다.

| 막 | 상태 | 해야 할 것 |
|---|---|---|
| M | 없음 | 레퍼런스 1개씩 HTML 갤러리로 보여 주고 반응 원문 + 되묻기 2~3회 → 무드 어휘 잠금(LOCK-M). 현재 U의 아이보리·레드는 에이전트 가정이므로 레퍼런스 중 하나로만 제시 |
| W | Figma W 있음(역추출, 2026-09-05) · HTML 로우파이 없음 · LOCK-W 없음 | HTML 로우파이는 Figma W에서 역생성해 `design/invitation-scheduler/wireframes-html/`에 두고 클라이언트 컨펌 → 되묻기 → LOCK-W |
| I | interview.md 준비됨(대상·과제·사전 정정 2건), 미실시 | `interview.md`(양식 `templates/interview.md`) — 대상: 예비부부 1 + 초대받는 지인 1. 실제 인터뷰가 어려우면 시뮬레이션 Agent로 대체하고 명시. 기존 `사람-해석` 행("색으로 구분")의 승격/기각을 여기서 받는다 |
| U | 있음 (A BLOCKED·C PASS·V 미실시) | I막 결과로 요구 계약이 바뀌면 U를 고친다. 바뀌지 않으면 A 재검·V 실시로 마무리 |

## 2. 제작 절차 P1~P7 (worker — U막)

| 단계 | 하는 일 | 완료 확인 |
|---|---|---|
| P1 토큰 | 변수 `color/*`(26) `space/*`(8) `radius/*`(4) + 텍스트 스타일 9종 | `getLocalVariablesAsync().length ≥ 38`, 스타일 9 |
| P2 아이콘 | `Icon/<name>` 24×24 컴포넌트, stroke를 `color/text/primary`에 바인딩 | 18개 |
| P3 원자 컴포넌트 | `Avatar` `Badge/Status` `Chip/Filter` `Tag/Side` `Tag/Group` `Button` `Form/Input` `Form/Toggle` `Response/Cell` `Calendar/Day` | 배리언트 속성값 = 상태 어휘 |
| P4 복합 컴포넌트 | `Nav/TopBar` `Nav/TabBar` `List/PersonRow` `Card/Meeting` `Banner/Alert` `Segment/Control` | 인스턴스 중첩 사용 |
| P5 화면 | `S01`~`S11` 390×844, 좌→우 흐름 순서, 각 프레임 아래 `"<화면명> · notes"` 텍스트(FRAME에는 `description`이 없다) | `docs/screen-map.md` §3 커버리지 빈칸 0 · 화면마다 content 높이 ≤ 프레임 높이 검사 |
| P6 README·Foundations | 00 페이지에 데이터 모델·상태 어휘·읽는 법 텍스트, 01 페이지에 토큰 스와치 | 에이전트가 README만 읽고 이어서 작업 가능 |
| P7 스냅샷 | `.cache/nodes-after.json` (아래 §4 스크립트) → master에 보고 | 파일 존재, 노드 수 기록 |

### 2.1 `use_figma` 스크립트 공통 헬퍼 (모든 제작 호출 첫머리에 붙인다)

```js
const page = await figma.getNodeByIdAsync("<PAGE_ID>"); await figma.setCurrentPageAsync(page);
for (const st of ["Regular","Medium","Bold"]) await figma.loadFontAsync({family:"Noto Sans KR", style: st});
const vars={}; for (const v of await figma.variables.getLocalVariablesAsync()) vars[v.name]=v;
const ts={};   for (const s of await figma.getLocalTextStylesAsync()) ts[s.name]=s;
const paint=(name,o)=>{let p=figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',vars[name]); if(o!==undefined) p={...p,opacity:o}; return p;};
const txt=async(chars,style,color,name)=>{const t=figma.createText(); t.name=name||'label'; await t.setTextStyleIdAsync(ts[style].id); t.characters=chars; t.fills=[paint(color||'color/text/primary')]; return t;};
const bind=(n,prop,v)=>n.setBoundVariable(prop, vars[v]);
const padXY=(n,x,y)=>{bind(n,'paddingLeft',x);bind(n,'paddingRight',x);bind(n,'paddingTop',y);bind(n,'paddingBottom',y);};
const radius=(n,v)=>{for(const p of ['topLeftRadius','topRightRadius','bottomLeftRadius','bottomRightRadius']) bind(n,p,v);};
```

규약:
- **색은 `paint()`로만** 넣는다(변수 바인딩). 하드코딩 `{r,g,b}` 금지. 예외는 `brief.md` `tokens.color.exceptions`만.
- **텍스트는 `txt()`로만** 만든다(텍스트 스타일 참조). `fontSize` 직접 설정 금지.
- 간격·패딩·모서리는 `bind()`/`padXY()`/`radius()`로 변수에 바인딩. 4의 배수가 아닌 값 금지.
- 컨테이너는 전부 오토레이아웃(`createAutoLayout` 또는 `layoutMode` 설정). 절대 배치는 캘린더 점·오버레이만.
- 레이어 이름은 영문 kebab-case 역할명. 컴포넌트 인스턴스 이름은 그대로 둔다.
- 한 호출에서 화면 1개(또는 컴포넌트 세트 2~3개)까지. 호출마다 `return { createdNodeIds }`.
- 화면 프레임: `S<nn> <한글명>`, 390×844, `clipsContent=true`, fill `color/bg/canvas`, 내부는 `header / content / tab-bar` 3분할 오토레이아웃.
- 화면 `description` 형식: `목적: … / 진입: … / 다음: … / 까다로운 경우: …`

### 2.2 더미 데이터
`docs/screen-map.md` §4만 쓴다. 실명·실연락처·실주소 금지. 날짜는 결혼식 2026-11-21, 오늘 2026-09-05 기준.

## 3. 검증 브리프 템플릿 (master → reviewer)

reviewer는 **신규 컨텍스트 Agent**로 띄운다(fork 금지). 아래 문장 그대로 보낸다. `decisions.md`·제작 의도·대화 이력은 넣지 않는다.

### 3.1 A단계 브리프

```
당신은 Figma 노드 스냅샷만 보고 구조적 사실을 판정하는 검증자다. 수정하지 않고 판정만 낸다.
읽을 파일은 아래 두 개뿐이다. 그 외 파일 탐색(Glob/Grep/다른 Read)을 하지 마라.
 1) <절대경로>/design/invitation-scheduler/.cache/nodes-after.json
 2) <절대경로>/design/invitation-scheduler/brief.md 의 「A단계 기준값」 YAML 블록만
항목 A-0(대비율·누락 리소스·자동 기본명·프레임 이탈), A-1 색, A-2 타이포 스타일 참조, A-3 4pt 그리드,
A-4 재사용률(기준값 TODO면 SKIP), A-5 네이밍, A-6 배리언트 필수 상태를 PASS/FAIL/SKIP/N/A로 답하라.
FAIL은 위반 노드 경로(id·name)와 실제 값을 전부 나열한다. 기준값이 TODO/비어 있으면 SKIP(기준값 없음)이라 쓴다.
A-0은 기준값과 무관하게 항상 판정한다. 출력은 항목별 표 + 종합 판정(통과/조건부 통과/불통과).
```

### 3.2 C단계 브리프

```
당신은 화면 스크린샷만 보고 미적·게슈탈트 품질을 판정하는 검증자다. 제작 의도를 모른다. 수정하지 않는다.
읽을 파일은 아래 PNG들뿐이다. 그 외 파일 탐색을 하지 마라.
 <절대경로>/design/invitation-scheduler/renders/r1-S01.png … r1-S11.png
판단기준(확정 행만):
 - C-2 흐름 "지인 풀 → 모임 편성 → 일정 조율 → 확정"이 화면 순서로 읽히는가
 - C-2 시각적 디테일로 마무리됐는가 — 플레이스홀더·잘린 텍스트·겹친 요소가 보이면 FAIL
 - C-2 신랑/신부/양가가 항상 색으로 구분되는가
 - C-5 익숙한 UI 패턴을 청첩장·예비부부·양가 맥락에 맞게 다듬었는가 — 범용 대시보드 템플릿처럼 보이면 FAIL
 - C-6 중복 소속 / 늦은 회신·마감 / 겹치는 모임 3가지가 실제 UI로 보이는가 (각각 어느 화면 어디인지 적어라)
 C-1(색온도) C-3(여백 리듬) C-4(밀도)는 기준 미승격 → SKIP(판단기준 미기재)라고 쓴다.
A단계 요약: <항목별 PASS/SKIP만>.
각 항목을 PASS / FAIL(무엇이 어떻게 보이는지 + 스크린샷 파일명과 위치) / SKIP으로 답하라. "개선 여지" 같은 중립 표현 금지.
```

## 4. 스냅샷 스크립트 (P7·A단계 입력)

```js
// use_figma — 03 Screens + 02 Components를 한 번에 덤프. 인스턴스 내부는 depth 제한으로 제외.
const dump=(n,depth)=>{const o={id:n.id,name:n.name,type:n.type};
 if('fills' in n && Array.isArray(n.fills)) o.fills=n.fills.map(f=>f.type==='SOLID'?{hex:'#'+[f.color.r,f.color.g,f.color.b].map(c=>Math.round(c*255).toString(16).padStart(2,'0')).join('').toUpperCase(),bound:!!(f.boundVariables&&f.boundVariables.color)}:{type:f.type});
 if('strokes' in n && n.strokes.length) o.strokes=n.strokes.map(f=>f.type==='SOLID'?{hex:'#'+[f.color.r,f.color.g,f.color.b].map(c=>Math.round(c*255).toString(16).padStart(2,'0')).join('').toUpperCase()}:{type:f.type});
 if(n.type==='TEXT'){o.textStyleId=n.textStyleId;o.fontSize=n.fontSize;o.chars=n.characters.slice(0,40);}
 if('layoutMode' in n && n.layoutMode!=='NONE'){o.layout={mode:n.layoutMode,gap:n.itemSpacing,pt:n.paddingTop,pr:n.paddingRight,pb:n.paddingBottom,pl:n.paddingLeft};}
 o.box={x:Math.round(n.x),y:Math.round(n.y),w:Math.round(n.width),h:Math.round(n.height)};
 if(n.type==='INSTANCE'){o.mainComponent=n.mainComponent&&n.mainComponent.name;return o;}
 if(n.type==='COMPONENT_SET'){o.variants=n.children.map(c=>c.name);}
 if('children' in n && depth<12) o.children=n.children.map(c=>dump(c,depth+1));
 return o;};
const page=await figma.getNodeByIdAsync("2:4"); await figma.setCurrentPageAsync(page);
return page.children.map(c=>dump(c,0));
```
결과를 `.cache/nodes-after.json`에 저장한다. 컴포넌트 페이지는 별도 호출로 `.cache/components-after.json`.

## 5. 이 과제의 완료 게이트 (제출 전 체크)

- [ ] `docs/screen-map.md` §3 커버리지 표 빈칸 0 — 각 셀이 가리키는 UI가 실제 프레임에 존재
- [ ] S01~S11 프레임 전부 존재, 이름 규약 준수, `description` 기입
- [ ] A단계: A-0 FAIL 0 · A-1/2/3/5/6 FAIL 0 (A-4는 사람 입력 전까지 SKIP 허용)
- [ ] C단계: 확정 행 5개 FAIL 0 · 후보 행은 SKIP으로 기록(사람 승격 대기)
- [ ] `decisions.md` 검증 로그에 판정 원문, `brief.md` 검증 방식 기록 채움
- [ ] README 페이지에 파일 읽는 법·상태 어휘·데이터 모델이 있어 **다른 에이전트가 이어서 작업 가능**
- [ ] 사람에게 남길 미해결 결정 이름: `A-4 재사용률 하한`, `C-1/C-3/C-4 판단기준 승격`, `target 파일 위치(A1)`
