<!--
A/C단계 검증 기준값 — 이 프로젝트 전용.
references/ 의 stage-a-structural.md, stage-c-aesthetic.md 는 "무엇을 어떻게 판단하는가"(방법)만 담고,
"이 프로젝트에서 그 값이 얼마인가"는 전부 이 파일에 있다. 방법론 파일에 프로젝트 값을 쓰지 않는다.
전제: brief.md의 토큰 값, decisions.md의 축 선택.
-->

# 검증 기준값 — 청첩장모임 스케줄러

## A단계 기준값 (구조적 사실)

| 체크 카테고리 | 이 프로젝트의 값 |
|---|---|
| 허용 컬러 | `brief.md`의 토큰 9종(Background/Surface/Text-Primary/Text-Secondary/Accent/Success/Warning/Neutral/Muted). 그 외 바인딩 안 된 SOLID fill이 있으면 실패 |
| 타이포 스타일 | Title 20/SemiBold, Body 15/Regular, Caption 13/Regular, Label 12/Medium — 이 4종 외 자유 조합 발견 시 실패. 폰트는 Inter(Pretendard 미탑재로 대체, `brief.md` 참고) |
| Spacing 그리드 | **8px**. 아이콘–텍스트 최소 간격 4px만 예외 허용 |
| 반복 요소 | 모임 카드, 지인 리스트 아이템, 상태 배지, 아바타 — 인스턴스 비율 **≥ 90%** |
| 레이어 네이밍 | `[역할]` 또는 `[역할]/[상태]` (예: `모임카드`, `모임카드/확정앞둠`, `상태배지/대기중`, `하단탭바`) |
| Variant 커버리지 | 상태 배지 4변형(대기중/확정앞둠/확정됨/완료) 전부 존재. 모임 카드는 최소 빈 상태(empty) 변형 존재 |

### 조회 스니펫 (이 프로젝트 노드 이름 기준)

```js
// 컴포넌트 재사용률 + 네이밍 컨벤션 위반 탐지
const frame = figma.currentPage.findOne(n => n.name === "홈");
const all = frame.findAll(() => true);
const badNames = all.filter(n => /^(Frame|Rectangle|Group|Ellipse) \d+$/.test(n.name)).map(n => n.name);
const cardLike = frame.findAllWithCriteria({ types: ["INSTANCE", "FRAME"] })
  .filter(n => n.name.includes("모임카드"));
const instanceRatio = cardLike.filter(n => n.type === "INSTANCE").length / (cardLike.length || 1);
return { badNames, instanceRatio };
```

## C단계 기준값 (미적 판단)

| 판단 항목 | 이 프로젝트의 합격선 |
|---|---|
| 색온도·조명 일관성 | 상태 배지 4색(대기중=중립회색 `#B8B2AA`, 확정앞둠=주황 `#C98A3A`, 확정됨=녹색 `#5B8A6B`, 완료=연회색 `#D9D4CC`)이 서로 다른 채도 "느낌"으로 보이면 실패. 확정앞둠 주황이 유독 쨍하면 팔레트 이탈 |
| 시각적 위계 | 홈 화면 기준 — **회신 마감 임박 모임이 스크롤 없이 상단에서 즉시 눈에 띄어야 함**(PRD §3). 2초 보고 못 찾으면 실패 |
| 여백 리듬 | 카드 내부 패딩 16 vs 카드 사이 간격 **12는 실패 / 24는 통과** |
| 정보 밀도 | 카드당 시선 정지점 **3개까지**(모임명·참석자 요약·상태배지). B단계에서 저밀도 축을 선택했으므로 그 이상이면 실패 |
| 클리셰 | 경조사 맥락 — 화려한 파스텔 그라디언트, 하트 이모지 남발도 이 프로젝트에서는 클리셰로 간주(`brief.md` 톤 참고) |
| 엣지케이스 | 빈 상태(아직 모임 없음)에 안내 문구 + 행동 버튼이 함께 있어야 통과. "데이터 없음" 텍스트 하나면 실패 |

<!--
TODO(디자이너): 위 6항목 중 합격선이 숫자/구체 예시로 그어진 것은 "여백 리듬"과 "정보 밀도"뿐이다.
나머지 4개도 같은 밀도로 — "어디부터 실패인지" 선을 그어야 에이전트가 판단할 수 있다.
-->
