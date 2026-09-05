# oss-design-harness

**현업 디자이너의 판단 기준(안목)을 추출해, 에이전트에 최적화된 형태로 재구성하는 Figma-네이티브 디자인 하네스.**

VIBE MAFIA CLUB 하네스톤 2회차(2026-09-05)를 계기로 이너서클 코파운더들과 함께 만드는 오픈소스 프로젝트입니다.
지향점: `ui-ux-pro-max` 급, 현업에서 쓸 수 있는 수준의 skill.

## 이 레포의 상태 (2026-09-05)

두 층이 함께 있습니다. 구분해서 읽으세요.

- **코어(범용 절차)** — `.claude/skills/oss-design-harness/SKILL.md`, `templates/`, `scripts/harness/`. 게이트·모드·0/B/제작/A/C/V 단계·GATE 인수인계·라우팅·상한이 채워져 있습니다. **판단기준 값은 여전히 비어 있습니다(TODO)** — 그것은 프로젝트 원장에서 사람이 채웁니다. 코어에는 특정 프로젝트의 화면명·상태·색이 들어가면 안 되고, `scripts/harness/check_contracts.py`가 검사합니다.
- **프로젝트(과제 산출물)** — `docs/projects/<id>/project.json`이 진입점입니다.
  - `invitation-scheduler` 청첩장모임 스케줄러: `docs/prd.md` → `docs/screen-map.md` → `design/invitation-scheduler/`(원장·결정·검증 로그) → Figma 파일(원장 `brief.md` target 참조). 하네스톤 2회차 팀4 과제.
  - `family-trip` 가족 여행 관리 앱: **두 번째 도메인(리허설, plan-only)**. `docs/projects/family-trip/`에 fixture PRD·도메인 메모·설정. target·무드가 확정되면 build. 코어가 도메인을 바꿔도 그대로 굴러가는지 확인하는 용도입니다.
  - `docs/backlog/saju/` 사주 풀이: **보류**(사용자 결정 2026-09-05, 가족 여행으로 대체). 재개 시 `docs/projects/saju/`로 옮기면 검사기 대상에 들어갑니다.
- 배운 것은 `docs/harness-lessons.md`에, 다음 개선 계획은 `docs/PLAN-design-harness.md`에 있습니다.

## 프레임워크 — 4단계 판단 구조

디자이너가 일하는 **순서**를 그대로 흉내내지 않습니다. 사람이 순서대로 일하는 이유의 상당수는 사람의 기억력·주의력 한계를 우회하는 것이지, 결과가 좋아지는 진짜 원인이 아닙니다. 대신 각 단계가 실제로 하려던 일(**판단 기준**)만 뽑아서, 에이전트가 잘하는 방식(병렬 생성, 다각도 교차 비평)으로 다시 구현합니다.

| 단계 | 시점 | 하는 일 |
|---|---|---|
| **0. 요구사항 정렬** | 화면을 만들기 **전** | 뭘 만들지 자체가 불확실할 때, 레퍼런스/시나리오를 보여주고 반응(좋다/싫다+이유)을 받아 암묵적 판단기준을 뽑아낸다. 라벨형 질문("모던한 게 좋으세요?") 금지. |
| **B. 발산·수렴** | 만드는 도중, 정답이 여러 개일 때 | 독립적인 축(무드/밀도/난이도 등)을 먼저 나누고, 축마다 후보를 병렬 생성해 비교·수렴한다. |
| **A. 구조적 사실 검증** | 다 만든 후 | 데이터로 예/아니오 확인 가능한 것 (spacing, 컴포넌트 재사용, 네이밍, variant 존재 여부). |
| **C. 미적·게슈탈트 판단** | 다 만든 후 | 스크린샷을 렌더해서 실제로 봐야만 아는 것 (색온도 일관성, 위계, 여백 리듬, 클리셰 여부, 엣지케이스 완성도). |

C단계에서 탈락하면 원인에 따라 세 갈래로 라우팅한다 — ① 국소 결함(그 속성만 고쳐 C 재검) ② 방향 자체가 틀림(B로 회귀) ③ 반복 실패(0으로 에스컬레이션). 재시도 상한을 두고, 최종 판단은 항상 사람이 내린다.

자세한 배경·논리 검증 과정은 킥오프 자료(`docs/concept.md`) 참고.

## 구조

```
.claude/skills/oss-design-harness/SKILL.md   # 라우터 — 절대 규칙·모드·게이트·라우팅·상한
.claude/skills/oss-design-harness/references/ # 방법론 13파일 (dev + feat/yj1 + iceberg 합병) — 프로젝트 값 없음
.claude/skills/design-verify/SKILL.md         # "검증해줘" 얇은 진입점
.claude/skills/wedding-scheduler-figma/       # 청첩장 과제 래퍼 (값 없음, project.json·원장 참조)
templates/brief.md                            # 원장 양식 (소스 5종, A 기준값 YAML, 검증 방식 기록)
templates/decisions.md                        # append 전용 라운드·검증 로그·GATE 블록
templates/contracts/                          # gate.yaml, requirements.json, components.json 양식
templates/onboarding.md · interview.md        # O단계 온보딩 · I막 인터뷰 양식
docs/integrations/ooo-interview.md            # Ouroboros ooo interview 어댑터(개념 매핑·실행 경로)
scripts/harness/check_contracts.py            # target 단일 원장·기준값 TODO·도메인 누출·GATE 검사
docs/projects/<id>/project.json               # 프로젝트 진입점 (경로만, target 복제 금지)
docs/harness-lessons.md                       # 재현된 실패 → 범용 규칙 → 반영 위치
docs/PLAN-design-harness.md                   # 다음 단계(P1~P3) 계획
docs/PLAN-merge-feat-yj1.md                   # feat/yj1 하네스 합병 계획(시너지·충돌·P0~P5)
docs/concept.md                               # 컨셉 스펙 전문
AGENTS.md / docs/team-playbook.md / docs/figma-mcp.md   # 에이전트 계약·팀 운영·MCP 실측
```

### 층 분리 규칙 (feat/yj1에서 이식)

`references/`는 **"무엇을 어떻게 판단하는가"(방법)**만 담고, `design/<id>/`는 **"이 프로젝트에서 그 값이 얼마인가"**를 담는다. 방법론 파일에 특정 프로젝트의 답(색상 값, 화면 목록, 결정 결과)을 쓰면 다음 프로젝트가 그 답을 그대로 베낀다 — 검사기가 `domain_terms`로 잡는다.

## 사용법

1. `docs/projects/<id>/project.json`을 만들거나 고른다(PRD·원장 경로). `python scripts/harness/check_contracts.py <id>`로 ERROR 0을 확인한다.
2. 이 레포를 루트로 Claude Code를 실행하고 `oss-design-harness` 스킬이 발동하게 한다. 모드(plan-only / build / review / improve)를 정한다.
3. O단계 온보딩(`templates/onboarding.md`, 재진술 승인) → 게이트 G-1~G-4 → M 무드 → W 와이어프레임(HTML→Figma) → I 인터뷰(ooo interview) → 0단계(원장) → B(또는 스킵 사유) → 제작-L/S → A → C → V → 사람 최종 판단. 단계마다 `decisions.md`에 GATE 블록을 append 한다.
4. 판단기준 `TODO`는 사람이 채운다. 에이전트가 채우면 그 순간 검증이 무너진다.
5. 새 도메인은 project.json·PRD·원장·`_system`을 새로 만들고 코어는 그대로 쓴다.

## 라이선스

MIT — [LICENSE](./LICENSE)
