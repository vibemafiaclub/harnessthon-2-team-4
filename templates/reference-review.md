# 레퍼런스 조사·검수·추출 계약

프로젝트 산출물 루트에 복사한다. 아래는 형식이며 실제 선택·승인을 뜻하지 않는다. REF는 화면/상태 단위로 발급하고, 같은 앱의 다른 화면은 별도 REF로 연결한다.

## 조사 범위

- 프로젝트 / 조사 질문 / 열린 갭: TODO
- 비교할 사용자 과업 / 범위 밖 과업: TODO
- 수집자 / 독립 검수자 / 검수 격리 수준: TODO
- 앱 전체가 아닌 이번에 검토하는 화면·상태: TODO

## REF-001 — 증거 카드

```yaml
reference_id: REF-001
product_identity:
  name: null
  developer: null
  app_id: null
source_url: null
accessed_at: null
platform: null
version: null                  # 확인되지 않으면 null
task: null
screen_state: null
evidence:
  - id: E-001
    kind: null                 # official-description | store-image | live-screen | live-flow
    original_url: null
    local_path: null
    region: null               # 전체 화면 내 위치. 잘라낸 화면이면 원본도 연결
    observation: null
    limitation: null
claims:
  - id: CLAIM-001
    text: null
    evidence_ids: []
    review: UNVERIFIED         # SUPPORTED | CONTRADICTED | UNVERIFIED
review:
  collector: null
  reviewer: null               # collector와 다름
  isolation: null
  status: not-reviewed         # not-reviewed | reviewed | blocked
  report_path: null
  unresolved: []
recommendation:
  decision: null               # adopt | hold | exclude; 에이전트 제안
  reason: null
human_decision:
  decision: pending            # pending | adopt | hold | exclude
  actor: null
  decided_at: null
  reaction_verbatim: null
  reason_verbatim: null
  scope: null                  # 특정 요소·과업만 지정
  revisit_when: null
patterns: []
```

## 사람 반응 — 한 레퍼런스씩 진행

| 항목 | 반응 원문 | 연결 ID |
|---|---|---|
| 자유 반응 | TODO | REF-001 |
| 표면 룩앤랭귀지: 가져올 것/피할 것 | TODO | |
| 워크플로·구조 | TODO | |
| 인터랙션 품질 | TODO | |
| 원하는 결과 | TODO | |
| 거부할 가정 | TODO | |

## PATTERN-001 — 추출 카드

| 필드 | 내용 |
|---|---|
| 출처 REF / 증거 ID / 사람 선택 기록 | TODO |
| 관찰한 구체 요소 | TODO |
| 왜 도움이 될지 — 검증 전 가설 | TODO |
| 적용할 과업 / 화면 / 조건 | TODO |
| 적용 방식 | TODO |
| 가져오지 않을 요소와 이유 | TODO |
| 정상·빈·로딩·실패·복구 상태 | TODO |
| 충돌하는 다른 패턴 / 해결할 결정 | TODO |
| 판단기준 후보 / C태그 또는 흐름 검증 | TODO |
| 사람의 기준 승격 원문 / 상태 | 후보 — 미승격 |
| 적용 후 화면·컴포넌트 노드 ID | 제작 후 기록 |
| 검증 결과·근거 | 검증 후 기록 |

## 인수인계 검토

- [ ] 사용하는 주장은 근거가 있고 독립 검수 기록이 있다.
- [ ] 소개문·홍보 이미지·실행 화면·실행 흐름의 증거 범위를 구별했다.
- [ ] 사람의 채택/보류/제외와 에이전트 추천을 구별했다.
- [ ] 채택 범위에만 추출 패턴을 연결했다.
- [ ] 새 기준을 확정으로 사용할 경우 사람의 승격 기록이 있다.
- [ ] 원본 이미지에서 알 수 없는 수치·동작을 지어내지 않았다.
- [ ] 보류·제외 이유와 재검토 조건을 보존했다.

체크 미충족이면 해당 항목의 미해결 결정 이름을 적는다. 체크리스트 자체가 독립 검수 결과나 사람 승인을 대신하지 않는다.

## 변경 이력 — 추가 전용

| 일시 | REF/PATTERN | 이전 상태 | 새 상태 | 변경 주체 | 근거·반응 원문 |
|---|---|---|---|---|---|
| TODO | | | | | |
