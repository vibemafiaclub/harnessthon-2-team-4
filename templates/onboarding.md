<!--
O단계(온보딩) 산출물 템플릿. design/<project-id>/onboarding.md 로 복사해서 채운다. 빈 템플릿 — 전부 TODO.
원칙: 질문지가 아니라 재진술. 에이전트가 레포·Figma·설정에서 읽을 수 있는 것을 먼저 채우고(소스=실측),
사람에게는 "틀린 줄 번호"만 받는다. 판단기준·기준값은 여기서 확정하지 않는다(원장의 몫).
-->

# Onboarding — <project-id>

## O-1 역할표 (누가 결정하나)

| 역할 | 권한 | 누가(역할명, 실명 대신) | 연락·컨펌 채널 | 응답 대기 상한 |
|---|---|---|---|---|
| 클라이언트 | 막 컨펌·LOCK, UNLOCK 승인 | TODO | TODO | TODO |
| 디자이너 | 판단기준 승격/기각, 레퍼런스 채택 | TODO | TODO | TODO |
| 오너 | 제출본·target 파일 결정, 상한 변경 | TODO | TODO | TODO |
| 드라이버(에이전트 세션) | 제작·기록. 판정·승격·선택 권한 없음 | TODO (세션 ID) | — | — |

## O-2 프로젝트 설정

- project.json: `docs/projects/<id>/project.json` — 검사기 결과: TODO (`python scripts/harness/check_contracts.py <id>`)
- PRD: TODO (경로, 크기, 마지막 수정)
- 인터뷰 대상 유형: TODO / 인터뷰 스킬: TODO (경로 A/B/C)

## O-3 모드와 시작 막 — 기존 산출물 상태표

| 막 | 기존 산출물 | 위치 | LOCK 유무 | 이번 세션에서 할 일 |
|---|---|---|---|---|
| M 무드 | TODO (없음 / 있음: 레퍼런스 n개) | TODO | 없음 | TODO |
| W 와이어프레임 | TODO (HTML / Figma) | TODO | 없음 | TODO |
| I 인터뷰 | TODO | TODO | 없음 | TODO |
| U UI | TODO (화면 n개, A/C/V 상태) | TODO | 없음 | TODO |

모드: TODO (plan-only / build / review / improve) · 시작 막: TODO

## O-4 대상 파일

- Figma URL: TODO (사람 제공 / 에이전트 생성 — 생성이면 첫 보고에 URL 제시, 가정 로그 "높음")
- 같은 파일에 쓰는 다른 세션: TODO (없음 / 있음 → 소유자)

## O-5 도구 실측

| 도구 | 상태 | 비고 |
|---|---|---|
| Figma MCP 읽기 / 속성 / 렌더 / 쓰기 / 변수 | TODO | `docs/figma-mcp.md` 표 |
| 인터뷰 스킬 MCP | TODO (A/B/C) | `docs/integrations/<skill>.md` |
| 한도·인증 | TODO | 429 시 자동 재시도 금지 |

## O-6 입력 자산 인벤토리 (있는 것만 `실측`, 없으면 "없음")

| 자산 | 있음/없음 | 위치 | 소스 |
|---|---|---|---|
| 레퍼런스·무드 보드 | TODO | | |
| 브랜드 가이드·기존 토큰 | TODO | | |
| 기존 화면(Figma/HTML) | TODO | | |
| 더미 데이터 규칙(실명 금지)·기준일 | TODO | | |

## O-7 작업 약속

- 라운드 상한: 3 (변경 시 오너 승인) · 하위 라운드 상한: 3
- 검증 격리 수준: TODO (프롬프트 지시만 / 도구 제한 / 별도 디렉터리)
- 커밋·푸시: TODO (브랜치, 시점)
- 보고 형식: `AGENTS.md` §6

## O-8 재진술 (사람이 "맞다 / 틀린 줄 번호"로 답한다)

1. 이 프로젝트는 TODO 를 만든다. 결정자는 TODO 다.
2. 모드는 TODO 이고 TODO 막에서 시작한다. 기존 산출물 TODO 는 LOCK 없는 가정이다.
3. 대상 Figma 파일은 TODO 이며 쓰는 세션은 이 세션 하나다.
4. 인터뷰는 TODO 스킬로, 대상 TODO 유형 각 1명 이상.
5. 판단기준 값은 원장에서 사람이 채운다. 에이전트는 채우지 않는다.
6. 라운드 상한 3, 429 자동 재시도 없음, 검증은 신규 컨텍스트 Agent.
7. 커밋은 TODO 브랜치에 TODO 시점.

**승인 원문**: "TODO" — 누가 / 언제 → GATE `stage: onboarding` PASS

## 인수인계 (드라이버 교체 시 한 줄 추가, O-3·O-5만 재확인)

| 시각 | 누가 → 누구로 | 재확인한 것 | 변경 |
|---|---|---|---|
| TODO | | | |
