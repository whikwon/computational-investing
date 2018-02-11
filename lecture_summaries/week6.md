## Summary
- [The Fundamental Law](#dd)
- [CAPM for Portfolios : Managing Market Risk](#ee)
- [How to Assess an Event Study](#ff)

## The Fundamental Law <a name="dd"></a>

### Thought Experiment - Coin Flipping
- Coin Flipping을 통해 Expected outcome, 위험 보상 비율(모두 잃을 확률, Reward Risk Ratio, Shape Ratio)에 대해서 알아보자.
- Expected outcome : $1,000로 1번의 배팅을 할 것인가 vs $1로 1,000번의 배팅을 할 것인가?
  (단, 51%의 확율로 win)
- 싱글 배팅일 경우 기대 수익 : 0.51 * $1,000 + 0.49 * -$1,000 = $20
- 멀티 배팅일 경우 기대 수익 : 1,000 * (0.51 * $1 + 0.49 * -$1) = $20
  -> 즉, 두 경우의 기대 수익은 같다
- 싱글 배팅일 경우 모두 잃을 확률 : 49%
- 멀티 배팅일 경우 모두 잃을 확률 : (49%)^1000 = 0.157e-309
  -> 즉, 멀티 배팅일 경우 모두 잃을 확률이 천문학적으로 적다
- Reward Risk Ratio -> Single : 0.63 vs Multi : 20 -> Multi bet is more than 20 times better!
- 즉, 결론적으로 멀티 배팅이 모든 것을 잃을 위험을 낮추며, 표준 편차를 낮추고, 보상 위험 비율을 훨씬 높이는 결과를 얻는다 (자세한 계산은 추가적으로 해보도록 하자)

### The Fundamental Law Part1 - IR, IC, BR
- IR(Information Ratio) : 위험조정 성과평가 척도의 하나, 포트폴리오의 초과 수익률을 추적 오차로 나눈 것
- IR = (포트폴리오 수익률 - 벤치마크 수익률) / 트래킹 에러
  -> 벤치마크 수익률 : 포트폴리오 성과를 상대적 관점에서 측정하기 위한 비교 대상 지표
                 ex) 주식펀드인 경우 KOSPI, KOSPI200 등
  -> 트래킹 에러 : 포트폴리오 수익률이 벤치마크 수익률을 제대로 추적하지 못하는 정도
  -> 결국 위험 1단위를 감수하는데 대해 보상받는 포트폴리오 추과수익
- IC(Information Coeffient) : The information coefficient (IC) is a measure of the merit of a predicted value. In finance, the information coefficient is used as a performance metric for the predictive skill of a financial analyst.[1] The information coefficient is similar to correlation in that it can be seen to measure the linear relationship between two random variables, e.g. predicted stock returns and the actualized returns. The information coefficient ranges from 0 to 1, with 0 denoting no linear relationship between predictions and actual values (poor forecasting skills) and 1 denoting a perfect linear relationship (good forecasting skills)
- BR(Breadth) : Breadth is about how often does it occur. How many times can you execute on this method that you've developed for discovering what a stock is gonna do. So that's breadth, BR.

### The Fundamental Law Part2 - James simons(Jim simons) vs Warren Buffet
- James Simons(Jim Simons) : 미국의 수학자이자 헤지 펀드 매니저다. 그는 백만장자 수학자로 유명하고, 또 수학에서 그는 Chern-Simons theory에 대한 업적으로 유명하다. 
   1978년, 그는 갑자기 학계를 떠나 투자 운용 회사인 Renaissance Technologies를 세우기 시작했다. 그는 많은 프로그래머, 물리학자, 계산언어학자, 그리고 수학자를 고용했다. 금융 데이터를 과학적으로 분석하고 미래 변화를 예측해서 거래를 했다. 그것이 얼마나 성공적이었냐하면, Renaissance Technologies의 가장 유명한 Medallion Fund는 1994년부터 2014년까지 연 평균 71.8%의 이익을 냈다고 한다. 순수하게 데이터를 분석하는 과학적인 접근으로 투자를 하는 것이 Renaissance Technologies의 성공 요인일 것이다.
- Quantitative Trading : 정량적 분석, 계량적 분석이라고 해석하고, 주로 통계적 분석에 기반하여 수익모델을 계량화하고 이를 수익모델로 트레이딩하는 것을 Quant Trading 이라고 한다.
  -> 통계적 차익거래를 한다 : 주식, 채권, 선물옵션들의 이론가치를 정량 분석하고, 시장가격이 통계적 범위 내에서 내재가격에 벗어날 때 매수나 매도를 하고, 계산된 이론 가치에 도달했을 때, 청산하여 수익을 낸다.
  ->  전제 : 1) 가격은 모든 시장요소가 반영되어 있다. 2) 과거의 패턴이 미래에도 반복 될 것이다.
  -> 즉, 수학 외적인 요소는 전혀 고려하지 않는다.
  -> 단기투자에 대한 패턴을 만들 수 있다 (금융위기 때, 대부분의 퀀트투자는 망했지만, 유일하게 건재했던 방법)
