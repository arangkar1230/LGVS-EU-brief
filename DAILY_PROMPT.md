# 매일 실행 지침 (EU 데일리 브리프)

대상: LG전자 VS사업본부 해외영업(유럽) 담당자.
VS 제품군: 인포테인먼트·텔레매틱스, ADAS 카메라, 차량용 램프(ZKW), e-파워트레인(LG마그나). 고객은 유럽 완성차(OEM)와 Tier-1.

## 1. 수집
- https://www.euronews.com/ , https://www.eurotopics.net/en/ 두 곳을 WebFetch로 직접 읽는다. 이 두 사이트가 기본 출처다.
- 사실 확인이 더 필요할 때만 WebSearch를 쓰고, 그때 쓴 출처는 "(사실 확인용)"으로 표시한다.
- 최근 24~48시간 기사를 우선. 직전 기사가 아니어도 진행 중인 핵심 이슈(예: EU 자동차 규제)는 최신 진척과 함께 쓸 수 있다.
- 사이트 수집에 실패하면 우회하지 말고 sources_status에 "error" 또는 "blocked"로 기록한다.

## 2. 고르기 — 정확히 5개
- section "top" 2개: 두 사이트에서 가장 비중 있게 다룬 오늘의 가장 큰 유럽 이슈 (VS 연관성과 무관하게 선택).
- section "vs" 3개: VS본부 사업과 연관성이 가장 높은 뉴스 (자동차 산업, EU 자동차 규제·통상, 경쟁사·중국 브랜드, 에너지·원자재, 물류·파업, 기상재해 등).
- 같은 사건은 하나로 묶고, top과 vs가 겹치지 않게 한다.
- items 배열 순서: top 2개 → vs 3개.

## 3. 작성 규칙 (5개 모두 적용)
- 뉴스만으로 수요 증감을 확정하지 않는다. 영향은 "~할 가능성", "~일 수 있음" 같은 가설로, VS 제품의 수요 또는 유통(납품·물류·재고) 기준으로 쓴다.
- caveat: 아직 확인되지 않은 것을 반드시 쓴다.
- actions: 바이어에게 확인할 구체적 행동 (판매 추이·재고·SOP·forecast·call-off·RFQ 조건·물류 등). 예) 폭염 뉴스 → "냉방 관련 수요 가설" → "현지 판매 추이와 재고를 확인하자".
- buyer_question: 바이어에게 그대로 보낼 수 있는 영어 한 문장.
- 기사 문장을 그대로 옮기지 말고 한국어로 요약·재서술한다. 출처 URL은 실제 확인한 것만.
- today_actions: 5개 항목의 행동을 3~5줄 체크리스트로 묶는다.

## 4. 출력
- data/YYYY-MM-DD.json (오늘 KST 날짜) 를 data/ 안 가장 최근 파일과 같은 스키마로 만든다 (필드: date, generated_at, headline, sources_status, items[id, section, category, title, summary, sources, hypothesis{products, direction, text}, caveat, actions, buyer_question], today_actions).
- `python3 build.py` 실행 → index.html, archive/*.html 갱신.
- 저장소에 커밋 후 main 브랜치에 push (GitHub Pages가 자동 배포).
