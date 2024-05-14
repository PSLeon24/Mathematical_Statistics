ㅎ# Mathematical_Statistics
데이터 사이언스를 위한 수리통계학 학습 노트

# 1. 확률과 분포
### 1.1. Probability
- 확률 변수(random variable): 확률적으로 값이 결정되는 변수(e.g., 동전 던지기의 예에서 동전을 던졌을 때 윗면이 무엇인지)
- 확률 분포(probability distribution): 확률 변수가 취할 수 있는 모든 값과 그 값들이 나타날 확률을 나열한 표/그림/함수식(e.g., 동전 던지기의 예에서 윗면이 앞면(뒷면)일 때 확률이 얼마인지 알려주는 함수)
- 확률(probability): 어떤 사건이 일어났을 지에 대한 가능성을 0~1 사이의 숫자로 표현한 값(e.g., 동전 던지기의 예에서 확률 변수가 앞면(뒷면)일 가능성의 값)
- 사건(event): 확률변수에서 관측될 수 있는 결과의 집합
- 표본 공간(sample space): 가능한 모든 사건의 집합
- P(X = head) = p에서 P는 확률 분포, X는 확률 변수, head는 사건, p는 확률

### 1.2. Probability distribution
- 균일 분포(Uniform distribution): 사건이 무엇인지와 무관하게 확률이 동일한 분포
- 베르누이 분포(Bernoulli distribution): 확률 변수 X의 값이 2개(0 or 1)인 분포 → 두 가지인 시도, 예컨대 생존/사망이나 정품/불량 등의 수많은 문제를 다룰 수 있음
  - <img width="392" alt="스크린샷 2024-05-09 오전 9 27 33" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/9fc2194b-100a-444d-a380-2394de9c1300">
  - "P(X = x)": 확률 변수 X가 값 x(예를 들어, 1)를 가질 때의 확률
  - ";" 뒤의 p는 p가 모수(parameter)로 주어진다는 의미
    - 확률 분포에서의 모수(parameter): 확률 분포의 특성을 나타내는 수(e.g., 베르누이 분포에서 동전에서 앞면이 나올 확률, 정규 분포에서는 평균과 분산, 통계학에서 모수는 항상 그리스 문자로 표기)
  - "{": x의 여러 가지 케이스들을 나눠서 보는 것
  - 성질
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/bebe6271-7c2e-45ff-a587-cbce8e863b79)

- 지지역(support): 확률 분포에서 확률 값이 0이 아닌 확률 변수 x의 집합(즉, 발생 가능한 사건(예: head, tail)은 지지역으로 바뀔 수 있으며, 발생 불가능한 사건(예: 동전을 던졌는데 head도 tail도 아닌 동전이 세워진다던지)은 불가능한 사건이니까 확률이 0이며, 따라서 지지역으로 바뀔 수 없음)

### 1.3. pmf vs pdf
- 이산형 확률 분포(Discrete probability distribution): 확률 변수 X의 값이 이산적(discrete)일 때의 확률 분포(e.g., 베르누이 분포)
  - 이산표본공간에서 정의된 확률 변수의 값이 유한하거나 countably infinite
  - 종류: 베르누이 분포, 이항 분포, 기하 분포, 다항 분포, 포아송 분포
- 연속형 확률 분포(Continuous probability distribution): 확률 변수 X의 값이 연속적(continuous)일 때의 확률 분포(e.g., 연속 균등 분포)
  - 확률 변수의 값이 무한개이며 셀 수 없음
  - 연속형 확률 변수의 확률 값을 구할 때는 면적을 구하기 위해 적분을 이용(e.g., 아래는 연속 균등 분포를 푸는 수식)
  - 종류: 균등분포, 정규분포, 카이제곱 분포, t-분포, F 분포
  - 이항분포의 확률 질량 함수(pmf)
    - <img width="400" alt="스크린샷 2024-05-09 오전 9 44 26" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/d3339e40-1459-4dca-9aa8-e66deac260b4">

