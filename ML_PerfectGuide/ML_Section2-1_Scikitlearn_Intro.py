"""
사이킷런 소개
 쉽고, 파이썬스러운 API를 제공
 머신러닝을 위한 매우 다양한 알고리즘과 편리한 프레임워크, API를 제공
 오랜 기간 실전환경에서 검증됐으며 매우 많은 환경에서 사용됨
 Numpy와 Scipy 기반 위에서 구축된 라이브러리


 피처(속성)?
   데이터 세트의 일반 속성,머신러닝은 2차원 이상의 데이터에서 많이 사용되므로
   타겟값을 제외한 나머지 속성을 모두 피처로 지칭
 레이블, 클래스, 타겟값(결정값)?
   타겟값은 지도 학습시 데이터의 학습을 위해 주어지는 정답 데이터
   지도 학습 중 분류의 경우에는 이 결정값을 레이블 또는 클래스로 지칭


사이킷런을 이용한 붓꽃 데이터 분류
  붓꽃 데이터 피처 - Sepal length, Sepal width, Petal length, Petal width
  붓꽃 데이터 품종(레이블) - Setosa, Vesicolor, Virginica

지도학습 - 분류
 분류(Classification)은 대표적인 지도학습 방법이다.
 지도학습은 학습을 위한 다양한 피처와 분류 결정값인 레이블 데이터로 모델을 학습한 뒤,
 별도의 테스트 데이터 세트에서 미지의 레이블을 예측한다.
 즉, 지도학습은 명확한 정답이 주어진 데이터를 먼저 학습한 뒤 미지의 정답을 예측하는 방식.
 이 때 학습을 위해 주어진 데이터 세트를 학습 데이터 세트,
 머신러닝 모델의 예측 성능을 평가하기 위해 별도로 주어진 데이터세트를 테스트 데이터 세트로 지칭한다.

붓꽃 데이터 분류 예측 프로세스
 데이터 세트 분리 : 데이터를 학습 데이터와 테스트 데이터로 분리
 모델 학습 : 학습 데이터를 기반으로 ML 알고리즘을 적용해 모델을 학습시킴
 예측 수행 : 학습된 ML 모델을 이용해 테스트 데이터의 분류를 예측
 평가 : 예측된 결과값과 테스트 데이터의 실제 결과값을 비교해 ML 모델 성능을 평가

"""

## 사이킷런을 이용하여 붓꽃(Iris) 데이터 품종 예측하기
# 사이킷런 버전 확인
import sklearn
print(sklearn.__version__)

# 붓꽃 예측을 위한 사이킷런 필요 모듈 로딩
from sklearn.datasets import load_iris               # 데이터 로딩
from sklearn.tree import DecisionTreeClassifier      # 결정트리 알고리즘
from sklearn.model_selection import train_test_split # 학습데이터 - 테스트 데이터 분리

# 데이터 세트를 로딩
import pandas as pd

# 붓꽃 데이터 세트를 로딩
iris = load_iris()
# iris.data는 Iris 데이터 세트에서 피처만으로 된 데이터를 numpy로 갖고 있다.
iris_data = iris.data
# iris.target은 붓꽃 데이터 세트에서 레이블(결정 값) 데이터를 numpy로 갖고 있다.
iris_label = iris.target
print('iris target 값 : ', iris_label)
print('iris target 명 : ', iris.target_names)
# 붓꽃 데이터 세트를 자세히 보기 위해 DataFrame으로 변환한다.
iris_df = pd.DataFrame(data = iris_data, columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df.head(3))

# 학습 데이터와 테스트 데이터 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label,
                                                     test_size=0.2, random_state=11)
# 학습 데이터 세트로 학습(Train) 수행
# DecisionTreeClassifier 객체 생성
df_clf = DecisionTreeClassifier(random_state=11)
# 학습수행
df_clf.fit(X_train, y_train)
# 테스트 데이터 세트로 예측(Predict) 수행
# 학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행
pred = df_clf.predict(X_test)
print(pred)

# 예측 정확도 평가
from sklearn.metrics import accuracy_score
print('예측 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))










