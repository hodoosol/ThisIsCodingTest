### Pandas
# 파이썬에서 데이터 처리를 위해 존재하는 가장 인기있는 라이브러리
# 판다스의 주요 구성 요소
#   1. DataFrame - Column X Rows, 2차원 데이터 셋
#   2. Series - 1개의 column값으로만 구성된 1차원 데이터 셋

# Pandas 시작 - DataFrame 로딩, 기본 API
import pandas as pd
# read_csv()를 이용하여 csv를 DataFrame으로 로딩할 수 있다.
# read_csv() 인자를 콤마(,)가 아닌 다른 분리자로 변경하여 다른 유형의 파일도 로드가 가능하다. (???? 뭔소린지 잘)

titanic_df = pd.read_csv('titanic_train.csv')
print('titanic 변수 type : ', type(titanic_df))

# head() = DataFrame의 맨 앞 일부 데이터만 추출한다.
# index는 column명이 없고, 물리적인 값을 가지고 있다. 그냥 값 그 자체일 뿐.
print(titanic_df.head(5))

print('------------------------------------------')

# DataFrame의 생성
dic1 = {'Name' : ['dasol', 'hodoo', 'haroo'],
         'Year' : [2011, 2016, 2015],
         'Gender' : ['Female', 'Male', 'Female']}

# 딕셔너리를 DataFrame으로 변환
data_df = pd.DataFrame(dic1)
print(data_df)
print('#'*30)

# 새로운 컬럼명을 추가
data_df = pd.DataFrame(dic1, columns=['Name', 'Year', 'Gender', 'Age'])
print(data_df)
print('#'*30)

# 인덱스를 새로운 값으로 할당
data_df = pd.DataFrame(dic1, index=['one', 'two', 'three'])
print(data_df)
print('#'*30)


print('------------------------------------------')


# DataFrame의 컬럼명과 인덱스
print('columns : ',titanic_df.columns)
print('index : ', titanic_df.index)
print('index value : ', titanic_df.index.values)


print('------------------------------------------')


# DataFrame에서 Series 추출 및 DataFrame 필터링 추출
# DataFrame에서 []연산자 내에 한개의 컬럼만 입력하면 Series 객체를 반환
series = titanic_df['Name']
print(series.head(3))
print('## type : ', type(series))

# DataFrame 객체에서 []연산자 내에 여러개의 컬럼을 리스트로 입력하면 그 컬럼들로 구성된 DataFrame 반환
filtered_df = titanic_df[['Name', 'Age']]
print(filtered_df.head(3))
print('## type : ', type(filtered_df))

# DataFrame에서 []연산자 내에 한개의 컬럼을 리스트로 입력하면 한개의 컬럼으로 구성된 DataFrame 반환
one_col_df = titanic_df[['Name']]
print(one_col_df.head(3))
print('## type : ', type(one_col_df))


print('------------------------------------------')


# shape - DataFrame의 행과 열의 크기를 가지고 있는 속성
print('DataFrame의 크기 : ', titanic_df.shape)

# info() - DataFrame 내의 컬럼명, 데이터 타입, Null 건수, 데이터 건수 정보를 제공
print(titanic_df.info())

# describe() - 데이터값들의 평균, 표준편차, 4분위 분포도를 제공, 숫자형 컬럼들에 대해서 해당 정보를 제공
print(titanic_df.describe())

# value_counts() - 동일한 개별 데이터 값이 몇건이 있는지 제공, 즉 개별 데이터값의 분포도를 제공
# 주의할 점은 value_counts()는 Series객체에서만 호출될 수 있으므로
# 반드시 DataFrame을 단일컬럼으로 입력하여 Series로 변환한 뒤 호출해야함
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)

titanic_pclass = titanic_df['Pclass']
print(type(value_counts))


print('------------------------------------------')


# sort_values() by = 정렬컬럼, ascending = True 또는 False로 오름차순/내림차순으로 정렬
print(titanic_df.sort_values(by='Pclass', ascending=False))
print(titanic_df[['Name', 'Age']].sort_values(by='Age'))
print(titanic_df[['Name', 'Age', 'Pclass']].sort_values(by=['Pclass', 'Age']))


print('------------------------------------------')


