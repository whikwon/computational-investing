## Summary
- [Jensen's alpha](##ja)
- [Back testing](##bt)

## Jensen's Alpha <a name="ja"></a>
- performance를 측정하는 지표로 활용된다.
- CAPM의 수식으로 부터 나오는 개념이다.
	- $\mathbb{E}(R_i) = R_f + \beta_i (\mathbb{E}(R_m) - R_f)$은 CAPM을 정의하는 식이다.
	- CAPM은 index(market)과 portfolio 간의 관계를 나타내는 식으로 beta에 따라 risk/return이 결정된다는 내용이다. 
	- CAPM은 **expectation**이 취해지기 때문에 alpha에 대한 정보가 고려되지 않는다. CAPM은 어느 정도 risk를 감수했을 때 얻어야 하는 risk adjusted return에 관한 식으로 생각할 수 있다.  
	- beta는 market과 portpolio(혹은 단일 security)의 return 간의 공분산을 통해 구한다. 
- Risk adjusted return보다 실제 얻는 return이 크냐 작냐에 따라서 alpha 값이 정해지며 큰 경우 **positive alpha** 라고 한다. 
	- CAPM 식에서 expectation을 삭제했을 때 상수(alpha)항이 생기게 되고 이에 따라서 각 사건에 대한 return 값이 변할 수 있다. 
	- alpha 값은 투자자의 능력을 나타낸다고 볼 수 있다. 
	- alpha는 $R_i = R_f + B_i * (R_m - R_f) + \alpha$의 식을 통해 구한다. 
	
## Back Testing <a name="bt"></a>
- 과거의 데이터를 활용해서 back testing 할 때의 유의점에 대해 설명한다. 
- 과거 특정 시점에 이벤트로 인해 performance가 큰 영향을 받을 수 있으므로 이를 잘 고려 해야 한다. (예로, dotcom boom 시기에 IT 관련 주는 엄청난 주가 상승이 있었다.) 
- Data mining fallacy: 단순히 운이 좋아서 performance가 좋아보이게 나타날 수 있다. 
- Overfitting: 과거 데이터를 전부 외워버려서 performance가 좋아보이긴 하나 일반적인 상황에 대해서 최적화되지 못해서 현재/미래 데이터에 대한 performance는 나쁜 경우를 의미한다. 
- back testing은 실제 과거에 돌아갔다고 가정하고 매도/매수를 알고리즘에 맞게 진행한다. 과거 데이터는 survivor's bias가 없어야하며 매도/매수는 각 날짜에 volume 내에서 진행이 된다. 
	- quantopian에서 back testing이 쉽게 가능하다. 

### Reference
- https://www.investopedia.com/terms/a/alpha.asp
- https://en.wikipedia.org/wiki/Jensen%27s_alpha 
