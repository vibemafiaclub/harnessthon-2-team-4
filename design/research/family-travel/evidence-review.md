# 공개 화면 독립 검수

2026-09-05. 수집자 root, 검수자 `/root/family_travel_evidence` 신규 컨텍스트. 격리: 프롬프트 지시만. 지정 이미지 9개와 관찰 주장만 제공했다. 추천·보고서·사용자 선호·decisions.md는 미제공. 파일 탐색·수정 금지. 아래는 검수자 응답 원문이다.

| 이미지 | 판정 | 확인 위치·한계 |
|---|---|---|
| familywall-calendar.png | SUPPORTED | 중앙에 “Weekend at Grandma’s” 제목과 시작·종료 일시, 아래 참여자 아바타와 지도, 맨 아래 “Type your comment...” 입력 영역이 보인다. |
| cozi-calendar.png | SUPPORTED | 중앙 기기 일정에 여러 색 점이 있고, 기기 바깥 인물 사진을 같은 계열 색 선으로 연결한 홍보 합성이다. 작은 일정 문구의 상세 판독은 제한된다. |
| cozi-today.png | SUPPORTED | 기기 내부 상단 “Upcoming events”, 중하단 “Groceries”, 최하단 “Anne’s To Do” 구역이 한 화면에 보인다. 할 일 구역은 하단이 잘려 내용 전체를 확인할 수 없다. |
| timetree-calendar.png | SUPPORTED | “Jun 2026” 월 달력과 일정 라벨, 하단 Events/Album/Add/Activity/Memo가 보인다. 빨간 1–13 번호와 강조 테두리는 화면 요소를 가리키는 안내 주석 형태다. |
| timetree-comments.png | SUPPORTED | 상단 “Yoga”, 시작 18:30·종료 19:30, 하단 사진 아이콘과 “Comment” 입력 영역이 보인다. 사진 아이콘의 빨간 테두리는 강조 주석이다. |
| wanderlog-plan.png | SUPPORTED | 왼쪽 여행 계획 영역과 오른쪽 지도, 상단 “Trip to London”, 사람+ 아이콘이 보인다. 주황색 원·화살표가 해당 영역을 강조한다. 아이콘의 실제 동작은 확인하지 않았다. |
| wanderlog-transit.png | SUPPORTED | 상단 날짜 선택 영역, 번호 1·2·3 장소 사이에 자동차 아이콘과 “10 mins drive · 6.8 km”, “5 mins drive · 1.9 km”, Directions가 보인다. 주황색 표시가 추가되어 있다. |
| wanderlog-offline.png | SUPPORTED | Trip plans 목록의 런던·NYC 항목에 제목, 날짜, 참여자 아바타와 아래 화살표 아이콘이 보인다. 런던은 날짜 오른쪽, NYC는 다음 줄에 아이콘이 있다. 다운로드 완료 여부는 확인할 수 없다. |
| tripit-timeline.png | SUPPORTED | 기울어진 기기 목업 내부에 비행기·침대·자동차 아이콘, 08:30·PST·EST 등의 시간 정보, “Scheduled” 상태 라벨이 보인다. 오른쪽과 하단 일부가 잘려 있다. |

검수 범위는 지정된 정적 이미지의 가시 요소이며, 앱 직접 실행·동작 성공·성능·원본 토큰·최신 버전 일치 여부는 판정하지 않았다.

## 원문 외 기록

REF-FW-02, REF-CZ-03, REF-WL-04는 수집자가 직접 이미지를 보았으나 이번 독립 검수 대상은 아니므로 not-reviewed다. 공식 소개·도움말의 문장 사실은 수집자가 출처를 확인했으며 이번 이미지 검수의 SUPPORTED를 문서 전체 검수로 확장하지 않는다. 사람의 최종 채택은 모든 REF에서 pending이다.
