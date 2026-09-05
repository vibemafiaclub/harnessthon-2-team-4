# ooo interview 어댑터 — 하네스 M/W/I막의 인터뷰 진행 스킬

> 대상: [Ouroboros](https://github.com/Q00/ouroboros) `ooo interview` (로컬 클론 `C:\Users\deepnoid\gpters24\ouroboros`, 실측 버전 0.51.14, 2026-09-05).
> 역할: 우리 하네스는 **무엇을 묻고 무엇을 잠글지**(M/W/I막, LOCK, 되묻기)를 정하고, ooo interview는 **질문 생성·상태 지속·모호성 원장**을 맡는다. ooo는 요구를 발명하지 않는다 — 사람 승격 규칙은 그대로다.

## 1. 실행 경로

| 경로 | 조건 | 호출 |
|---|---|---|
| A. MCP | Claude Code에 Ouroboros MCP가 연결됨 (`/mcp`에서 확인, 툴 이름 예: `mcp__plugin_ouroboros_ouroboros__ouroboros_interview` — 실측 후 기록) | 매 호출 직전 `ToolSearch "+ouroboros interview"`로 스키마 재로드 → `ouroboros_interview` |
| B. CLI | MCP 미연결 | `ooo interview "<topic>"` 를 사용자가 `!` 접두로 실행. 트랜스크립트를 `interview.md`에 원문으로 옮긴다 |
| C. 폴백 | ooo 사용 불가 | SKILL.md 되묻기 규칙 + 0-2 루프를 수동으로 진행. `interview.md` 머리에 "폴백"이라고 적는다 |

2026-09-05 실측: MCP 서버는 `ooo mcp info`에 정상 등록되어 있으나 이 Claude 세션에서는 미연결(`ToolSearch` 결과 없음). 설정은 `~/.claude.json`에 있음 → 세션 재시작 후 재확인.

## 2. 개념 매핑 — ooo ↔ 하네스

| ooo interview | 하네스 | 비고 |
|---|---|---|
| `references: [{reference_id, label, origin, url?, excerpt?}]` | M막 레퍼런스 cue (`templates/reference-review.md`의 REF ID) | ooo는 URL을 **읽지 않는다**(cue로만 저장). 이미지 갤러리는 우리가 따로 보여 준다 |
| 레퍼런스 대비 질문(자동 생성): "surface look and language / workflow or structure / interaction qualities / desired outcome / assumptions we should reject" | **0-2의 5축 대비 질문과 동일** | ooo가 첫 답 이후 한 cue당 1개 결정론적으로 낸다 → 우리는 그 답을 원장 섹션 4·5·6·7에 꽂는다 |
| `RequirementCandidate.content_source`: `user_stated` / `reference_derived` / `model_inferred` / `repo_observed` | 소스 5종: `사람-원문` / (레퍼런스 반응 → `사람-원문`, 그 해석은 `사람-해석`) / `사람-해석` / `실측` | ooo도 "사용자 확인이 content source를 바꾸지 않는다"고 명시 — 우리 규칙과 같다 |
| `resolution`: `confirmed` / `needs_confirmation` / `unknown` / `conflicting` | 상태: 확정 / 후보 / 미기입 / 충돌 | `conflicting`은 우리 「충돌」 — 지어내지 않고 사람에게 |
| `refine_answer` 게이트(자유서술 답을 구조화해 **확인 후** 전달) | 되묻기 규칙 probe-1 ("왜?") | ooo의 refine이 첫 되묻기를 맡는다. probe-2/3(유사 변형)은 우리가 `references`에 변형 cue를 추가해 낸다 |
| 모호성 원장(ambiguity ledger, 메인 세션에 상시 표시) | `brief.md` 수렴 판정표 | 둘을 따로 두지 않는다 — ooo 원장 항목을 판정표 행에 매핑해 기록 |
| `restate_goal` 게이트(목표 재진술 → 명시적 승인) | **LOCK-<막>** | 막 종료 시 ooo restate 승인 발화 원문을 LOCK `evidence_verbatim`에 넣는다 |
| `seed-ready` | 하네스에서는 **쓰지 않는다** | 우리는 Seed를 만들지 않는다. seed-ready는 "닫힘 감사 허가"로만 읽고, 다음 막 진입은 LOCK로 판단 |
| `lateral_review_recommended` → `ouroboros_lateral_think`(researcher/contrarian/simplifier) | B-3 교차 비평 페르소나 | 인터뷰 중간에는 참고만. 판정 기준으로 승격하지 않는다 |
| `ui_ux_basics` 용어 팩(`confused_terms`) | 클라이언트가 용어를 모를 때만 | 요구 소스가 아니다(ooo 문서도 동일하게 명시) |
| `[from-code]` / `[from-user]` / `[from-research]` 접두 | `실측` / `사람-원문` / 외부 조사(원장에는 `가정` 또는 REF 근거) | Figma 파일 실측이 우리의 `[from-code]` |

## 3. 막별 사용법

### M막 (무드)
1. `ouroboros_interview(initial_context="<프로젝트> 시각 언어 정렬 — 무드 어휘만 다룬다. 구조·기능은 다루지 않는다", references=[REF-01 …])` — 레퍼런스는 **한 번에 하나**만 넣고, 우리가 HTML 갤러리로 같은 레퍼런스를 보여 준다.
2. ooo가 낸 5축 대비 질문에 클라이언트가 답한다(원문 기록). ooo `refine_answer`로 구조화 확인 = probe-1.
3. 답에서 나온 단어(예: "따뜻", "라운드")로 **유사 변형 cue 2~3개**를 `references`에 추가해 다음 턴을 이어 간다 = probe-2/3. 반응이 꺾이는 지점을 원장에 적는다.
4. restate 게이트 승인 원문 → `LOCK-M`. 토큰 값은 잠그지 않는다(어휘·채택 레퍼런스만).

### W막 (와이어프레임)
- HTML 로우파이 링크를 `references`의 `origin: "wireframe-html"` cue로 넣고, 대비 질문의 "workflow or structure" 축 답만 취한다. surface 축 답이 나오면 원문만 기록하고 "W에서는 다루지 않는다"고 되돌린다.
- 컨펌 원문 → `LOCK-W`.

### I막 (기능 인터뷰)
- `initial_context`에 시나리오 과제(`interview.md` T1~T4)를 하나씩 넣는다. ooo 질문은 "이 화면에서 다음에 무엇을 하겠나"류의 체험 질문으로 유지되도록, 라벨 질문이 나오면 우리가 parent-question 경로(`meta.ask_user_directly`)에서 바꿔 묻는다.
- `conflicting`·`unknown` 후보는 `GAP-F/GAP-X`로 증류. LOCK-W와 충돌하면 UNLOCK 요청.
- restate 승인 → `LOCK-I`.

## 4. 금지·주의
- ooo의 자동 기본값(safe auto assumption)은 **auto 모드 기능**이다. 우리 인터뷰에서는 쓰지 않는다 — 에이전트가 기본값으로 닫는 것은 절대 규칙 1 위반.
- ooo `seed-ready`를 "인터뷰 완료"로 보고하지 않는다. LOCK 블록이 없으면 미완료.
- 라운드 상한: ooo 세션 재시작으로 우리 라운드 카운터가 초기화되지 않는다(`decisions.md`가 원장).
- 시뮬레이션 인터뷰(페르소나 Agent가 답변)에 ooo를 써도 된다. 단 `interview.md`에 "시뮬레이션"을 명시하고 LOCK 근거로 쓰지 않는다.

## 5. 기록
- `interview.md` 머리: `진행 스킬: ooo interview 0.51.14 / 경로 A|B|C / ooo session_id`
- ooo 트랜스크립트는 원문 그대로 `interview.md` 워크스루 표에. 요약 금지.
