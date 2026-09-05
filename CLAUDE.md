# harnessthon-2-team-4 — oss-design-harness

Figma-네이티브 디자인 하네스. "현업 디자이너의 판단 기준을 추출해, 에이전트에 최적화된 형태로 재구성"한다.
배경·경쟁 포지셔닝: [docs/concept.md](docs/concept.md). 전체 설명: [README.md](README.md).

## 불변 규칙

- 화면 제작 요청은 `oss-design-harness` 스킬을 거친다. 즉흥 제작 금지.
- 순서가 아니라 함수다 — 0(정렬)→B(발산수렴)→A/C(검증)를 기계적으로 순서대로 밟지 않는다. 각 단계는 "지금 이게 불확실한가"로 진입 여부를 판단한다.
- 산출물(`brief.md`, `decisions.md`, `criteria.md`, `build-plan.md`)은 `projects/<슬러그>/` 아래에 둔다. 스킬 폴더 안에 프로젝트별 값(색상, 화면 목록, 결정 결과)을 쓰지 않는다.
- C단계(미적 판단)는 반드시 스크린샷을 렌더해 실제로 보고 판단한다. 노드 속성 조회로 대체 금지.
- C단계 실패 시 원인 진단 없이 그냥 다시 만들지 않는다 — 국소결함/방향오류/반복실패 셋 중 하나로 분류하고 그에 맞게 라우팅한다.
- "이 정도면 됐다"는 최종 판단은 항상 사람이 내린다. 에이전트가 스스로 완료 선언하고 끝내지 않는다.
- Figma 조작은 `use_figma` 호출 전 반드시 `figma-use` 스킬(리소스: `resource:figma-use`)을 먼저 로드한다.

## 구조

```
CLAUDE.md
projects/<프로젝트슬러그>/brief.md      # 0단계 산출물 — 레퍼런스·역추출 기준·가정·토큰
projects/<프로젝트슬러그>/decisions.md  # B단계 산출물 — 축·후보·선택 근거
projects/<프로젝트슬러그>/criteria.md   # A/C단계 이 프로젝트의 합격선
projects/<프로젝트슬러그>/build-plan.md # 제작 순서·화면 목록
.claude/skills/oss-design-harness/       # 0→B→제작 오케스트레이터
.claude/skills/design-verify/            # A/C 검증 + 실패 라우팅
```

**층 분리**: 스킬의 `references/`는 방법(어떻게 판단하는가)만, `projects/<슬러그>/`는 값(이 프로젝트에서 얼마인가)만 담는다. 방법론 파일에 프로젝트 답을 쓰면 다음 프로젝트가 그대로 베낀다.
