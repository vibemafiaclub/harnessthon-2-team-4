# AGENTS.md — 이 레포에서 일하는 모든 코딩 에이전트의 공통 계약

> Codex CLI(worker)·Claude Code(master/cso/reviewer) 공용. Claude Code는 `.claude/skills/oss-design-harness/SKILL.md`를 스킬로 자동 로드하지만, Codex는 이 파일이 진입점이다. **먼저 이 파일 → 그다음 SKILL.md 전문을 읽고 시작한다.**

## 1. 우리가 만드는 것

- 과제: `docs/prd.md` — 예비부부 두 사람이 함께 쓰는 **청첩장모임 스케줄러**. 지인 풀 관리 → 모임 편성 → 일정 후보·회신 수합 → 확정·공유 → 전체 일정 조망 → 진행 상태 구분.
- 산출물: **Figma 파일**(Figma MCP로 직접 제작). 코드(HTML/React)로 UI를 만드는 과제가 아니다.
- 평가 기준: ① 흐름이 끊김 없이 이어지는가 + 까다로운 경우(중복 소속·늦은 회신·겹치는 모임)를 화면 어딘가에서 다뤘는가 ② 심미적 완성도 ③ **"AI 에이전트가 읽고 이어서 작업할 수 있는 데이터로서의 디자인"** — 네이밍·오토레이아웃·컴포넌트·변수가 곧 점수다.

## 2. 하네스 — 반드시 SKILL.md의 게이트·라우터를 따른다

`.claude/skills/oss-design-harness/SKILL.md`가 유일한 절차 원본이다. 요약이 아니라 그 파일을 읽는다. 핵심만 적는다.

| 단계 | 하는 일 | 산출물 |
|---|---|---|
| 게이트 G-1~G-4 | 산출물 루트 고정 · 템플릿 복사 · 대상 Figma 파일 확정 · Figma MCP 스모크 | — |
| 0 요구사항 정렬 | 레퍼런스 1개씩 보여주고 반응 원문 수집 → 5축 대비 질문 → 후보 증류 → **사람이 승격** | `brief.md`(원장) |
| B 발산·수렴 | 독립 축 2~4개 + baseline 고정 → 후보를 **텍스트 스펙**으로 병렬 생성 → 페르소나 교차 비평 → **사람이 선택** | `decisions.md` |
| 제작 | 선택된 후보만 Figma에 만든다. 제작 전·후 노드 스냅샷 저장 | Figma 프레임 + `.cache/nodes-*.json` |
| A 구조 검증 | 별도 검증 노드가 노드 속성만으로 PASS/FAIL/SKIP/N/A. A-0 하한선은 SKIP 불가 | `decisions.md` 검증 로그 |
| C 미적 검증 | 별도 검증 노드가 **스크린샷을 보고** 판정. 제작 의도·decisions.md는 주지 않는다 | `decisions.md` + 오버라이드 로그 |

**절대 규칙 (SKILL.md 절대 규칙 1~5의 요약 — 원문이 우선)**
1. `TODO`는 세 종류다. **판단기준·기준값 TODO는 추측해서 채우지 않는다** — 사람에게 묻고 멈춘다. 절차 TODO는 기본 절차로 진행한다. 산출물 TODO는 각 단계가 채운다.
2. 최종 "됐다" 판단·축별 후보 선택·판단기준 승격은 **항상 사람**이 한다.
3. 확정 안 된 정보는 `brief.md` 가정 로그에 명시한다. 침묵 금지.
4. **검증하는 노드 ≠ 만든 노드.** worker가 만들면 reviewer가 검증한다. 같은 세션의 "이제 검증자 관점으로"는 격리가 아니다.
5. 멈출 때는 미해결 결정의 **이름**을 남긴다 ("C-1 색온도 기준 미확정 — 디자이너 확인 필요").

## 3. 팀 배선 (cys 멀티에이전트) — 누가 무엇을 하나