- 확률 질량 함수(Probability mass function): 이산형 확률 분포에 대한 확률 함수, 이산확률변수 X의 값 x1, ..., xn의 각 확률을 대응
- 확률 밀도 함수(Probability density function): 연속형 확률 분포에 대한 확률 함수, 확률 변수 X가 어떤 구간 [l, u]의 모든 값을 취하고 이 구간에서의 함수 f(x)
  - 확률 밀도 함수에서는 X가 주어진 범위(표본 공간) 내에서 임의의 실수 값을 가짐

### 1.4. Normal distribution
- 정규분포(Normal distribuiton): 연속 확률 분포의 하나로, 자연적으로 흔히 볼 수 있는 분포. 가우스 분포
  - 특징: 대칭(symmetric)이며 종 모양의 형태(bell shape)
- 중심극한정리(CLT, Central Limit Theorem): 표본 평균의 분포가 정규분포를 따른다는 정리
- 표준 정규 분포(Z-distribution, Standard normal distribution): 평균이 0이고 표준 편차가 1인 정규분포
  - 모든 정규 분포는 표준 정규 분포로 변환(transformation)될 수 있음.
  - 임의의 정규 분포를 표준 정규 분포로 변환하는 과정
    1. 평균이 μ이고 분산이 σ²인 정규 분포를 다음과 같이 표시: X ~ Normal(μ, σ²)
    2. Y(Z-score) = (X - μ) / σ
    3. Y ~ Normal(0, 1)

### 1.5. Binomial distribution
- 이항 분포(Binomial distribution): 1회의 시도에서 성공/실패를 다루었던 분포인 베르누이 분포를 n번의 시도로 확장한 분포. 즉, n회의 베르누이 시행을 합한 것
  - <img width="481" alt="스크린샷 2024-05-09 오전 11 10 12" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/f69988f6-e76e-41a1-8edd-7422a00af3e3">
  - 첫번째 항: 조합(combination), 두번째 항: 성공 횟수 x, 세번째 항: 실패 횟수 n-x번
  - 이항 분포의 평균: np, 분산: np(1-p)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/fe9169ee-52f9-4823-8710-0a74d48a87fc)
    - n이 고정되었을 때 p가 0과 가깝거나 1에 가까우면 그 분산 값이 커지고, p가 0.5일 때 분산은 최소가 됨

- 다항 분포(Mulitinomial distribution): 이항 분포(0 or 1) → 다항 분포(n1, n2, n3, ...)

- 모수 공간(parameter space): 모수가 의미 있는 값을 가질 수 있는 공간
  - 이항 분포에서의 모수 공간: n은 1보다 크거나 같은 정수, p는 0과 1 사이의 실수
  - 정규분포에서의 모수 공간:  평균은 임의의 실수값, 분산은 0보다 큰 실수

### 1.6. Poisson distribution
- 포아송 분포(Poisson distribution): '단위 시간/공간 내 사건의 발생 횟수'에 대한 확률 분포(e.g., 1시간에 몇 건의 구매가 발생했는지)
  - <img width="354" alt="스크린샷 2024-05-09 오전 11 25 00" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/4239e79d-c65d-42bb-b632-b6d07930821d">
  - 특징: 평균과 분산 모두 모수인 λ로 동일
    - 실제 데이터로부터 포아송 관련 모델링을 할 때는 과산포인 경우가 많은데 이를 해결하기 위해 음이항 분포(negative binomial)을 사용하기도 함
    - 과산포(overdispersion): 평균보다 분산이 큰 경우
  - 포아송 분포는 이항 분포로부터 유도될 수도 있음. 이항 분포에서 n이 무척 크고 p가 낮아지면 λ = np인 포아송으로 근사가 가능
    - 대표적인 예시: 책의 한 페이지에서 나타날 수 있는 오탈자의 수
    - 수많은 글자(n이 크고) 중 오탈자의 수는 무척 적음(p가 작음). 포아송 관점에서는 각 페이지를 단위 공간으로 보고 페이지 당 오탈자의 수가 포아송을 따른다고 볼 수 있음

