> **합병 노트(2026-09-05)**: 이 파일은 `dev`(운영 뼈대)와 `feat/yj1`(판정 디테일), iceberg-1234 하네스(3축 원칙·추적성·정량 미학)를 합친 것이다. 출처를 각 절 머리에 적었다. 프로젝트 값(색·화면명·인명)은 여기 없다 — `docs/projects/<id>/`와 `design/<id>/`에 있다.

> 출처: iceberg-1234 `rules/apple-hig-enforced.md`. **project.json `platform: ios`일 때만** 적용하는 선택 규칙이다. 적용 시 A단계에 HIG 7~15(터치 44pt·최소 11pt·대비·Safe Area·Dark·Nav·색 외 구분·Pressed/Focused 배리언트)를 추가한다. 웹·안드로이드 프로젝트는 읽지 않는다.

# Apple HIG 강제 규칙 (iOS/iPadOS)

**출처**: `apple-hig-ios-design-guide.md` + Apple Human Interface Guidelines

대상 플랫폼이 iOS/iPadOS일 때, 하네스의 **모든 단계**에서 아래 규칙은 예외 없이 강제된다. 위반 시 해당 단계를 통과할 수 없다.

---

## HIG-COLOR: 색상 규칙
- **색상만으로 정보를 전달하지 않는다.** 모양, 아이콘, 텍스트 레이블을 반드시 병행한다. (WCAG + Apple "Differentiate Without Color")
- **텍스트와 배경 간 충분한 대비율을 확보한다.** 본문 텍스트 최소 4.5:1, 대형 텍스트(18pt+ 또는 14pt Bold+) 최소 3:1. (WCAG AA)
- **Dark Mode를 반드시 지원한다.** 모든 컬러 토큰은 Light/Dark 쌍으로 정의한다.
- **iOS 26 Liquid Glass 시대**: 브랜드 컬러는 콘텐츠 영역에 배치하고, UI 레이어는 표준 컴포넌트를 사용한다. 색상은 액션·상태·피드백을 나타내는 명확한 목적으로만 사용한다.

## HIG-TYPO: 타이포그래피 규칙
- **최소 텍스트 크기: 11pt.** 이보다 작은 텍스트는 어떤 경우에도 허용하지 않는다.
- **Dynamic Type을 지원한다.** 커스텀 폰트 사용 시에도 사용자 설정 텍스트 크기에 반응해야 한다.
- **Optical Sizes**: 텍스트 크기에 따라 tracking(자간)과 leading(행간)을 동적으로 조정한다.
- **줄 간격**: 텍스트 겹침 방지를 위해 충분한 행간을 확보한다.

## HIG-LAYOUT: 레이아웃 규칙
- **Layout Margins**: Compact width 16pt, Regular width 20pt.
- **Safe Areas를 반드시 존중한다.** Navigation bars, toolbars, tab bars, 홈 인디케이터 영역을 침범하지 않는다.
- **주요 콘텐츠는 줌이나 가로 스크롤 없이 표시한다.**
- **Auto Layout 필수**: 다양한 디바이스 크기와 방향에 자동 대응하는 레이아웃을 구성한다.

## HIG-TOUCH: 터치 타겟 규칙
- **모든 인터랙티브 요소의 최소 터치 타겟: 44pt x 44pt.**
- **요소 간 충분한 간격**: 인접한 터치 타겟이 겹치지 않도록 최소 8pt 간격을 확보한다.

## HIG-NAV: 네비게이션 규칙
- **Tab Bar**: 화면 하단, 최상위 콘텐츠 분류, 정보 계층을 반영하는 컨트롤.
- **Navigation Bar**: 왼쪽 뒤로 버튼 + 중앙 타이틀 + 선택적 오른쪽 버튼 구조를 준수한다.
- **계층적 네비게이션**: 명확한 정보 계층, 일관된 패턴.

## HIG-MODAL: 모달/시트 규칙
- **모달은 사용자의 주의가 필요한 중요 작업에만 사용한다.** 과도한 모달 중첩을 피한다.
- **명확한 닫기 방법을 제공한다.** 완료/취소가 명확해야 한다.
- **작업 완료 후 이전 상태로 복귀한다.**

## HIG-ICON: 아이콘/이미지 규칙
- **고해상도 이미지 필수**: @2x 및 @3x 제공.
- **종횡비 유지**: 이미지를 의도된 종횡비로 표시하여 왜곡을 방지한다.
- **SF Symbols 활용**: 커스텀 아이콘보다 우선 고려한다.

## HIG-A11Y: 접근성 규칙
- **VoiceOver 지원**: 모든 인터랙티브 요소에 접근성 레이블과 힌트를 제공한다.
- **Dynamic Type 지원**: 모든 텍스트 요소가 사용자 정의 텍스트 크기에 반응한다.
- **Differentiate Without Color**: 색상 외 구분 방법을 제공한다.
- **Reduce Motion API 활용**: 애니메이션 대신 페이드 효과를 사용한다.

## HIG-FEEDBACK: 피드백/인터랙션 규칙
- **사용자 행동에 즉각적으로 반응한다.** 모든 탭/프레스에 시각적 피드백을 제공한다.
- **진행 상황을 표시한다.** 로딩/프로그레스 인디케이터.
- **Edit Menu**: 시스템 제공 edit menu 사용.

## HIG-LIST: 리스트/컬렉션 규칙
- **표준 row 또는 grid 레이아웃을 우선 사용한다.**
- **삽입, 삭제, 재정렬 시 애니메이션을 제공한다.**
- **사용자가 보고 상호작용하는 동안 동적 레이아웃 변경을 피한다.**

## HIG-SEARCH: 검색 규칙
- **Navigation Bar에 Search Bar를 통합한다.**
- **직관적인 검색 경험을 설계한다.**

## HIG-BRAND: 브랜드 아이덴티티 규칙 (iOS 26)
- **UI Layer**: 표준 컴포넌트 사용. 익숙한 패턴.
- **Content Layer**: 고유한 브랜드 아이덴티티 표현.
- UI와 Content의 경계를 명확히 분리한다.

## HIG-GLASS: Liquid Glass 규칙 (iOS 26)
- **표준 컴포넌트는 자동으로 Liquid Glass material이 적용된다.** 수동으로 유사 효과를 만들지 않는다.
- **Liquid Glass는 기능적 레이어에만 사용한다.** 콘텐츠 영역에 적용하지 않는다.

---

## 수치 요약 (빠른 참조)

| 항목 | 값 |
|---|---|
| 최소 터치 타겟 | 44pt x 44pt |
| 인접 터치 간격 | ≥ 8pt |
| 최소 텍스트 크기 | 11pt |
| 본문 대비율 | ≥ 4.5:1 |
| 대형 텍스트 대비율 | ≥ 3:1 |
| Compact margin | 16pt |
| Regular margin | 20pt |
| Navigation Bar 높이 | 44pt (표준) / 96pt (Large Title) |
| Tab Bar 높이 | 49pt + Safe Area |
| Status Bar | ~54pt |
| Home Indicator | ~34pt |
| iPhone 프레임 | 390x844pt / 393x852pt |
| iPad 프레임 | 820x1180pt / 1024x1366pt |
| iOS Dark 배경 권장 | #1C1C1E (순수 검정 아님) |
