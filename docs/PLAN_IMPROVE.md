Figma Design Guide

«Codex가 Figma 화면을 생성·수정할 때 따라야 하는 디자인 원칙과 검수 기준이다.
목표는 단순히 깔끔한 UI를 만드는 것이 아니라, 사용자가 한 화면을 보는 순간 무엇을 이해하고 무엇을 해야 하는지 명확히 알 수 있도록 하는 것이다.»

---

1. Core Design Principles

모든 화면은 아래 4가지 질문을 기준으로 설계하고 검수한다.

1.1 이 화면에서 무엇을 보여줘야 하는가?

각 화면을 만들기 전에 먼저 정의한다.

- 사용자가 이 화면에 들어온 이유는 무엇인가?
- 이 화면에서 가장 먼저 알아야 하는 정보는 무엇인가?
- 사용자가 다음으로 해야 할 행동은 무엇인가?
- 가장 중요한 정보와 보조 정보는 무엇인가?

화면을 먼저 디자인하지 않는다.

반드시 다음 순서로 결정한다.

User Goal
→ Primary Message
→ Primary Action
→ Supporting Information
→ Layout
→ Visual Design

---

2. Main Screen

메인 화면은 서비스의 모든 기능을 나열하는 화면이 아니다.

서비스가 사용자에게 제공하는 핵심 가치와 현재 해야 할 행동을 가장 빠르게 이해시키는 화면이어야 한다.

Main Screen에서 반드시 전달해야 하는 것

1. 서비스의 핵심 메시지

사용자가 3~5초 안에 다음을 이해할 수 있어야 한다.

이 서비스가 무엇인지
+
나에게 어떤 가치를 주는지
+
지금 무엇을 하면 되는지

2. 가장 중요한 정보

메인 화면에는 Primary Information을 하나 명확하게 둔다.

예:

오늘의 핵심 결과
오늘의 상태
현재 진행 단계
나에게 가장 중요한 인사이트

여러 정보를 동일한 중요도로 보여주지 않는다.

---

3. Primary CTA

사용자가 다음에 해야 할 행동을 하나 명확하게 만든다.

예:

결과 확인하기
분석 시작하기
오늘의 운세 보기
다음 단계 진행하기

Primary CTA와 Secondary CTA의 시각적 강도를 반드시 구분한다.

---

3. One Page = One Step

사용자의 Workflow를 가능한 한 세분화한다.

하나의 화면에서 여러 단계의 행동을 동시에 요구하지 않는다.

Bad

정보 입력
→ 옵션 선택
→ 분석
→ 결과 확인
→ 추가 질문

모두 한 화면

Good

Step 1. 기본 정보 입력

↓

Step 2. 관심 영역 선택

↓

Step 3. 분석

↓

Step 4. 핵심 결과

↓

Step 5. 상세 해석

원칙

«One Page = One Primary Goal»

각 페이지에는 반드시 다음 세 가지가 존재해야 한다.

① 현재 사용자가 어느 단계에 있는가

② 이 화면에서 무엇을 해야 하는가

③ 행동 이후 어디로 이동하는가

---

4. Screen Message

각 화면을 만들기 전에 다음 형식으로 정의한다.

## Screen Purpose

User Goal:
사용자가 이 화면에서 원하는 것

Primary Message:
이 화면에서 가장 강하게 전달해야 하는 메시지

Primary Action:
사용자가 수행해야 할 가장 중요한 행동

Secondary Information:
Primary Message를 이해하기 위해 필요한 보조 정보

디자인은 이 구조를 시각적으로 표현해야 한다.

---

5. Visual Hierarchy

화면에서 모든 요소를 강조하지 않는다.

디자인의 핵심은 강약이다.

화면은 기본적으로 다음 구조를 따른다.

PRIMARY
가장 중요한 메시지 / 결과 / 행동

        ↓

SECONDARY
Primary를 설명하거나 지원하는 정보

        ↓

TERTIARY
부가 정보 / 상세 설명 / 참고 정보

Primary

가장 먼저 보여야 한다.

예:

- 핵심 숫자
- 핵심 메시지
- 주요 결과
- Primary CTA
- 핵심 이미지/상징

다음 요소를 이용해 강조할 수 있다.

- 크기
- Typography
- Contrast
- 공간
- 색
- 위치

---

Secondary

Primary를 받쳐준다.

Secondary 요소 자체가 Primary와 경쟁해서는 안 된다.

예:

- 설명
- 관련 수치
- 서브 카드
- 추가 인사이트
- Secondary CTA

---

Tertiary

필요할 때 읽는 정보다.