### DataFrame의 변환, 컬럼 세트 생성/수정, 삭제 및 Index 객체 소개
## DataFrame과 리스트, 딕셔너리, 넘파이 ndarray 상호 변환

# 리스트, ndarray에서 DataFrame 변환
import numpy as np
col_name1 = ['col1']
list1 = [1, 2, 3]

array1 = np.array(list1)
print('array1 shape : ', array1.shape)
df_list1 = pd.DataFrame(list1, columns=col_name1)
print('1차원 리스트로 만든 DataFrame : \n', df_list1)
df_array1 = pd.DataFrame(array1, columns=col_name1)
print('1차원 ndarray로 만든 DataFrame : \n', df_array1)

# 3개의 컬럼명이 필요함
col_name2 = ['col1', 'col2', 'col3']

# 2행x3열 형태의 리스트와 ndarray 생성 한 뒤 이를 DataFrame으로 변환
list2 = [[1, 2, 3],
         [11, 12, 13]]
array2 = np.array(list2)
print('array2 shape : ', array2.shape)
df_list2 = pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 DataFrame : \n', df_list2)
df_array1 = pd.DataFrame(array2, columns=col_name2)
print('1차원 ndarray로 만든 DataFrame : \n', df_array1)


print('------------------------------------------')


# 딕셔너리(dict)에서 DataFrame 변환
# Key는 컬럼명으로 매핑, Value는 리스트 형 또는 ndarray
dict = {'col1' : [1, 11], 'col2' : [2, 22], 'col3' : [3, 33]}
df_dict = pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame : \n', df_dict)

# DataFrame을 ndarray로 변환
array3 = df_dict.values
print('df_dict.values 타입 : ', type(array3), 'df_dict.values shape : ', array3.shape)
print(array3)

# DataFrame을 리스트와 딕셔너리로 변환
# DataFrame을 리스트로 변환
list3 = df_dict.values.tolist()
print('df_dict.values.tolist() 타입 : ', type(list3))
print(list3)

# DataFrame을 딕셔너리로 변환
dict3 = df_dict.to_dict('list')
print('\n df_dict.to_dict 타입 : ', type(dict3))
print(dict3)


# DataFrame의 컬럼 데이터 셋 Access
# DataFrame의 컬럼 데이터 세트 생성과 수정은 [] 연산자를 이용하여 쉽게 할 수 있다.
# 새로운 컬럼에 값을 할당하려면 DataFrame[] 내에 새로운 컬럼명을 입력하고 값을 할당해주면 된다.
titanic_df['Age_0'] = 0
print(titanic_df.head(3))
titanic_df['Age_by_10'] = titanic_df['Age'] * 10
titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch'] + 1
print(titanic_df.head(3))

# 기존 컬럼에 값을 업데이트 하려면 해당 컬럼에 업데이트 값을 그대로 지정하면 된다.
titanic_df['Age_by_10'] = titanic_df['Age_by_10'] + 100
print(titanic_df.head(3))


print('------------------------------------------')


## DataFrame 데이터 삭제
# axis에 따른 삭제
titanic_drop_df = titanic_df.drop('Age_0', axis=1)
print(titanic_drop_df.head(3))

# DataFrame의 drop()
# DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
# inplace = False가 default인데, 이것은 원본 DataFrame은 유지하고, 드롭된 DataFrame을 새롭게 객체 변수로 받는 것이다.
# 이 경우 drop() 호출을 한 DataFrame은 아무런 영향이 없으며 drop() 호출의 결과가 해당 해당 컬럼이 drop된 DataFrame이다.
# 원본 DataFrame에 드롭된 결과를 적용할 경우에는 inplace = True를 적용
# inplace = True는 titanic_df = titanic_df.drop('Age_0', axis=1, inplace=False)와 같다.

# 여러개 컬럼을 삭제하려면 drop의 인자로 삭제 컬럼들을 리스트로 입력한다.
drop_result = titanic_df.drop(['Age_0', 'Age_by_10', 'Family_No'], axis=1, inplace=True)
print('inplace=True로 drop 후 반환된 값 : ', drop_result)
print(titanic_df.head(3))

# axis = 0 일 경우 drop()은 row 방향으로 데이터를 삭제한다.
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 15)
print('#### before axis 0 drop ####')
print(titanic_df.head(3))

