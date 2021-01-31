### 사이킷런의 내장 예제 데이터
from sklearn.datasets import load_iris

iris_data = load_iris()
print(type(iris_data))

keys= iris_data.keys()
print('붓꽃 데이터 세트의 키들 : ', keys)

# 키는 보통 data, target, target_name, feature_names, DESCR로 구성돼 있다. 개별 키는
# data - 피처의 데이터 세트
# target - 분류 시 테이블 값, 회귀일 때는 숫자 결과값 데이터 세트
# target_names - 개별 레이블의 이름
# feature_names - 피처의 이름
# DESCR - 데이터 세트에 대한 설명과 각 피처의 설명을 나타냄

print('\n feature_names의 type : ', type(iris_data.feature_names))
print('feature_names의 shape : ', len(iris_data.feature_names))
print(iris_data.feature_names)

print('\n target_names의 type : ', type(iris_data.target_names))
print('target_names의 shape : ', len(iris_data.target_names))
print(iris_data.target_names)

print('\n data의 type : ', type(iris_data.data))
print('data의 shape : ', iris_data.data.shape)
print(iris_data['data'])

print('\n target의 type : ', type(iris_data.target))
print('target의 shape : ', len(iris_data.target.shape))
print(iris_data.target)


print('----------------------------------')


### Model Seletion 소개 - 학습 데이터와 테스트 데이터
## 학습 데이터세트
# 머신러닝 알고리즘의 학습을 위해 사용
# 데이터의 속성들과 결정값(레이블)값 모두를 가지고 있음
# 학습 데이터를 기반으로 머신러닝 알고리즘이 데이터 속성과 결정값의 패턴을 인지하고 학습


## 테스트 데이터 세트
# 테스트 데이터 세트에서 학습된 머신러닝 알고리즘을 테스트
# 테스트 데이터는 속성 데이터만 머신러닝 알고리즘에 제공하며,
# 머신러닝 알고리즘은 제공된 데이터를 기반으로 결정값을 예측
# 테스트 데이터는 학습 데이터와 별도의 데이터 세트로 제공되어야 함


## 학습 데이터와 테스트 데이터 분리 - train_test_split()
# sklearn.model_selection의 함수

# X_train, X_test, y_train, t_test = train_test_split(iris_data.data, iris_data.target,
#                                                     test_size=0.3, random_state=121)

# test_size = 전체 데이터에서 테스트 데이터 세트 크기를 얼마로 샘플링할 것인가를 결정. default는 0.25
# train_size = 전체 데이터에서 학습용 데이터 세트 크기를 얼마로 샘플링할 것인가를 결정. 잘 사용하지 않음
# shuffle = 데이터를 분리하기 전에 미리 섞을지를 결정. default는 True. 데이터를 분산시켜 좀 더 효율적이게
# random_state = 호출할 때 마다 동일한 학습/테스트용 데이터 세트를 생성하기 위해 주어지는 난수 값     ### Q2. 난수값이 정확히 뭔지 잘 모르겠다 ...
# train_test_split()은 호출 시 무작위로 데이터를 분리하므로
# random_state를 지정하지 않으면 수행할 때 마다 다른 학습/테스트용 데이터를 생성함

## 학습/테스트 데이터 세트 분리하지 않았을 때 -> 예측 정확도 : 1.0 -> Wrong
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
dt_clf = DecisionTreeClassifier()
train_data = iris.data
train_label = iris.target
dt_clf.fit(train_data, train_label)

# 학습 데이터 셋으로 예측 수행
pred = dt_clf.predict(train_data)
print('예측 정확도 : ', accuracy_score(train_label, pred))


## 학습/테스트 데이터 세트 분리 !!!
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

dt_clf = DecisionTreeClassifier()
iris_data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target,
                                                     test_size=0.3, random_state=121)

dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print('예측 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))


print('----------------------------------')


## 넘파이 ndarray뿐 아니라 판다스 DataFrame/Series도 train_test_split()으로 분할 가능
import pandas as pd

iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['target'] = iris_data.target
print(iris_df.head())

ftr_df = iris_df.iloc[:, :-1]
tgt_df = iris_df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(ftr_df, tgt_df,
                                                     test_size=0.3, random_state=121)

print(type(X_train), type(X_test), type(y_train), type(y_test))

dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)
pred = dt_clf.predict(X_test)
print('예측 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))


print('----------------------------------')


### 교차 검증
## K 폴드 교차 검증

# 일반 K 폴드
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import numpy as np

iris = load_iris()
features = iris.data
label = iris.target
dt_clf = DecisionTreeClassifier(random_state=156)

# 5개의 폴드 세트로 분리하는 KFold 객체와 폴드 세트별 정확도를 담을 리스트 객체 생성
kfold = KFold(n_splits=5)
cv_accuracy = []
print('붓꽃 데이터 세트 크기 : ', features.shape[0])

n_iter = 0

# KFold 객체의 split() 호출하면 폴드 별 학습용, 검증용 테스트의 로우 인덱스를 array로 반환
for train_index, test_index in kfold.split(features) :
    # KFold,split()으로 반환된 인덱스를 이용하여 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    # 반복 시 마다 정확도 측정
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n#{0} 교차 검증 정확도 :{1}, 학습 데이터 크기 :{2}, 검증 데이터 크기 :{3}'
          .format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스 :{1}'.format(n_iter, test_index))

    cv_accuracy.append(accuracy)

print('----------------------------------')

# Stratified K 폴드
#  - 불균형한 분포도를 가진 레이블(결정 클래스) 데이터 집합을 위한 K 폴드 방식
#    학습 데이터와 검증 데이터 세트가 가지는 레이블 분포도가 유사하도록 검증 데이터 추출

import pandas as np

iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
print(iris_df['label'].value_counts())

kfold = KFold(n_splits=3)
# kfold.split(X)는 폴드 세트를 5번 반복할 때마다 달라지는 학습/테스트 용 데이터 로우 인덱스 번호 반환
n_iter = 0
for train_index, test_index in kfold.split(iris_df) :
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('## 교차검증 : {0}'.format(n_iter))
    print('학습 레이블 데이터 분포 : \n', label_train.value_counts())
    print('검증 레이블 데이터 분포 : \n', label_test.value_counts())

# BUT !! 이렇게 하면 0, 1, 2 세개의 레이블을 골고루 학습하지 못하고
# 그 중 2개만 학습한 뒤, 나머지 1개로 검증하게 됨 -> Wrong

print('----------------------------------')

# 올바른 예시
# 학습 레이블과 검증 레이블의 분포가 균일하게 설정됨 -> Good
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=3)
n_iter = 0

for train_index, test_index in skf.split(iris_df, iris_df['label']) :
    n_iter += 1
    label_train = iris_df['label'].iloc[train_index]
    label_test = iris_df['label'].iloc[test_index]
    print('## 교차검증 : {0}'.format(n_iter))
    print('학습 레이블 데이터 분포 : \n', label_train.value_counts())
    print('검증 레이블 데이터 분포 : \n', label_test.value_counts())

print('----------------------------------')

import numpy as np

dt_clf = DecisionTreeClassifier(random_state=156)
kfold = StratifiedKFold(n_splits=3)
n_iter = 0
cv_accuracy = []


# StratifiedKFold의 split() 호출시 반드시 레이블 데이터 세트도 추가 입력해야함
for train_index, test_index in kfold.split(features, label) :
    # KFold,split()으로 반환된 인덱스를 이용하여 학습용, 검증용 테스트 데이터 추출
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf.fit(X_train, y_train)
    pred = dt_clf.predict(X_test)
    n_iter += 1
    # 반복 시 마다 정확도 측정
    accuracy = np.round(accuracy_score(y_test, pred), 4)
    train_size = X_train.shape[0]
    test_size = X_test.shape[0]
    print('\n#{0} 교차 검증 정확도 :{1}, 학습 데이터 크기 :{2}, 검증 데이터 크기 :{3}'
          .format(n_iter, accuracy, train_size, test_size))
    print('#{0} 검증 세트 인덱스 :{1}'.format(n_iter, test_index))

    cv_accuracy.append(accuracy)