시각적 강도를 낮춘다.

예:

- 부연 설명
- 도움말
- 메타데이터
- 세부 정보
- Disclaimer

---

6. Bento Grid

정보를 표현할 때 Bento Grid를 주요 레이아웃 시스템으로 활용한다.

단, Bento Grid는 단순히 여러 카드로 화면을 채우기 위한 장식이 아니다.

정보의 위계와 Grouping을 표현하기 위한 시스템으로 사용한다.

---

Bento Grid Hierarchy

가장 중요한 콘텐츠는 가장 큰 영역을 차지한다.

예:

┌─────────────────────────────┐
│                             │
│        PRIMARY CARD         │
│                             │
├──────────────┬──────────────┤
│ Secondary A  │ Secondary B  │
├──────────────┴──────────────┤
│ Supporting Information      │
└─────────────────────────────┘

또는

┌──────────────────┬──────────┐
│                  │ Sub A    │
│   PRIMARY        ├──────────┤
│                  │ Sub B    │
├──────────────────┴──────────┤
│ Supporting Card             │
└─────────────────────────────┘

중요도가 높은 정보일수록 다음을 사용한다.

larger area
+
stronger typography
+
higher contrast
+
more whitespace

---

7. Bento Grid Usage Rules

Bento Grid를 사용한다고 모든 카드를 동일한 크기로 만들지 않는다.

Bad

Card A
Card B
Card C
Card D

모두 동일 크기
모두 동일 색상
모두 동일 강조

정보 위계가 사라진다.

Good

Main Insight        → Large

Key Supporting Info → Medium

Details             → Small

즉,

«Card Size = Information Importance»

가 되어야 한다.

---

8. Emotional Direction

디자인의 목표 감성은 다음과 같다.

Warm + Calm + Modern

사용자에게 차갑고 기계적인 AI 서비스가 아니라,

따뜻함
편안함
신뢰감
차분함
개인적인 경험

을 전달해야 한다.

---

9. Color Direction

컬러는 단순히 예쁜 색을 선택하는 것이 아니라 서비스의 감정을 전달해야 한다.

Primary Tone

따뜻하고 차분한 계열을 우선 검토한다.

예:

Warm Ivory
Cream
Soft Beige
Sand
Warm Gray
Muted Brown

Accent Color는 서비스의 주제와 연결한다.

---

현대적인 사주 / 오행 서비스라면

전통적인 사주 이미지를 그대로 복제하지 않는다.

다음 키워드로 재해석한다.

Traditional Symbol
+
Modern Interpretation

예:

木
火
土
金
水

오행을 직접적인 전통 문양으로 과도하게 사용하기보다,

- 색
- Typography
- Symbol
- Texture
- 작은 Graphic Accent

등으로 현대적으로 표현한다.

---

10. Typography

폰트 역시 서비스의 감정을 전달해야 한다.

Typography 방향:

Warm
Readable
Calm
Human
Modern

너무 기술적이고 차가운 느낌의 Typography는 피한다.

---

Typography Hierarchy

최소 다음 레벨을 일관되게 정의한다.

Display
Heading 1
Heading 2
Body
Caption
Label

예:

Display
핵심 결과

Heading
카드 제목

Body
설명

Caption
보조 정보

각 화면에서 임의로 Font Size를 만들지 않는다.

---

11. Subject-Specific Typography

서비스가 사주 / 전통 / 동양적 요소를 포함한다면

한자 또는 핵심 Symbol을 Typography Hero Element로 활용할 수 있다.

예:

木
火
土
金
水

단,

전통 디자인을 그대로 재현하는 것이 아니라

Large Chinese Character
+
Modern Sans Serif
+
Generous Whitespace

조합처럼 현대적으로 해석한다.

---

12. Component Consistency

페이지마다 새로운 UI 문법을 만들지 않는다.

한 번 정의한 컴포넌트는 모든 화면에서 동일한 규칙을 따른다.

반드시 일관되어야 하는 요소:

Card
Button
Input
Navigation
Modal
Bottom Sheet
Chip
Badge
Icon
Typography
Spacing
Border Radius
Shadow
Color

---

13. Layout Consistency

예를 들어 첫 번째 화면에서 Bento Grid를 사용했다면

다음 화면에서 아무 이유 없이 완전히 다른 디자인 문법으로 변경하지 않는다.

Bad

Screen 1
Bento Grid

Screen 2
Glassmorphism

Screen 3
Flat Dashboard

Screen 4
Editorial Magazine

각각은 예뻐도 하나의 Product처럼 느껴지지 않는다.