titanic_df.drop([0, 1, 2], axis=0, inplace = True)
print('#### after axis 0 drop ####')
print(titanic_df.head(3))


print('------------------------------------------')


## Index
# 판다스의 Index 객체는 RDBMS의 PK(Primary Key)와 유사하게 DataFrame, Series의 레코드를 고유하게 식별하는 객체이다.
# DataFrame, Series에서 Index 객체만 추출하려면 DataFrame.index 또는 Series.index 속성을 이용

# 원본파일 재 로딩
titanic_df = pd.read_csv('titanic_train.csv')
# Index 객체 추출
indexes = titanic_df.index
print(indexes)
# Index 객체를 실제 값 array로 변환
print('Index 객체 array 값 : \n', indexes.values)

# Index는 0에서 시작해 증가하는 형태, 1차원 데이터이다.
# []를 이용하여 임의로 Index의 값을 변경할 수는 없다.

# Series 객체에 연산 함수를 적용할 때 Index는 연산에서 제외된다. 오직 식별용으로만 사용됨 !
series_fair = titanic_df['Fare']
print(series_fair.head(5))

print('fare series max 값 : ', series_fair.max())
print('fare series sum 값 : ', series_fair.sum())
print('sum() fair series : ', sum(series_fair))
print('fare series + 3 \n: ', (series_fair + 3).head(3))

# DataFrame 및 Series에 reset_index() 메소드를 수행하면 인덱스를 새롭게 연속 숫자형으로 할당하며
# 기존인덱스는 'index'라는 새로운 컬럼 명으로 추가됨.
titanic_reset_df = titanic_df.reset_index(inplace=False)
print(titanic_reset_df.head(3))

print('### before reset_index ###')
value_counts = titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입 : ', type(value_counts))

new_value_counts = value_counts.reset_index(inplace=False)
print('### after reset_index ###')
print(new_value_counts)
print('new_value_counts 객체 변수 타입 : ', type(new_value_counts))



print('------------------------------------------')



### 데이터 셀렉션 및 필터링
## [] - 컬럼 기반 필터링 또는 불린 인덱싱 필터링 제공
# DataFrame 바로 뒤에 있는 '[]'안에는 컬럼명 문자(또는 컬럼명의 리스트 객체) 또는 인덱스로 변환 가능한 표현식이다.
titanic_df = pd.read_csv('titanic_train.csv')
print('단일 컬럼 데이터 추출 : \n', titanic_df['Pclass'].head(3))
print('\n여러 컬럼들의 데이터 추출 : \n', titanic_df[['Survived', 'Pclass']].head(3))
# print('[] 안에 숫자 index는 KeyError 오류 발생 : \n', titanic_df[0])

# [] 내에 숫자 값을 입력할 경우 오류가 발생한다고 했는데, pandas의 index형태로 변환가능한 표현식은 입력 가능
# 가령 titanic_df의 처음 2개 데이터를 추출하고자 titanic_df[0:2]와 같은 슬라이싱을 사용하였다면 원하는 결과 반환해 줌.
titanic_df[0:2] # But, 그렇게 좋은 방법은 아님.
# 또, [] 내에 조건식을 입력하여 불린 인덱싱을 수행할 수 있으나 컬럼명과 불린 인덱싱으로 범위를 좁혀서 코딩하는 것이 좋다.
print(titanic_df[titanic_df['Pclass'] == 3].head(3))


print('------------------------------------------')


## ix[], iloc[], loc[]  - 명칭/위치 기반 인덱싱을 제공
# 명칭(Label) 기반 인덱싱은 컬럼의 명칭을 기반으로 위치를 지정하는 방식이다.
# 위치(Position) 기반 인덱싱은 0을 출발점으로 하는 가로축, 세로축 좌표 기반의 행과 열 위치를 기반으로 데이터를 지정한다.
# 따라서 행, 열 위치값으로 정수가 입력된다. 행, 열의 위치는 고정되어 있어, 데이터가 삭제되어도 바뀌지 않는다.

# ix[] 연산자 - 명칭 기반과 위치 기반 인덱싱 모두를 제공.
# but, 둘 다 사용 가능하다보니 오류가 발생하고, 디버깅이 어려워져 사용하지 않는 추세
print(titanic_df.head(3))