# 교차 검증별 정확도 및 평균 정확도 계산
print('\n## 교차 검증별 정확도 : ', np.round(cv_accuracy, 4))
print('## 평균 검증 정확도 : ', np.mean(cv_accuracy))


print('----------------------------------')


### cross_val_score()
# 폴드 세트 추출, 학습/예측, 평가를 한번에 수행

from sklearn.tree import  DecisionTreeClassifier
from  sklearn.model_selection import cross_val_score, cross_validate
from sklearn.datasets import load_iris
import numpy as np

iris_data = load_iris()
dt_clf = DecisionTreeClassifier(random_state=156)

data = iris_data.data
label = iris_data.target

# 성능 지표는 정확도(accuracy), 교차 검증 세트는 3개
scores = cross_val_score(dt_clf, data, label, scoring='accuracy', cv=3)
print('교차 검증별 정확도 : ', np.round(scores, 4))
print('평균 검증 정확도 : ', np.round(np.mean(scores), 4))


print('----------------------------------')


## GridSearchCV - 교차 검증과 최적 하이퍼 파라미터 튜닝을 한 번에
# 사이킷런은 GridSearchCV를 이용해 분류나 회귀와 같은 알고리즘에 사용되는 하이퍼 파라미터를
# 순차적으로 입력하면서 편리하게 최적의 파라미터를 도출할 수 있는 방안을 제공함

from sklearn.datasets import load_iris
from sklearn.tree import  DecisionTreeClassifier
from  sklearn.model_selection import GridSearchCV, train_test_split
from  sklearn.metrics import accuracy_score

# 데이터를 로딩하고 학습 데이터와 테스트 데이터 분리
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target,
                                                     test_size=0.2, random_state=121)
dtree = DecisionTreeClassifier()

# parameter들을 dictionary형태로 설정
parameters = {'max_depth' : [1, 2, 3], 'min_samples_split' : [2, 3]}

import pandas as pd
# param_grid의 하이퍼 파라미터들은 3개의 train, test set fold로 나누어서 테스트 수행 설정
# regit = True가 default. True이면 가장 좋은 파라미터 설정으로 재학습 시킴
grid_dtree = GridSearchCV(dtree, param_grid=parameters, cv=3, refit=True, return_train_score=True)

# 붓꽃 Train 데이터로 param_grid의 하이퍼 파라미터들을 순차적으로 학습/평가
grid_dtree.fit(X_train, y_train)

# GridSearchCV 결과는 cv_results_ 라는 딕셔너리로 저장됨, 이를 DataFrame으로 변환
scores_df = pd.DataFrame(grid_dtree.cv_results_)
scores_df[['params', 'mean_test_score', 'rank_test_score',
           'split0_test_score', 'split1_test_score', 'split2_test_score']]
print(scores_df)
print(grid_dtree.cv_results_)

print('----------------------------------')


print('GridSearchCV 최적 파라미터 : ', grid_dtree.best_params_)
print('GridSearchCV 최고 정확도 : {0:.4f}'.format(grid_dtree.best_score_))

# refit=True로 설정된 GridSearchCV 객체가 fit()을 수행시
# 학습이 완료된 Estimator를 내포하고 있으므로 predict()를 통해 예측도 가능
pred = grid_dtree.predict(X_test)
print('테스트 데이터 세트 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))

# GridSearchCV의 refit으로 이미 학습이 된 estimator 반환
estimator = grid_dtree.best_estimator_
print('테스트 데이터 세트 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred)))