---

Good

모든 화면이 같은 Design DNA를 공유한다.

Same Grid Logic

Same Card Language

Same Radius

Same Typography Hierarchy

Same Color System

Same Spacing System

Same Interaction Pattern

페이지마다 Layout variation은 가능하지만

Visual Grammar는 유지한다.

---

14. Design System

가능하면 먼저 Design Token을 정의한다.

Color Tokens

background
surface
surface-secondary

text-primary
text-secondary
text-muted

primary
primary-hover
primary-subtle

border
divider

success
warning
error

---

Radius

가능하면 3~4개 이하로 제한한다.

radius-sm
radius-md
radius-lg
radius-xl

---

Spacing

일정한 Spacing System을 사용한다.

예:

4
8
12
16
24
32
48
64

임의로

17
21
29
37

같은 값을 계속 만들지 않는다.

---

15. Component Variants

컴포넌트는 상태를 Variant로 관리한다.

예:

Button

Primary
Secondary
Ghost
Disabled
Loading

Card

Hero
Standard
Compact
Interactive

Input

Default
Focus
Filled
Error
Disabled

---

16. Main vs Supporting Components

화면마다 Hero Component가 하나 존재하도록 한다.

Hero Component는 가장 중요한 메시지를 표현한다.

예:

Today's Insight

五行 Balance

Current Result

Recommended Action

그리고 나머지 컴포넌트는 Hero를 지원한다.

Hero Card

↓ supported by

Insight Card
Detail Card
Timeline
Recommendation
Secondary Action

모든 Card가 Hero처럼 보이면 안 된다.

---

17. Screen Composition Rule

모든 화면은 가능하면 다음 순서로 구성한다.

Context

↓

Primary Message

↓

Primary Action / Primary Information

↓

Supporting Information

↓

Optional Detail

사용자가 화면을 위에서 아래로 읽었을 때 자연스럽게 이해되어야 한다.

---

18. Reduce Cognitive Load

한 화면에서 사용자가 판단해야 하는 선택지를 과도하게 늘리지 않는다.

특히 다음 상황을 피한다.

5개의 Primary Button

10개의 동일한 Card

긴 설명문

중요도가 구분되지 않은 숫자

여러 단계의 Form이 하나의 화면에 존재

사용자가

«"그래서 여기서 뭘 해야 하지?"»

라고 생각하게 만들어서는 안 된다.

---

19. Progressive Disclosure

상세 정보는 처음부터 모두 노출하지 않는다.

Summary
↓
Key Insight
↓
Details
↓
Deep Dive

구조를 사용한다.

예:

오늘의 핵심 해석

↓

왜 이런 결과가 나왔나요?

↓

오행별 상세 분석

↓

전문 해석

---

20. Workflow Visualization

여러 단계가 존재하는 경우 현재 위치를 명확하게 보여준다.

예:

01 정보 입력
02 관심사 선택
03 분석
04 결과

현재 단계는 강조하고

완료된 단계와 이후 단계를 시각적으로 구분한다.

---

21. Figma Implementation Rule

Codex가 Figma를 수정할 때 기존 Frame을 개별적으로 꾸미는 방식으로 접근하지 않는다.

먼저 다음을 확인한다.

1. Current User Flow

2. Existing Design Tokens

3. Existing Components

4. Existing Grid

5. Existing Typography

6. Existing Spacing

7. Existing Screen Hierarchy

그 이후 수정한다.

---

22. Codex Design Workflow

Codex는 다음 순서로 작업한다.

Step 1 — Understand

현재 Figma 전체 화면을 살펴보고

Screens
Components
Styles
Tokens
User Flow

을 파악한다.

---

Step 2 — Define User Workflow

각 화면의 역할을 정의한다.

예:

Screen 01
Service Introduction

Screen 02
User Input

Screen 03
Preference Selection

Screen 04
Analysis

Screen 05
Main Result

Screen 06
Detail Result

---

Step 3 — Define Message

각 화면마다 다음을 작성한 뒤 디자인한다.

Primary Message
Primary Action
Secondary Information

---

Step 4 — Establish Design System

반복되는 요소를 Component / Style / Variable로 정리한다.

---

Step 5 — Apply Bento Hierarchy

정보 중요도에 따라 Card Size와 위치를 결정한다.

---

Step 6 — Apply Emotional Design

Color / Typography / Spacing / Graphic 요소를 통해

Warm
Calm
Modern

감성을 유지한다.

---

Step 7 — Check Consistency

모든 Screen을 한 번에 펼쳐놓고 비교한다.