# print('컬럼 위치 기반 인덱싱 데이터 추출 : ', titanic_df.ix[0, 2])          (에러발생)
# print('컬럼명 기반 인덱싱 데이터 추출 : ', titanic_df.ix[0, 'Pclass'])      (에러발생)

data = {'Name' : ['dasol', 'hodoo', 'haroo', 'mayo'],
        'Year' : [2011, 2016, 2015, 2015],
        'Gender' : ['Female', 'Male', 'Female', 'Female']}
data_df = pd.DataFrame(data, index=['one', 'two', 'three', 'four'])
print(data_df)

# data_df를 reset_index()로 새로운 숫자형 인덱스를 생성
data_df_reset = data_df.reset_index()
data_df_reset = data_df_reset.rename(columns={'index' : 'old_index'})

# index 값에 1을 더해서 1부터 시작하는 새로운 index값 생성
data_df_reset.index = data_df_reset.index + 1
print(data_df_reset)

# print(data_df_reset.ix[0, 1])      (에러발생)
# print(data_df_reset.ix[1, 1])      (에러발생)

print('------------------------------------------')

# DataFrame iloc[] 연산자 - 위치 기반 인덱싱 제공
print(data_df.head())
print(data_df.iloc[0, 0])
# data_df.iloc[0, 'Name']       (에러발생) -> 정확하게 행, 열의 위치 인덱스를 입력해야함.
# data_df.iloc['one', 0]        (에러발생)

print('------------------------------------------')

# DataFrame loc[] 연산자 - 명칭 기반 인덱싱 제공
print(data_df.loc['one', 'Name'])
print(data_df_reset.loc[1, 'Name'])

# print(data_df_reset.loc[0, 'Name'])  # (에러발생) -> 0이라는 객체를 찾지 못함.
print('위치기반 iloc slicing\n', data_df.iloc[0:1, 0], '\n')
print('명칭기반 loc slicing\n', data_df.loc['one' : 'two', 'Name'], '\n')
print(data_df_reset.loc[1:2, 'Name'])


print('------------------------------------------')


## 불린 인덱싱 ☆☆ - 조건식에 따른 필터링을 제공
titanic_df = pd.read_csv('titanic_train.csv')
titanic_boolean = titanic_df[titanic_df['Age'] > 60] # 나이가 60세 이상인 데이터 찾아줘.
print(type(titanic_boolean))

print(titanic_df['Age'] > 60)  # 조건 값이 반환
var1 = titanic_df['Age'] > 60  # var1의 타입은 불린 Series 객체
print(type(var1))

print(titanic_df[titanic_df['Age'] > 60][['Name', 'Age']].head(3))
print(titanic_df[['Name', 'Age']][titanic_df['Age'] > 60].head(3))
print(titanic_df.loc[titanic_df['Age'] > 60, ['Name', 'Age']].head(3))

# 논리 연산자로 결합된 조건식도 불린 인덱싱으로 적용 가능
titanic_df[(titanic_df['Age'] > 60) & (titanic_df['Pclass'] == 1) & (titanic_df['Sex'] == 'female')]

# 조건식은 변수로도 할당 가능, 복잡한 조건식은 변수로 할당하여 가독성 향상
cond1 = titanic_df['Age'] > 60
cond2 = titanic_df['Pclass'] == 1
cond3 = titanic_df['Sex'] == 'female'
print(titanic_df[cond1 & cond2 & cond3])

print(titanic_df.shape)


print('------------------------------------------')


### 판다스 Aggregation함수와 Group by 수행
## Aggregation함수
# sum(), max(), min(), count() 등의 함수는 DataFrame/Series에서 집합연산을 수행.
# DataFrame의 경우 DataFrame에서 바로 Aggregation을 호출할 경우 모튼 컬럼에 해당 aggregation 적용
# panads의 DataFrame은 2차원 객체이므로 axis 0, 1 가짐을 유의
# sum(axis=0) -> 하나의 컬럼의 모든 값을 더함, sum(axis=1) -> 모든 열의 값을 더함

# Aggregation 함수 수행
print(titanic_df.count())

# 특정 컬럼들로 Aggregation 함수 수행
print(titanic_df[['Age', 'Fare']].mean())
print(titanic_df[['Age', 'Fare']].mean(axis=0))
print(titanic_df[['Age', 'Fare']].sum())
print(titanic_df[['Age', 'Fare']].count())

