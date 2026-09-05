# Brief — 앱 전체 공통 원장 (`_system`)

> 화면별 원장(`design/invitation-scheduler/brief.md`)은 이 파일의 토큰을 **실측 소스**로 인용한다.
> 이 프로젝트는 Greenfield(기존 라이브러리 없음)라, 토큰은 제작단계가 Figma 변수·텍스트 스타일로
> **먼저 생성**하고, 그 생성 결과가 A단계의 실측 기준이 된다. 값 자체의 선정은 사람이 위임했으므로 소스=가정(위임).

## target

```yaml
target:
  file_url: https://www.figma.com/design/xMsSA6ndIWBXEANJ0Ycphf
  file_key: xMsSA6ndIWBXEANJ0Ycphf
  pages:
    - "00 README"        # 에이전트용 안내·데이터 모델·상태 어휘 (id 0:1)
    - "01 Foundations"   # 변수·텍스트 스타일 시각화 (id 2:2)
    - "02 Components"    # 컴포넌트 세트 (id 2:3)
    - "03 Screens"       # 화면 프레임 390×844 (id 2:4)
```

## 디자인 토큰 — Figma 변수 컬렉션 `Tokens` (id `VariableCollectionId:2:5`, 모드 `Default`)

### 색 — `color/*` (실측: 2026-09-05 생성, 26개)
| 변수 | HEX | 용도 |
|---|---|---|
| color/bg/canvas | #F7F3EE | 화면 배경 (따뜻한 아이보리) |
| color/bg/surface | #FFFFFF | 카드·시트 |
| color/bg/subtle | #EFE9E1 | 비활성 영역·구분 배경 |
| color/border/default | #E5DDD2 | 기본 테두리 |
| color/text/primary | #1E1A17 | 본문 |
| color/text/secondary | #6B6259 | 보조 텍스트 |
| color/text/tertiary | #78706A | 플레이스홀더·힌트 (A-0 대비율 수정: 구 #9C928A 3.05:1 → 4.86:1 on white) |
| color/text/inverse | #FFFFFF | 진한 배경 위 텍스트 |
| color/brand/primary | #A93A31 | 주 액션 (봉인 도장의 붉은색) (구 #B8433A) |
| color/brand/primary-soft | #F6E3E0 | 주 액션 연한 배경 |
| color/side/groom | #3F5F8A | 신랑 측 |
| color/side/groom-soft | #E1E9F3 | 신랑 측 연한 배경 |
| color/side/bride | #A3455F | 신부 측 (구 #C2607A) |
| color/side/bride-soft | #F7E3E9 | 신부 측 연한 배경 |
| color/side/both | #7A5E1C | 양가 공동(상견례 등) (구 #9A7A2E) |
| color/side/both-soft | #F3EBD6 | 양가 연한 배경 |
| color/status/waiting | #8F5E0E | 회신 대기 (구 #C98A1C) |
| color/status/waiting-soft | #FBEFD6 | |
| color/status/ready | #6B4FA0 | 확정 대기(회신 마감) |
| color/status/ready-soft | #ECE5F6 | |
| color/status/confirmed | #256B4D | 확정 (구 #2E7D5B) |
| color/status/confirmed-soft | #DDF0E6 | |
| color/status/done | #6B645C | 다녀옴 (구 #8A8279) |
| color/status/done-soft | #ECE8E3 | |
| color/status/danger | #B02E2E | 겹침 경고·불가 (구 #C43B3B) |
| color/status/danger-soft | #FBE1E1 | |

> **개정 2026-09-05 (A-0 고정 하한선 대응)**: 소프트 배경 위 12~13px 라벨과 3차 텍스트의 WCAG AA(4.5:1) 미달로 8개 토큰 값을 어둡게 조정. 변수 바인딩이므로 두 파일(`ZVyw…`, `xMsSA…`) 모두 값만 갱신했다. 비활성 버튼 라벨(tertiary on subtle, 4.03:1)은 WCAG 1.4.3 비활성 컴포넌트 예외로 둔다.

### 간격 — `space/*` (4pt 그리드)
`space/1`=4, `space/2`=8, `space/3`=12, `space/4`=16, `space/5`=20, `space/6`=24, `space/8`=32, `space/10`=40

### 모서리 — `radius/*`
`radius/sm`=8, `radius/md`=12, `radius/lg`=16, `radius/pill`=999

### 타이포 — 텍스트 스타일 (폰트: Noto Sans KR — 실측: `listAvailableFontsAsync`에 Regular/Medium/Bold 존재. Pretendard 미존재)
| 스타일 | 크기/행간 | 굵기 |
|---|---|---|
| Display | 28/36 | Bold |
| Title/LG | 22/30 | Bold |
| Title/MD | 18/26 | Bold |
| Body/LG | 16/24 | Medium |
| Body/MD | 15/22 | Regular |
| Body/MD-Strong | 15/22 | Medium |
| Caption | 13/18 | Regular |
| Caption/Strong | 13/18 | Medium |
| Label | 12/16 | Medium |

## 상태 어휘 (PRD §4-6 → 앱 전역 enum)
| 코드 | 한글 라벨 | 뜻 | 색 토큰 |
|---|---|---|---|
| `waiting` | 회신 대기 | 후보를 보냈고 마감 전, 미회신자 있음 | status/waiting |
| `ready` | 확정 대기 | 전원 회신 완료 또는 마감 경과 — 커플이 날짜를 골라야 함 | status/ready |
| `confirmed` | 확정 | 날짜 확정·전원 공유됨 | status/confirmed |
| `done` | 다녀옴 | 모임 날짜 경과 | status/done |

## 네이밍 컨벤션
- 화면 프레임: `S<nn> <한글 화면명>` (예 `S06 모임 상세 · 회신 수합`)
- 컴포넌트: `<Category>/<Name>`; 배리언트 속성은 영문 camelCase (`type`, `size`, `state`, `side`, `status`)
- 내부 레이어: 영문 kebab-case 역할명 (`header`, `title`, `member-list`, `cta`). 자동 기본명(`Frame 12`) 금지.
- 변수: `color/…`, `space/…`, `radius/…`
