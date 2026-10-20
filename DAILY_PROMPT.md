# 매일 실행 지침 (EU 데일리 브리프)

대상: LG전자 VS사업본부 해외영업(유럽) 담당자.
VS 제품군: 인포테인먼트·텔레매틱스, ADAS 카메라, 차량용 램프(ZKW), e-파워트레인(LG마그나). 고객은 유럽 완성차(OEM)와 Tier-1.

## 1. 수집
- https://www.euronews.com/ , https://www.eurotopics.net/en/ 는 WebFetch로 홈페이지를 직접 읽는다.
- POLITICO Europe(https://www.politico.eu/)는 홈페이지 직접 수집이 막혀 있으면 WebSearch("POLITICO Europe" + 자동차/통상/에너지/EU 규제, 최근 24시간)로 기사를 찾는다.
- BBC 코리아(https://www.bbc.com/korean/topics/cdr56k47q13t)는 시도해 보고 차단되면 우회하지 말고 sources_status에 "blocked"로 기록한다.
- 최근 24~48시간 기사만 사용. 자동차 산업, EU 규제·통상, 에너지·원자재, 거시경제(금리·인플레이션·소비), 물류·파업·소요, 기상재해를 우선한다. VS와 무관한 기사(문화·여행 등)는 제외.

## 2. 작성 규칙
- 뉴스만으로 수요 증감을 확정하지 않는다. 모든 영향은 "~할 가능성", "~일 수 있음" 같은 가설로 쓴다.
- 각 항목에 caveat(아직 확인되지 않은 것)를 반드시 쓴다.
- 각 가설은 바이어에게 확인할 구체적 행동(SOP·forecast·call-off·RFQ 조건·물류·재고 등)으로 연결한다.
- buyer_question은 바이어에게 그대로 보낼 수 있는 영어 한 문장.
- 기사 문장을 그대로 옮기지 말고 한국어로 요약·재서술한다. 출처 URL은 실제 확인한 것만.
- 항목 5~8개, 관련도(높음/중간/낮음) 순으로 정렬.

## 3. 출력
- data/YYYY-MM-DD.json (오늘 KST 날짜) 를 data/ 안 기존 파일과 같은 스키마로 만든다.
- `python3 build.py` 실행 → index.html, archive/*.html 갱신.
- 저장소에 커밋 후 main 브랜치에 push (GitHub Pages가 자동 배포).