print('------------------------------------------')

## Group by
# groupby() 메소드는 by 인자로 group by 하려는 컬럼명을 입력 받으면 DataFramegroupBy 객체를 반환
# 이렇게 반환된 DataFramegroupBy 객체에 aggregation 함수를 수행
titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))
print(titanic_groupby)

# DataFrameGroupBy 객체에 aggregation 함수를 호출하여 group by 수행
# Index는 groupby() 안의 인자로 생성된다.
titanic_groupby = titanic_df.groupby('Pclass').count()
print(titanic_groupby)

print(type(titanic_groupby))
print(titanic_groupby.shape)
print(titanic_groupby.index)

titanic_groupby = titanic_df.groupby(by='Pclass')[['PassengerId', 'Survived']].count()
print(titanic_groupby)

titanic_df[['Pclass', 'PassengerId', 'Survived']].groupby('Pclass').count()
print(titanic_groupby)

titanic_df.groupby('Pclass')['Pclass'].count()
print(titanic_df['Pclass'].value_counts())

print('------------------------------------------')

# RDBM의 group by는 select 절에 여러개의 aggregation 함수를 적용할 수 있음
# Select max(Age), min(Age) from titanic_table group by Pclass
# 판다스는 여러개의 aggregation 함수를 적용할 수 있도록 agg()함수를 별도로 제공함
print(titanic_df.groupby('Pclass')['Age'].agg([max, min]))

# 딕셔너리를 이용하여 다양한 aggregation 함수를 적용
agg_format = {'Age' : 'max', 'SibSp' : 'sum', 'Fare' : 'mean'}
print(titanic_df.groupby('Pclass').agg(agg_format))


print('------------------------------------------')


### 판다스 결손 데이터 처리하기
## isna() : DataFrame의 isna() 메소드는 주어진 컬럼값들이 NaN인지 True/False 값을 반환(NaN이면 True)
print(titanic_df.isna().head(3))

# 아래와 같이 isna() 반환 결과에 sum()을 호출하여 컬럼별로 NaN 건수를 구할수 있다.
print(titanic_df.isna().sum())

## fillna() : Missing 데이터를 주어진 인자로 대체
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('Good')
print(titanic_df.head(3))

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())  # 이제 Null값은 하나도 없다.


print('------------------------------------------')


### 판다스 람다식 적용하여 데이터 가공하기
# 판다스는 apply 함수에 람다식을 결합해 DataFrame이나 Series의 레코드 별로 데이터를 가공해준다.
# 판다스의 경우 컬럼에 일괄적으로 데이터를 가공하는 것이 속도 면에서 더 빠르나,
# 복잡한 데이터 가공이 필요할 경우 어쩔 수 없이 apply lambda를 이용한다.

titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name', 'Name_len']].head(3))

titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age', 'Child_Adult']].head(10))

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else ('Adult' if x <= 60 else 'Elderly'))
print(titanic_df['Age_cat'].value_counts())

# 람다식에서 if - else 구문이 복잡해지면 번거로우니 함수식으로 만들어도 된다.
def get_category(age) :
    cat = ''
    if age <= 5 : cat = 'Baby'
    elif age <= 12 : cat = 'Child'
    elif age <= 18 : cat = 'Teenager'
    elif age <= 25 : cat = 'Student'
    elif age <= 35 : cat = 'Young Adult'
    elif age <= 60 : cat = 'Adult'
    else : cat = 'Elderly'

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
print(titanic_df[['Age', 'Age_cat']].head())


"""
판다스 Summary
 2차원 데이터 핸들링을 위해서는 넘파이보단 판다스 사용하기.
 판다스는 매우 편리하고 다양한 데이터 처리 API를 제공하지만 다 알기엔 많은 시간과 노력 필요
 따라서 핵심 사항에 집중하고, 문제에 부딪힐 때 마다 찾아서 해결하는 것이 좋다.
"""

"""
1장 Summary
 머신러닝이란 애플리케이션을 수정하지 않고도 데이터를 기반으로 패턴을 학습하고 결과를 추론하는 알고리즘의 통칭
 파이썬 기반의 머신러닝을 익히기 위해서는 다양한 지원 패키지도 학습해야 한다.
"""