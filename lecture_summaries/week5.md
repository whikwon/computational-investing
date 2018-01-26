## Summary
- [Digging into Data](#dd)

## Digging into Data <a name="dd"></a>
- Bollinger Band: 주식 가격의 이동평균선과 표준편차를 이용하는 변동성 지표이다. 
- 보통 시장 내 개별 주식의 가격이 크게 변하더라도 전체 시장의 가격은 크게 변하지 않는다. 
  - technical indicator로 시장과 다르게 움직이는 주식의 event를 찾아내는 것이 중요하다. 
- 특정 주식에서 발생하는 어떤 사건에 의해 가격 변동이 일어나는 경우 유사 사건을 모아놓고 보면 특정한 움직임을 보이는 경우가 있다. 
- Survivor's bias: 장기간 데이터를 고려했을 때 시장에서 사라진 주식을 고려하지 않게 되면 기대했던 것보다 좋은 결과를 나타낼 수 있다.
  - 위 문제를 해결하기 위해서 과거부터 계속 존재한 주식만을 고려하는 방법이 있다. 
  - 무작위로 portfolio를 구성해서 back-test를 진행하고 여기서 얻는 평균적인 값을 baseline으로 설정하는 방법도 있다. baseline과 우리가 구성한 portfolio의 test 결과와 비교한 경우에 성능을 얻을 수 있다. 


### Actual vs Adjusted Price
- Actual price(close): 마감 종가로 장 중에 변한 가격만 고려한 시장에서 거래되는 가격이다. 
- Adjusted price(Adjusted close): 수정 종가로 주식의 가격에 영향을 미칠수 있는 distribution(유통)을 고려해서 조정한 가격이다. distribution에는 cash dividends, stock dividends, stock splits 등이 포함된다. 쉽게 설명하면 주주들에게 배분된 배당금, 주식 분할을 모두 고려했을 때의 과거로부터 지금까지 얻은 return을 가격으로 책정하는 경우가 많다. 

### Data Sanity and Scrubbing

- 주식 데이터를 사용하기 전에 오류가 없는지 sanity check를 해야 한다. 
  - 주로 발생되는 오류는 데이터 누락(missing, NaN), 분할이 반대로 되는 경우(reverse split), 갑작스럽게 가격이 엄청 낮아지는 경우 등이 있다. 
- reverse split 확인 방법으로는 주식 가격이 50% 이상 감소하거나 200% 이상으로 증가한 경우를 사건과 매칭시켜 비교하는 방법이 있다. 
- 데이터 누락 확인 방법은 NaN이 있는지 확인하면 된다. 
- 데이터에 문제가 있을 수 있기 때문에 확인하는 것이 매우 중요하며 두 곳 이상에서 받은 뒤 비교하면 된다. 

### Keywords
- Bollinger Band(technical indicator)
- Survivorship bias

### Reference
- https://www.investopedia.com/ask/answers/06/adjustedclosingprice.asp
- Coursera - Computational Investing Week 5 

### Keywords
- Adjusted Price 계산 방법?
- Distributions