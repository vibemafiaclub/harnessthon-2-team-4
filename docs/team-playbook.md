# Team Playbook — FM-Harness(Figma MCP 하네스) 팀 운영

> 하네스톤 2회차 · 팀 4 · 2026-09-05. 이 문서는 **팀(사람 + 에이전트 노드)이 어떻게 움직이는지**를 적는다. 디자인 절차 자체는 `.claude/skills/oss-design-harness/SKILL.md`가 원본이고, 에이전트 공통 계약은 `AGENTS.md`다.

## 1. 편성

cys 멀티에이전트 터미널의 한 부서(dept-2)를 FM-Harness 팀으로 쓴다. 작업 폴더는 이 레포 루트다.

| 노드 | CLI · 모델 | 설정 원천 | 역할 |
|---|---|---|---|
| master(부마스터) | Claude Code · Fable 5.1 | `~/.claude` (Figma 플러그인 인증 완료) | 오너 창구. 게이트 G-1~G-4 판정, 단계 라우팅, 브리프 작성, 검증 결과로 승인/재위임 |
| cso | Claude Code · Fable 5.1 | `~/.claude` 상속(`claude-figma` 어댑터) | 0단계 원장 인터뷰어. 수렴 판정표·가정 로그 관리. 스톨 감지 |
| worker (main) | **Codex CLI · gpt-6-astra · reasoning high** | `~/.codex/config.toml` + `codex mcp` figma(OAuth) | 제작단계 실행자. 선택된 후보를 Figma에 만든다. A/C FAIL 수정 |
| reviewer-claude-1 | Claude Code · Fable 5.1 | `~/.claude` 상속 | A·C 검증 전담. 판정만, 수정 없음, 제작 의도 미수신 |

기동 명령(부서 소켓 안에서):
```
cys launch-agent --role cso               --agent claude-figma --cwd C:\Users\deepnoid\gpters24\harnessthon-2-team-4
cys launch-agent --role worker            --agent codex        --cwd C:\Users\deepnoid\gpters24\harnessthon-2-team-4
cys launch-agent --role reviewer-claude-1 --agent claude-figma --cwd C:\Users\deepnoid\gpters24\harnessthon-2-team-4
```
`claude-figma` 어댑터는 `~/.cys/pack-dept-dept-2/agents.json`에 정의되어 있다 — 부서 격리 설정 대신 사용자 `~/.claude`를 쓰는 이유는 **Figma 플러그인(MCP OAuth)이 거기에만 있기 때문**이다.

## 2. 왜 이렇게 나눴나

- **판단과 구현의 분리**: master/cso(Claude)는 묻고·정리하고·판정한다. worker(Codex)는 만든다. 모델을 다르게 둔 것은 벤더 다양성이 아니라 역할 경계를 물리적으로 만들기 위해서다 — 같은 세션이 만들고 검증하면 SKILL.md 절대 규칙 4가 무너진다.
- **검증자 무지가 검증력**: reviewer는 `decisions.md`·제작 의도·대화 이력을 받지 않는다. 스크린샷 절대경로와 `brief.md` 확정 행만 받는다. 실사용자도 의도를 모르고 화면을 보기 때문이다.
- **Figma 쓰기 주체는 하나**: worker만 Figma에 쓴다. 후보 생성 Agent들이 각자 쓰면 rate limit·네이밍 충돌·정체불명 프레임이 남는다(SKILL.md B-2).

## 3. 한 화면의 라이프사이클 (누가 → 누구에게)