- Value Investment : 기업의 가치에 믿음을 둔 주식 현물 투자 전략을 말한다. 그리고 가치투자를 지향하는 주식 현물 투자가들을 가치투자자라고 부른다.
  -> 계속 기업이라는 가정 하에 PBR, PER을 계산하는 능력 / 'PBR, PER key-words updated'
    (PBR:주가를 한 주당 순자산으로 나눈 것, 주가순자산비율, 주가순자산배율, 장부가치)
    (PER:현재 주가를 주당순이익(순이익/총 발행주식)으로 나눈 값, 주가수익률, 주가이익률)
  -> 시장지배력, 브랜드, 비지니스 모델의 지속성
- Warren Buffet's Value Investment
  -> 주가는 신경쓰지말고 PBR을 믿어라. 화사의 성장과 가장 밀접한 관계가 있다.
  -> ROE(자기자본 수익율)가 높고 일관성 있는 주식을 선호한다 / 'ROE key-words updated'
  -> 성장율을 점칠 수 없는 하이테크 기업보다 수 십년간 이익을 증대하여 온 로테크 기업에 투자하라.
  -> 이익수익율(EPS/주가)이 장기채권과 비슷하거나 높을 때 투자하라 / 'EPS key-words updated'
  -> 손실 방지 규칙 : 1. 돈을 잃지 않는다. 2. 첫 번째 규칙을 지킨다.
  -> 절대 돈을 벌 수 있는 M&A 차익거래를 열심히 하자.

## CAPM for Portfolios : Managing Market Risk <a name="ee"></a>

### CAPM Recap, Overview for Portfolios
- $R_i=\alpha_i+\beta_iR_m+e_i$
- $E(R_i)=\alpha_i+\beta_iE(R_m)$
- Rm은 시장 전체적 요인, ei는 개별 기업적 요인
- 베타는 시장에서의 수익률, 시장과의 연관성으로 인해 우리가 자산에 투자 할 것으로 예상되는 수익
- 알파 부분은 스킬
- 포트폴리오의 기대 수익률은 모든 보유 자산에 대한 개별 수익의 가중치 합계

### Using CAPM to Reduce Risk

## How to Assess an Event Study <a name="ff"></a>
- RSI(Relative Strength Index) : 주식, 선물, 옵션 등의 기술적 분석에 사용되는 보조지표이다. RSI는 가격의 상승압력과 하락압력 간의 상대적인 강도를 나타낸다. / 'RSI key-words updated'
  -> 일정 기간 동안 주가가 전일 가격에 비해 상승한 변화량과 하락한 변화량의 평균값을 구하여, 상승한 변화량이 크면 과매수로, 하락한 변화량이 크면 과매도로 판단하는 방식이다.
  -> 그 외 계산방법은 키워드를 참조

### Reference
- https://blog.naver.com/drgal/60034306089
- https://en.wikipedia.org/wiki/Information_coefficient
- https://psh951120.blog.me/221026232552
- http://cafe.naver.com/gtabully/3943
- http://cafe.naver.com/vilab/68086
- https://ko.wikipedia.org/wiki/%EA%B0%80%EC%B9%98%ED%88%AC%EC%9E%90
- http://cafe.naver.com/stockschart/601605
- https://blog.naver.com/PostView.nhn?blogId=choe55&logNo=220151487564&parentCategoryNo=&categoryNo=7&viewDate=&isShowPopularPosts=true&from=search
- https://blog.naver.com/choe55/220158601238
- https://blog.naver.com/choe55/220171066331
- https://ko.wikipedia.org/wiki/RSI_(%ED%88%AC%EC%9E%90%EC%A7%80%ED%91%9C)
- Coursera - Computational Investing Week 5 