### 1.7. Standardization and Normalization
- 스케일링(Scaling): 숫자의 스케일을 조절하는 것으로 대표적인 방법으로 표준화와 정규화가 있으며, 데이터의 분포 형태는 바꾸지 않음
- 표준화(Standardization): 평균을 0, 표준편차를 1로 맞춰주는 변환
  - <img width="100" alt="스크린샷 2024-05-09 오전 11 35 21" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/0fa9a0a0-c0f9-4c23-8c78-d5ab2158821e">

- 정규화(Normalization): 최솟값을 0, 최댓값을 1로 맞춰주는 변환
  - <img width="163" alt="스크린샷 2024-05-09 오전 11 35 33" src="https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/0c24dc70-0136-49f1-97aa-2801d0a810f0">

### 1.8. Approximation

### 1.9. Negative binomial distribution


# 2. 기댓값, 그리고 더 많은 분포
# 3. 점 추정과 구간 추정
# 4. 가설 검정: t test와 ANOVA


# Practical Statistics for Data Scientists
## New 1. 탐색적 데이터 분석 (practice/Practice EDA~.ipynb)
- 탐색적 데이터 분석(exploratory data analysis): 요약통계량(평균, 중앙값, 분위수 등)과 간단한 도표(상자그림, 산점도 등)등을 통해 복잡한 데이터의 경향성을 파악하는 것
- 데이터의 종류
  - 수치형, 연속형, 정수형(이산), 범주형, 이진, 순서형
- 테이블 데이터: 흔히 행과 열로 이루어져서 데이터를 표현하는 방법 ~ 판다스에서는 데이터 프레임 구조(feature는 각 열, record는 각 행을 나타냄)
  - features are used to predict outcome.
- 1. 위치 추정
  - 데이터의 값들이 어디쯤에 위치하는지(중심경향성)를 나타내는 추정값을 확인하는 과정
  - 평균, 가중평균, 중앙값, 백분위수, 가중 중앙값, 절사평균, 극단값(outlier) 등을 확인 + robust
    - 가중 평균(weighted mean): 가중치를 곱한 값의 총합을 가중치의 총합으로 나눈 값
    - 가중 중앙값(weighted median): 데이터를 정렬한 후, 각 가중치 값을 위에서부터 더할 때, 총합의 중간이 위치하는 데이터 값, wquantiles 패키지의 median() 함수를 사용해서 구할 수 있음
    - 절사평균(trimmed mean): 정해진 개수의 극단값을 제외한 나머지 값들의 평균 ~ scipy.stats에 있는 trim_mean 함수 사용
- 2. 변이 추정
  - 데이터 값이 얼마나 밀집해 있는지 혹은 퍼져 있는지를 나타내는 산포도를 확인하는 과정, 일반적으로 편차를 기본으로 함(e.g., 평균절대편차)
  - 편차, 분산, 표준편차(분산의 제곱근), 평균절대편차(Manhattan norm, L1 norm), 중앙값의 중위절대편차(MAD), 순서통계량, 범위, 백분위수, 사분위범위(IQR)을 확인
    - 평균절대편차(mean absolute deviation): 평균과의 편차의 절댓값의 평균(편차 자체의 평균을 구하게 되면 음의 편차가 양의 편차를 상쇄시키므로 바람직하지 않음)
    - 중앙값의 중위절대편차(median absolute deviation from the median): 중간값과의 편차의 절댓값의 중간값, statsmodels 패키지의 strong.scale.mad() 함수 사용
    - 순서통계량(순위, order statistics): 정렬(순위) 데이터를 나타내는 통계량, 가장 기본이 되는 측도가 범위(range)
    - 범위(range): 최댓값과 최솟값의 차이(최댓값 - 최솟값), 범위는 극단값에 매우 민감하여 데이터의 변이를 측정하는데 크게 유용하지 않음 ~ 사분위범위(IQR)를 활용해 극복
  - 분산, 표준편차, 평균절대편차 모두 극단값에 로버스트하지 않음 → robust한 변이 추정값으로 중간값의 중위절대편차(MAD)가 있음
    - 분산과 표준편차는 제곱편차를 사용하기 때문에 특히 극단값에 민감함