```
오너 ──요청──▶ master ──G-1~G-4──▶ (미통과: 오너에게 요청·정지)
master ──"0단계 시작, 슬러그 X"──▶ cso ──레퍼런스 1개씩·5축 질문──▶ 오너(디자이너)
cso ──후보 증류──▶ 오너 승격/기각 ──▶ brief.md 확정 행
master ──B-1 축·baseline 확정──▶ 서브에이전트 병렬 후보(텍스트 스펙) ──▶ 페르소나 비평 ──▶ 오너 선택 ──▶ decisions.md
master ──제작 브리프(brief.md + 선택 후보 + 요소 목록)──▶ worker ──Figma 제작·스냅샷──▶ master
master ──A 검증 브리프(nodes-after.json 절대경로 + 기준값)──▶ reviewer ──PASS/FAIL/SKIP/N/A──▶ master
  FAIL ▶ worker 수정 ▶ reviewer 재검(새 컨텍스트)
master ──C 검증 브리프(renders/rN.png 절대경로 + 확정 행 + A 요약)──▶ reviewer ──판정+원인──▶ master ──▶ 오너 최종 판정
  오버라이드 ▶ decisions.md 오버라이드 로그 ▶ brief.md 후보 ▶ 오너 승격 ▶ 다음 라운드 기준
```

## 4. 이 과제에 특화한 운영 결정

1. **앱 전체 공통 원장 먼저**: `design/_system/brief.md`에서 토큰(색·타이포·spacing·네이밍·상태 어휘)을 먼저 확정한다. 화면별 원장은 이것을 실측 소스로 인용한다. Greenfield라 "실측"의 원천은 우리가 첫 화면에서 만든 Figma 변수·스타일이다 — 첫 화면(추천: 전체 일정 조망) 제작 후 `get_variable_defs`로 실측해 `_system`에 역기입한다.
2. **화면 순서는 `docs/screen-map.md`의 의존 순서**를 따른다. 지인 풀 → 모임 편성 → 일정 후보·회신 → 확정 공유 → 전체 조망 → 초대받은 지인 응답 화면.
3. **까다로운 경우 3종은 화면에 반드시 자리를 가진다**(평가 기준): 중복 소속 / 늦은 회신·마감 / 겹치는 모임. `screen-map.md` 커버리지 표의 빈 칸이 0이어야 제출 가능.
4. **"데이터로서의 디자인"**: 제출 전 A-0(자동 생성 기본명 0건)·A-5(네이밍 컨벤션)·오토레이아웃 사용·컴포넌트/변수 바인딩을 reviewer가 전 화면에 일괄 검증한다. 이 항목이 곧 채점 대상이다.
5. **두 사람이 함께 쓴다**: 모든 화면에 "누구 쪽(신랑/신부/공동)"이 데이터로 존재해야 한다. 개인용 일정앱처럼 보이면 B단계로 회귀한다.
6. **더미 데이터**: 실명·실연락처 금지. `docs/screen-map.md` §4의 더미 세트를 쓴다.

## 5. 제출 체크리스트

- [ ] Figma 파일 링크(보기 권한 공개) — 디스코드 제출 채널
- [ ] 사용한 모델·에이전트 명기: Claude Code Fable 5.1 (master/cso/reviewer) · Codex CLI gpt-6-astra (worker) · Figma MCP(`mcp.figma.com`)
- [ ] `design/*/brief.md`·`decisions.md` 커밋(토큰·비밀 없음 확인)
- [ ] `docs/screen-map.md` 커버리지 표 빈 칸 0
- [ ] reviewer 최종 A-0 전 화면 PASS 기록

## 6. 장애 시

| 증상 | 대응 |
|---|---|
| Figma MCP 401/인증 만료 | 사람이 `codex mcp login figma`(worker) / Claude `/mcp`(reviewer·cso). 에이전트는 멈추고 요청만 |
| 429 rate limit | 조회 횟수 줄이기(단계당 1회 스냅샷). 재시도 루프 금지 |
| 노드 기동 시 지침이 PowerShell에 흘러들어감 | `C-c` 두 번 → CLI 수동 기동 → `cys reinject --role <role>` |
| 검증자가 파일을 스스로 탐색 | 브리프에 "지정 절대경로 외 탐색 금지" 누락 — 브리프 재작성 후 새 컨텍스트로 재검 |
| 전 항목 SKIP | 통과가 아니다. 기준 없는 항목 이름(C-n)을 나열해 오너에게 요청 |
