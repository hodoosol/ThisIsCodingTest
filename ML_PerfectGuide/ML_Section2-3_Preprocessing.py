### 데이터 전처리(Preprocessing)
# 데이터 클렌징
# 결손값 처리(Null/NaN 처리)
# 데이터 인코딩(레이블, 원-핫 인코딩)
# 데이터 스케일링
# 이상치 제거
# Feature 선택, 추출 및 가공


### 데이터 인코딩
# 머신러닝 알고리즘은 문자열 데이터 속성을 입력받지 않으며 모든 데이터는 숫자형으로 표현되어야 한다.
# 문자형 카테고리형 속성은 모두 숫자값으로 변환/인코딩되어야 한다.

## 레이블(Label) 인코딩
# 문자형으로 된 값을 숫자로 인코딩 . . . ㄱㄴㄷ순으로 생성되는 듯
from sklearn.preprocessing import LabelEncoder
items = ['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

# LabelEncoder를 객체로 생성한 후, fit()과 transform()으로 labe인코딩 수행
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
print('인코딩 변환값 : ', labels)
print('인코딩 클래스 : ', encoder.classes_)
print('디코딩 원본값 : ', encoder.inverse_transform([4, 5, 2, 0, 1, 1, 3, 3]))


print('----------------------------------')


## 원-핫(One-Hot) 인코딩
# 레이블 인코딩한 피처 값의 유형에 따라 새로운 피처를 추가해
# 고유 값에 해당하는 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방식이다.
from sklearn.preprocessing import  OneHotEncoder
import numpy as np

items = ['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']
# 먼저 숫자값으로 변환을 위해 LabelEncoder로 변환
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)

# 2차원 데이터로 변환
labels = labels.reshape(-1, 1)

# 원-핫 인코딩을 적용
oh_encoder = OneHotEncoder()
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)

print('원-핫 인코딩 데이터')
print(oh_labels.toarray())
print('원-핫 인코딩 데이터 차원')
print(oh_labels.shape)


print('----------------------------------')


# 판다스 get_dummies()를 이용한 원-핫 인코딩 - pd.get_dummies(DataFrame)
import pandas as pd
df = pd.DataFrame({'item' : ['TV', '냉장고', '전자렌지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']})
print(df)

print(pd.get_dummies(df))


print('----------------------------------')


### 피처 스케일링과 정규화
# 표준화 : 데이터의 피처 각각의 평균이 0이고 분산이 1인 가우시안 정규 분포를 가진 값으로 변환하는 것
# 정규화 : 서로 다른 피처의 크기를 통일하기 위해 크기를 변환해주는 개념

## StadardScaler - 평균이 0이고, 분산이 1인 정규 분포 형태로 변환
from sklearn.datasets import load_iris
import pandas as pd
# 붓꽃 데이터 세트를 로딩하고 DataFrame으로 변환
iris = load_iris()
iris_data = iris.data
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names)

print('feature들의 평균 값')
print(iris_df.mean())
print('\nfeature들의 분산 값')
print(iris_df.var())


from sklearn.preprocessing import StandardScaler

# StandardScaler 객체 생성
scaler = StandardScaler()
# StandardScaler로 데이터 세트 변환. fit()과 transform() 호출
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

# transform()시 scale 변환된 데이터 세트가 numpy ndarray로 반환되어 이를 DataFrame으로 변환
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)

print('\nfeature들의 평균 값')
print(iris_df_scaled.mean())
print('\nfeature들의 분산 값')
print(iris_df_scaled.var())


print('----------------------------------')


## MinMaxScaler - 데이터 값을 0과 1사이의 범위 값으로 변환(음수 값이 있으면 -1에서 1값으로 변환)
from sklearn.preprocessing import MinMaxScaler

# MinMaxScaler 객체 생성
scaler = MinMaxScaler()
# MinMaxScaler로 데이터세트 변환. fit()과 transform() 호출
scaler.fit(iris_df)
iris_scaled = scaler.transform(iris_df)

# transform()시 scale 변환된 데이터 세트가 numpy ndarray로 반환되어 이를 DataFrame으로 변환
iris_df_scaled = pd.DataFrame(data=iris_scaled, columns=iris.feature_names)
print('\nfeature들의 최소 값')
print(iris_df_scaled.min())
print('\nfeature들의 최대 값')
print(iris_df_scaled.max())