- 3. 데이터 분포 탐색
  - 주로 데이터가 전반적으로 어떻게 분포하고 있는지를 알아보는 과정
  - 상자그림(boxplot), 도수분포표(frequency table), 히스토그램(histogram), 밀도 그림(density plot)를 활용하여 시각화
    - 밀도 그림(density plot): 히스토그램을 부드러운 곡선으로 나타낸 그림으로 커널밀도추정을 주로 사용
- 4. 이진 데이터와 범주 데이터 탐색
     - 이진 데이터의 경우는 1과 같이 중요한 범주의 비율이 어느 정도 되는지 알아보면 됨 - 막대 그래프(count plot or bar plot) 활용하여 시각화 가능
     - 범주 데이터는 보통 비율로 요약할 수 있고 아래와 같이 2가지의 경우로 주로 분류해서 구함
       - 범주가 몇 개 안 되는 경우: 막대 그래프(count plot or bar plot), 파이차트(pie chart)
         - 막대 그래프는 히스토그램과 유사하며, 통계학자나 데이터 시각화 전문가들은 파이차트가 시각적으로 효과적이지 않다는 이유로 잘 사용하지 않음
       - 범주가 많은 경우: 최빈값(mode), 기댓값(expected value)
- 5. 상관관계
  - 예측값과 목푯값의 상관관계를 조사하는 것으로써 이변량분석의 중요한 방법, 상관행렬이나 산점도를 활용해서 파악
    - X가 큰 값을 가지면 Y도 큰 값을 갖고, X가 작은 값을 가지면 Y도 작은 값을 가지는 경우 상관관계를 갖는다고 함
  - 상관계수(correlation coefficient): 수치적 변수들 간에 어떤 관계가 있는지를 나타내기 위해 사용되는 측정량(-1 ~ +1)
    - 절댓값이 1에 가까울수록 상관관계가 높으며 0에 가까울수록 상관관계가 없다는 뜻(+ 양의 상관관계, 음의 상관관계)
  - 상관행렬(correlation matrix): 행과 열이 변수들을 의미하는 표, 각 셀은 그 행과 열에 해당하는 변수들 간의 상관관계를 의미
  - 산점도(scatterplot): x축과 y축이 서로 다른 두 개의 변수를 나타내는 도표
- 6. 이변량분석 & 다변량분석
  - 육각형 구간(hexagonal binning), 등고선도(contour plot), 히트맵(heatmap), 분할표(contingency table), 바이올린 도표(violin plot)
  - 육각형 구간: 데이터를 점으로 표시하는 대신 데이터를 육각형 모양의 구간들로 나누고 각 구간에 포함된 기록값의 개수에 따라 색깔을 표시한 도표(pandas 패키지의 hexbin() 함수를 사용하여 시각화 가능)
    - 산점도는 데이터의 개수가 적을 때는 괜찮지만 수많은 행을 나타내기에는 부적절한데 이를 대체하기 위해 사용되는 방법
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/840efce2-0d5f-41a6-8f2f-6accbe7c5d58)

  - 등고선도: 산점도 위에 등고선을 사용한 도표로써 등고선의 '꼭대기'쪽으로 갈수록 밀도가 높아짐(seaborn 패키지의 kdeplot() 함수를 이용해 시각화 가능)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/14928a90-c21b-4c94-8782-d54d1667ef50)

  - 분할표: 두 범주형 변수를 요약하는 데 효과적인 방법으로, 범주별 빈도수를 기록한 표
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/bb1e1ddc-4ca3-4ad3-bc80-32d875712b47)

  - 바이올린 도표: 상자그림을 보완한 형태로, y축을 따라 밀도추정 결과를 동시에 시각화(seaborn 패키지의 violinplot() 함수를 이용해 시각화 가능)
    - 장점: 상자그림에서는 보이지 않는 데이터의 분포를 볼 수 있음(다만, 극단값과 이상값은 상자그림이 더 명확하게 보여줌)
    - ![image](https://github.com/PSLeon24/Mathematical_Statistics/assets/59058869/eb3535c2-4a89-4528-bb52-db226627b4c9)
