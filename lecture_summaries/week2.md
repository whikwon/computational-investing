# Week2
## 1. What is a company worth?
### 0) Key Terms and Support Resources
- Intrinsic Value (내재가치)
 - 흔히 말하는 기업의 가치, 내재가치 또는 본질가치, 고유가치, 실질가치와 동의어
 - ex) 콜옵션의 행사가격이 15원이고, 기초자산의 가격이 현재 25원아면, 이 옵션을 행사하는 경우 10원의 이익에서 지급한 프리미엄을 차감한 수익을 얻을 수 있고, 이 떄 내재가치는 10원이 된다.
 - 풋옵션 : 팔 수 있는 권리 / 콜옵션 : 살 수 있는 권리<br><br>
- Capital Assests Pricing Medel (CAPM, 자본자산가격결정모형)
 - capital assest -> 장기 자산, pricing model -> 가격을 결정하는데 사용하는 모델
 - 그러나 실제로 Capital Asset을 계산해 주지 않는다 -> Discount Rate만을 제공
 - Discount rate(할인율) : 현재의 돈과 미래의 돈의 가치를 현재시점으로 바꾸는 기능<br>
 즉, cash flow(미래의 현금흐름)을 할인율을 사용해 present value(현재가치)로 변경

### 1) Intrinsic value : Value of future dividends
- 회사의 가치1 : 회사의 주식 수와 현재 가격을 곱한 것 -> worth(가치)
- 회사의 가치2 : 지불하는 dividends(배당금)을 기준
- book value(장부가치) : 순자산(자본총계), 미래가치를 무시할 때 지금 당장 팔 수 있는 가격. 즉, 권리금이나 프리미엄이 전혀 붙지 않은 가격
- 내재가치 : 정확한 숫자가 아닌 추정치. 즉, 주식채권 이자율이다. 일관성을 입증한 종목의 현재부터 특정기간까지 창출하는 현금을 년수익률로 환산하고 보수적인 시장가치로 계산
 워런 버핏은 내재가치 수익률이 년 12~15% 종목들만 인수
- 시장가치 : 장부가치에 미래가치나 권리금이 붙은 금액, 주로 PER로 표시, 시가총액

### 2) How and Why News Affects Prices

### 3) Fundamental Analysis of Company Value
- company's worth -> effect the price of the stock of that company
- 평가 방법1 : book value(장부가치), 본질적인 회사의 가치
- 평가 방법2 : the value of future value / 이 두 가지를 합친 것이 시장 가치, 시가총액
- 즉, 시가총액이란 현재 가치와 미래 가치를 합한 것을 의미하며, 이것은 기업이 얼마나 대단한 기업인지를 나타내는 하나의 지표가 된다.<br><br>

## 2. Capital Assests Pricing Model
### 1) Capital Assets Pricing Model
- $CAPM : E(R_i)=R_f+\beta_i(E(R_m)-R_f)$
- $E(R_i)$ : i라는 주식을 의미하고, 그냥 하나의 주식을 의미. 원래의 의미는 capital asset으로 주식만을 의미하는 것은 아니지만, 편의상 주식으로 해석
- $R_f$ : Risk-free rate, 투자에 따른 위험이 전혀 없는, 무위험 자산에 투자했을 때의 수익률
- $E(R_m)$ : 시장에 존재하는 모든 자산들을 적절히 포함시켜 포트폴리오를 구성했을 때 예상되는 수익률. Market Portfolio라고 하며, 시장 전체의 평균 수익률, 시장 전체의 예상 수익률
- $\beta_i$ : i라는 주식의 예상 수익률과 시장 전체의 예상 수익률 사이의 상관관계
- Expected Rate of Return = Risk-free Rate + $\beta${Expected Market Return - Risk-free Rate}
- Expected Rate of Return = Risk-free Rate + Risk Premium
- $\beta_i=\frac{Cov(R_i,R_M)}{\sigma^2(R_M)}$ 개별주식i와 시장과의 상관관계를 나타내는 Covariance(공분산), 시장 수익률의 Variance(분산)을 나타낸다

### 2) CAPM : What is Beta?
- 위에서 나타낸 것과 같이 베타의 정의는 위와 같다.
- 시장가격이 두 가지 요인에 의해 결정된다고 가정해 보자. 하나는 시장 전체의 좋고 나쁨, 다른 하나는 시장과는 상관없는 개별 기업 특유의 경영 능력 등이다.
- $R_i=\alpha_i+\beta_iR_m+e_i$ 여기서 $R_m$은 시장 전체적 요인, $e_i$는 개별 기업적 요인이다. 여기서 개별 기업 특유의 요인으로 인한 부분이 없다고 가정하면 예상값은
- $E(R_i)=\alpha_i+\beta_iE(R_m)$ 이 된다. 여기서 CAPM에 의하면
- $E(R_i)=\alpha_i+\beta_i(E(R_m)-R_f)$ 라는 관계가 성립된다. CAPM에서의 베타와 두 번째 수식에서의 베타는 수학적으로 정확하게 일치한다.
- 즉, 직선 관계의 기울기를 구하는 공식은 $Cov(R_i,R_m)/\sigma^2(R_m)$ 으로, CAPM에서 베타의 정의와 정확하게 일치한다.

### 3) How Hedge Funds Use CAPM
- 초과 수익률은 포트폴리오의 베타가 1보다 크면 된다 (베타는 기울기)
- 각 주식의 포트폴리오의 베타와 알파를 알고, 분산 투자를 하면, 시장 수익률을 초과할 수 있는 수익률을 낼 수 있다.