한 화면만 예쁜지를 보는 것이 아니다.

다음을 확인한다.

전체 화면이 하나의 서비스처럼 보이는가?

---

23. Design Review Checklist

각 화면을 수정한 후 아래 질문에 답한다.

Information

- [ ] 이 화면의 목적을 한 문장으로 설명할 수 있는가?
- [ ] 사용자가 가장 먼저 봐야 하는 것이 명확한가?
- [ ] Primary / Secondary 정보가 구분되어 있는가?
- [ ] 사용자가 다음에 해야 할 행동이 명확한가?

Workflow

- [ ] 한 화면이 하나의 주요 단계를 담당하는가?
- [ ] 여러 행동을 한 화면에 과도하게 넣지 않았는가?
- [ ] 이전 단계와 다음 단계가 자연스럽게 연결되는가?
- [ ] 사용자가 현재 위치를 알 수 있는가?

Visual Hierarchy

- [ ] 가장 중요한 요소가 가장 강조되는가?
- [ ] Secondary 요소가 Primary를 받쳐주는가?
- [ ] 모든 요소가 동시에 강조되고 있지 않은가?

Emotion

- [ ] 따뜻한 느낌이 전달되는가?
- [ ] 너무 차갑거나 Dashboard처럼 보이지 않는가?
- [ ] Color와 Typography가 서비스의 주제와 연결되는가?

Bento Grid

- [ ] Bento Grid가 단순 장식이 아니라 정보 위계를 표현하는가?
- [ ] 카드 크기가 정보 중요도와 연결되어 있는가?
- [ ] Grid 구조가 화면마다 일관되는가?

Components

- [ ] 동일한 Button은 동일하게 보이는가?
- [ ] Card 스타일이 일관되는가?
- [ ] Border Radius가 일관되는가?
- [ ] Spacing System이 유지되는가?
- [ ] Typography hierarchy가 유지되는가?

Product Consistency

모든 페이지를 펼쳐놓고 확인한다.

- [ ] 동일한 서비스처럼 느껴지는가?
- [ ] 갑자기 다른 디자인 스타일의 페이지가 등장하지 않는가?
- [ ] 같은 Visual Grammar가 유지되는가?

---

24. Things to Avoid

다음을 피한다.

1. Generic AI Dashboard

카드 8개
아이콘 8개
모든 카드 동일 크기
Gradient
모든 정보 동일 강도

---

2. Decoration Before Information

정보 구조보다 먼저

Gradient
Shadow
Illustration
Glass Effect

을 추가하지 않는다.

---

3. Too Many Design Styles

Bento Grid를 사용하면서 동시에

Glassmorphism
Brutalism
Editorial
Material
Neumorphism

등 여러 디자인 문법을 섞지 않는다.

---

4. Too Many Accents

Accent Color를 과도하게 사용하지 않는다.

강조해야 할 부분이 많아질수록

실제로 강조되는 것은 없어진다.

---

5. Screen-by-Screen Optimization

각 화면만 따로 보고 디자인하지 않는다.

항상 전체 User Flow를 함께 확인한다.

---

25. Final Acceptance Criteria

디자인 완료 후 아래 5개 질문에 모두 YES가 되어야 한다.

1.

메인화면을 5초만 봐도

이 서비스가 무엇을 제공하는지 알 수 있는가?

2.

각 화면에서

사용자가 무엇을 해야 하는지 바로 알 수 있는가?

3.

가장 중요한 정보와 보조 정보 사이에

명확한 시각적 강약이 존재하는가?

4.

Color / Typography / Spacing을 통해

Warm + Calm + Modern이라는 감성이 전달되는가?

5.

모든 화면을 펼쳐놓았을 때

하나의 동일한 Product Design System으로 보이는가?

---

Codex Final Instruction

Figma를 수정할 때 기존 UI를 단순히 미적으로 개선하지 말 것.

가장 먼저

User Workflow
→ Screen Purpose
→ Information Hierarchy
→ Design System
→ Visual Design

순서로 판단한다.

특히 다음 원칙을 최우선으로 유지한다.

«One Page = One Primary Step»

«One Screen = One Primary Message»

«Primary content must visually dominate supporting content.»

«Bento Grid represents information hierarchy, not decoration.»

«Warmth must be expressed consistently through typography, color, spacing, and component styling.»

«Every screen must belong to the same visual system.»

최종적으로 디자인의 목표는

**“보기 좋은 화면”이 아니라
“사용자가 현재 무엇을 보고 있으며 다음에 무엇을 해야 하는지 즉시 이해할 수 있는 화면”**이다.