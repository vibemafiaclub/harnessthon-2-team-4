# harnessthon-2-team-4 — oss-design-harness

Figma-네이티브 디자인 하네스. "현업 디자이너의 판단 기준을 추출해, 에이전트에 최적화된 형태로 재구성"한다.
배경: [docs/concept.md](docs/concept.md) · 전체 설명: [README.md](README.md) · 다중 에이전트 계약: [AGENTS.md](AGENTS.md)

## 불변 규칙

- 화면 제작·검수 요청은 `oss-design-harness` 스킬(검수만이면 `design-verify`)을 거친다. 즉흥 제작 금지.
- **온보딩(O단계) 없이 시작하지 않는다.** 누가 결정하는지·모드·시작 막·대상 파일·도구 실측을 `onboarding.md` 재진술로 확인한다.
- 순서가 아니라 함수다 — 0/B/A/C는 "지금 이게 불확실한가"로 진입한다. 단, **4막(M 무드 → W 와이어프레임 → I 인터뷰 → U UI)은 순서이고 막마다 LOCK**이다. 잠긴 항목은 UNLOCK 요청으로만 바꾼다.
- 클라이언트 첫 반응은 라벨이다. 유사 변형 2~3개로 되묻기 전에는 승격하지 않는다.
- 산출물은 `design/<project-id>/`(원장·결정·인터뷰·온보딩·계약), 설정은 `docs/projects/<id>/project.json`. 스킬·`templates/`·`references/`에 프로젝트 값(색·화면명·인명·상태값)을 쓰지 않는다 — `python scripts/harness/check_contracts.py`가 검사한다.
- C단계는 반드시 스크린샷을 렌더해 본다. 노드 속성으로 대체 금지. Critic·Advocate는 각각 신규 컨텍스트 Agent.
- 검증하는 에이전트 ≠ 만든 에이전트. 같은 세션의 "검증자 관점"은 격리가 아니다.
- 실패는 반복실패 > 결정충돌 > 방향오류 > 국소결함 순으로 진단한 뒤 라우팅한다. 진단 없이 다시 만들지 않는다.
- 좋은 디자인 = 규칙·구조(①) AND 심미적 안정성(②) AND 핵심경험 서포트(③). ③은 요구 계약 추적성으로만 검증되며 근거 없으면 `검증 불가`=FAIL.
- "이 정도면 됐다"는 항상 사람이 낸다. 429·한도는 자동 재시도하지 않고 BLOCKED로 기록한다.
- `use_figma` 전에 `figma-use` 스킬을 로드한다.

## 구조

```
.claude/skills/oss-design-harness/SKILL.md      # 라우터 — 절대 규칙·모드·게이트·라우팅·상한
.claude/skills/oss-design-harness/references/   # 방법론 (프로젝트 무관): process-acts, stage-0/b/a/c/v, verify-routing,
                                                 #   foundation-derivation, reference-research, figma-playbook,
                                                 #   design-principle, forbidden-patterns, platform-hig-ios
.claude/skills/design-verify/SKILL.md           # "검증해줘" 얇은 진입점 — 같은 references를 읽는다
.claude/skills/wedding-scheduler-figma/         # 과제 래퍼 (값 없음)
templates/                                       # brief·decisions·interview·onboarding·reference-review·contracts/
scripts/harness/check_contracts.py              # target 단일 원장·기준값 TODO·도메인 누출·GATE 검사
docs/projects/<id>/project.json                  # 프로젝트 진입점 (경로만)
design/<id>/                                     # brief·decisions·interview·onboarding·contracts·runs/
docs/integrations/ooo-interview.md               # 인터뷰 스킬 어댑터
docs/harness-lessons.md                          # 실패 → 규칙 → 반영 위치
```

**층 분리**: `references/`는 방법(어떻게 판단하는가)만, `design/<id>/`는 값(이 프로젝트에서 얼마인가)만. 방법론 파일에 프로젝트 답을 쓰면 다음 프로젝트가 베낀다.