| 역할 | 에이전트/모델 | 담당 | 주소 |
|---|---|---|---|
| master(부마스터) | Claude Code · **Fable 5.1** | 오너 창구, 작업 분해·브리프, 게이트 판정, 최종 승인 | `cys send --to master` |
| cso | Claude Code · Fable 5.1 (Figma 플러그인 상속) | 원장 인터뷰 진행자(0단계), 가정 로그·수렴 판정표 관리, 진행 감시 | `--to cso` |
| **worker (main)** | **Codex CLI · gpt-6-astra (high)** + Figma MCP | B단계 후보 스펙 취합, **제작단계 실행(Figma 쓰기)**, A/C FAIL 수정 | `--to worker` |
| reviewer-claude-1 | Claude Code · Fable 5.1 (Figma 플러그인 상속) | **A·C 검증 전담**. 고치지 않고 판정만. 제작 의도를 받지 않는다 | `--to reviewer-claude-1` |

- 보고·요청은 `cys send --to <역할> "<메시지>"` + `cys send-key --to <역할> Return`. 화면 폴링 금지.
- worker는 **자기 결과를 자기가 통과시키지 않는다.** 제작 완료 → master에 "제작 완료 · 스냅샷 경로 · 대상 프레임 노드 ID"만 보고 → master가 reviewer에 A/C 검증 브리프(SKILL.md 「검증 Agent 배선」 준수: 절대경로만, 탐색 금지, decisions.md 미제공).
- 후보 병렬 생성(B-2)은 Claude Code 노드가 서브에이전트(신규 컨텍스트, fork 금지)로 띄운다. Codex worker는 후보를 **생성하지 않고** 선택된 후보를 만든다.

## 4. Figma MCP 사용 규약

- 서버: `https://mcp.figma.com/mcp` (Codex: `codex mcp list`에 `figma` OAuth · Claude: `figma@claude-plugins-official` 플러그인). 실측 기록과 폴백은 `docs/figma-mcp.md`.
- 읽기: `get_metadata` → 노드 트리(스냅샷용) · `get_design_context` · `get_variable_defs` · `get_screenshot`(C단계 렌더).
- 쓰기: `use_figma`(노드 생성·속성 설정) · `generate_figma_design` · `create_new_file` · `upload_assets`(아이콘·이미지).
- **대상은 반드시 `brief.md`의 `target`에 적힌 파일·페이지·프레임만.** 업무 파일·타인 파일 쓰기 금지. 후보 Agent는 Figma에 쓰지 않는다.
- rate limit(429)에 걸리면 재시도하지 말고 master에 보고한다. 노드 트리 조회는 단계당 **1회**만(SKILL.md A단계 입력 전달).
- 인증 만료는 에이전트가 못 푼다 — 사람에게 `codex mcp login figma` / Claude `/mcp`를 요청한다.

## 5. 경로 규약

- 산출물 루트(G-1): `design/<화면-슬러그>/` — 예 `design/friend-pool/`, `design/gathering-compose/`, `design/schedule-poll/`, `design/overview-calendar/`. 세션 내 고정.
- 각 루트: `brief.md`, `decisions.md`, `.cache/nodes-before.json`, `.cache/nodes-after.json`, `renders/r<N>.png`.
- 앱 전체 공통 원장(디자인 토큰·네이밍·상태 어휘): `design/_system/brief.md` — 화면별 원장은 여기의 토큰을 **실측 소스로 인용**한다(화면마다 새로 증류하지 않는다).
- 화면 인벤토리·까다로운 경우 커버리지: `docs/screen-map.md`. 팀 운영: `docs/team-playbook.md`.
- 비밀·토큰은 커밋하지 않는다(`.gitignore`). `.cache/`·`renders/`도 커밋하지 않는다.

## 6. 보고 형식 (worker → master)

```
[worker 보고] <단계> <화면-슬러그>
결과: 완료 | 차단 | 부분
대상: <file_url> / <page> / <frame 노드ID>
산출: <절대경로 목록>
미해결 결정: <이름> (없으면 "없음")
다음: <내가 기다리는 것>
```
