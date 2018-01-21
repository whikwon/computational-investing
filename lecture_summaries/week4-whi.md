# Week 4
## Event Studies
  - equity price에 영향을 주는 흔한 source들 
  - infomation이 어떻게 회사 가치에 영향을 주는지 
  - Efficient Markets Hypothesis에 대해서 배운다.
  
- 주식 거래는 true value를 기준으로 낮아질 때 buy 높아졌을 때 short을 하는 것이다. true value에 대한 내용은 여기선 다루지 않는다. 
- Market relative: market과 portpolio 간의 차이?
- Value를 결정하기 위한 2가지 접근 방식
  - Technical Analysis
    - Price & Volume
  - Fundamental Analysis
    - Financial statements
    - P/E ratios, cash on hand, dividend
- Informations: 가격/거래량은 시장에서, fundamentals은 dart에서, news는 각종 사이트에서 가져온다. 

## Efficient Markets Hypothesis
3가지 버전이 있다. 
- Weak: 현재 prices는 모든 과거의 publicy available information을 반영하고 있다. 현재 information에 대한 반영은 느리다. -> technical analysis로 profit 얻을 수 없다. 
- Semi-Strong: weak + price는 즉각적으로 새로운 public을 반영한다. -> technical analysis, Fundamental analysis로 profit 얻을 수 없다.
- Strong: Semi-string + price는 hidden 정보도 반영한다. -> insider information으로 profit 얻을 수 없다.
  - 교수 개인 견해로는 insider 정보로 많이 이득을 취한다고 한다. 

- EMH가 실제로 작동하나? -> P/E ratio와 annual return 관계를 보면 성립하지 않는다. 
- 행동 경제학으로 설명하려는 집단도 있다. 
  - overconfidence
  - overreaction
  - information bias 
  - news에 의해서 갑자기 가격이 오르거나 떨어지거나 하는 현상에 대해 다룬다. 


## Event studies (Mackinlay)
- good/bad event가 발생하기 전부터 가격이 변동된다.
  - 정보가 미리 새어나가서 그렇다는 견해가 있다. 
  - 나쁜 뉴스는 이미 나쁜 주식이라서 뉴스가 발생해서 더 내려가는 것이라고 볼 수도 있다. 
  - 나쁜 뉴스는 내려간 뒤에 어느 정도 회복한다. 

# Portfoli Optimization and the Efficient Frontier
- risk, correlation, covariance, Mean Variance, Optimization, Efficient Frontier를 배운다. 

## risk
volatility(std), draw down, risk를 계산할 수 있다. portpolio의 equity는 risk와 return으로 나타낼 수 있다. 
주로 risk가 높은 equity는 return이 높다. 다양한 equity를 조합해서 적정한 risk와 return을 갖도록 해야 한다. 
이게 portfolio optimiziation! 
- Harry Markovwitz는 portfolio theory, capitial assets pricing model 공로로 노벨상을 받았다. 

## Portfolio optimization
- inputs: 
  - 각 equity에 대한 Expected return (과거에서 미래에 대한 가격의 expectation. 예측이 들어가야 한다!)
  - 각 equity에 대한 volatility/risk
  - target return (우리가 원하는 return 값) 
  - **covariance matrix**
- outputs: equity에 할당해야 하는 가중치가 나온다. 이 가중치는 target return을 minimum risk로 달성할 수 있게 해준다. 


## 개별 equity를 조합해서 어떻게 Portfolio의 risk를 줄일 수 있나?
몇몇 경우에 대해서 target return에 대해서 equity 개별에 대해서 보다 portfolio를 조합할 경우 risk를 낮출 수 있다. 
- 예시: ABC, DEF, GHI로 이루어진 각각의 portfolio가 있다. ABC, DEF는 correlation이 높아서(0.9) 변동성이 같이 움직인다. 반면에 GHI는 반대로 움직인다.(-0.9) 이 때, ABC, DEF를 50:50으로 portfolio를 구성하면 변동성이 같기 때문에 기존과 같은 변동성을 갖는다. 반면에 ABC, DEF, GHI를 25:25:50으로 섞는 경우에는 GHI가 나머지를 상쇄하기 때문에 변동성이 줄어들게 된다! 

## Efficient Frontier
앞에서 얘기한 것처럼 target return을 만족하는 portfolio를 가질 때 조합하는 방법은 경우의 수가 많다. 그ㅡ 중에서 minimum risk를 찾는게 목표이다. return이 커지면 risk도 커지게 될 것이다. 근데 이게 정비례한 관계가 아닌데 이 관계를 나타내는 것이 efficient frontier이다. 중요한 3개의 점이 있는데 가장 높은 return은 가장 높은 return을 주는 1개 equity로 구성된다. lowest risk portfolio는 positive return이 아닐 수도 있다. middle은 highest, lowest 사이고 이 때 sharpe ratio가 최대가 된다. 

## How Optimizer Works
- 구성 요소
  - variable 정의: equity 가중치
  - constraints 정의: minimum/maximum 가중치 값(모든 가중치의 합은 1, 개별 가중치는 최소 0.1 이상. 이런 것들)
  - optimization criteria 정의: 가중치의 함수로 input으로 위에서 얘기한 input을 받고 output이 나오게 된다. 
  - optimizer algorithm: 가중치 변경해보고 constraint 확인하고 함수 불러서 반복한다. 


## 키워드
Equity: 자본
Arbitrage: 차익 거래 
키워드 사이트 : https://www.investopedia.com/walkthrough/corporate-finance/4/return-risk/expected-return.aspx
## 찾아 볼 것:
  - return 구하는 방법 머신러닝 기법 어떤 것들 적용하고 있는지 알아보기 


