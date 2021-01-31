### ndarray : N차원(Dimension) 배열(Array) 객체

## Numpy ndarray 개요
# Numpy 모듈의 array() 함수로 생성, 인자로 파이썬 list 또는 ndarray 입력
# import numpy as np
# array1 = np.array([1,2,3])                # 1차원 array
# array2 = np.array([[1,2,3,], [4,5,6]])    # 2차원 array(내포된 array)

# [1 2 3] = 1차원, shape = (3,)
# [[1 2 3] = 2차원, shape = (2, 3)
#  [4 5 6]]

# ndarray의 shape는 ndarray.shape으로, 차원은 ndarray.ndim으로 알 수 있다.
# ndarray내의 데이터 값은 숫자, 문자열, 불 값 모두 가능
# but, 하나의 ndarray 안의 데이터 속성은 동일해야함.
# ndarray 내의 데이터 타입은 ndarray.dtype으로 확인 가능

# astype()의 인자에 ndarray 넣어서 형 변환.
# 대용량 데이터를 다룰 때 메모리를 절약하기 위해 사용
# 0, 1, 2와 같이 크지 않은 범위의 숫자를 위해서 64bit float형을 쓰기보다는
# 8, 16 bit의 integer형으로 변환하면 메모리 절약 가능

# axis
# axis0 = 행, axis1 = 열, axis2 = 3차원 배열


### ndarray 생성 np.array()
import numpy as np
list1 = [1, 2, 3]
print('list1 : ', list1)
print('list1 type : ', type(list1))

array1 = np.array(list1)
print('array1 : ', array1)
print('array1 type : ', type(array1))


print('-----------------------')


# ndarray의 형태(shape)와 차원
array1 = np.array([1, 2, 3])
print('array1 type : ', type(array1))
print('array1 array 형태 : ', array1.shape)

array2 = np.array([[1, 2, 3],
                   [2, 3, 4]])
print('array2 type : ', type(array2))
print('array2 array 형태 : ', array2.shape)

array3 = np.array([[1, 2, 3]])
print('array3 type : ', type(array3))
print('array3 array 형태 : ', array3.shape)

print('array1 : {:0}차원, array2 : {:1}차원, array3 : {:2}차원'.format(array1.ndim, array2.ndim, array3.ndim))


print('-----------------------')


# ndarray 데이터값 타입
list1 = [1, 2, 3]
print(type(list1))

array1 = np.array(list1)
print(type(array1))
print(array1, array1.dtype)

print('-----------------------')

list2 = [1, 2, 'test']    # <U11 ?
array2 = np.array(list2)
print(array2, array2.dtype)

list3 = [1, 2, 3.0]
array3 = np.array(list3)
print(array3, array3.dtype)


print('-----------------------')


# astype()을 통한 타입 변환
array_int = np.array([1, 2, 3])
array_float = array_int.astype('float64')
print(array_float, array_float.dtype)

array_int1 = array_float.astype('int32')
print(array_int1, array_int1.dtype)

array_float1 = np.array([1.1, 2.1, 3.1])
array_int2 = array_float1.astype('int32')
print(array_int2, array_int2.dtype)


print('-----------------------')


# ndarray에서 axis 기반의 연산함수 수행
array2 = np.array([[1, 2, 3], [2, 3, 4]])
print(array2.sum())         # 모든 원소 다 더하기
print(array2.sum(axis=0))   # 행방향으로 더하기
print(array2.sum(axis=1))   # 열방향으로 더하기


print('-----------------------')


### 넘파이 배열 ndarray 초기화 방법과 ndarray차원과 크기를 변경하는 reshape()의 이해
# np.arange(10) => [0 1 2 3 4 5 6 7 8 9]
# np.zeros((3,2), dtype='int32') => [[0 0] [0 0] [0 0]]
# np.ones((3,2)) => [[1. 1.] [1. 1.] [1. 1.]] 디폴트는 실수

# reshape() 원하는 대로 재배열
# reshpae(-1, 5)와 같이 -1을 인자로 부여하면 -1에 해당하는 axis의 크기는
# 가변적이되 -1이 아닌 인자값에 해당하는 axis 크기는 인자값으로 고정하여 reshape한다.
# reshape(-1,) = 1차원으로 변환


# ndarray를 편리하게 생성하기 - arange, zeros, ones
sequence_array = np.arange(10)
print(sequence_array)
print(sequence_array.dtype, sequence_array.shape)

zero_array = np.zeros((3,2), dtype='int32')
print(zero_array)
print(zero_array.dtype, zero_array.shape)

one_array = np.ones((3,2))
print(one_array)
print(one_array.dtype, one_array.shape)


print('-----------------------')


# ndarray의 shape을 변경하는 reshape()
array1 = np.arange(10)
print('array1 : \n', array1)

array2 = array1.reshape(2, 5)
print('array2 : \n', array2)

array3 = array1.reshape(5, 2)
print('array3 : \n', array3)

# 변환할 수 없는 shape구조를 입력하면 오류 발생
# ex) array1.reshape(4, 3)


print('-----------------------')


# reshape()에 -1 인자값을 부여하여 특정 차원으로 고정된 가변적인 ndarray형태 변환
array1 = np.arange(10)
print(array1)

# 컬럼 axis 크기는 5에 고정하고 로우 axis 크기를 이에 맞춰 자동으로 변환, 즉 2*5 형태로 변환
array2 = array1.reshape(-1, 5)
print('array2 shape : ', array2.shape)
print('array2 : \n', array2)

# 로우 axis 크기는 5에 고정하고 컬럼 axis 크기는 이에 맞춰 자동으로 변환, 즉 5*2 형태로 변환
array3 = array1.reshape(5, -1)
print('array3 shape : ', array3.shape)
print('array3 : \n', array3)


print('-----------------------')


# reshape()은 (-1, 1), (-1, )와 같은 형태로 주로 사용됨
# 1차원 ndarray를 2차원으로 또는 2차원 ndarray를 1차원으로 변환 시 사용
array1 = np.arange(5)

# 1차원 ndarray를 2차원으로 변환하되, 컬럼 axis 크기는 반드시 1이여야함
array2d_1 = array1.reshape(-1, 1)
print('array2d_1 shape : ', array2d_1.shape)
print('array2d_1 : \n', array2d_1)

# 2차원 ndarray를 1차원으로 변환
array1d = array2d_1.reshape(-1, )
print('array1d shape : ', array1d.shape)
print('array1d : \n', array1d)

# -1을 적용하여도 변환이 불가능한 형태로의 변환을 요구할 경우 오류 발생
# array1 = np.arange(10)
# array4 = array1.reshape(-1, 4)

# -1값은 반드시 1개의 인자만 입력해야함
# array1.reshape(-1, -1)



print('-----------------------')


### ndarray의 인덱싱을 통한 데이터 세트 선택하기 _ 1
# 1. 특정 위치의 단일값 추출 - 원하는 위치의 인덱스 값을 지정하면 해당 위치의 데이터가 반환됨
# 2. 슬라이싱 - 연속된 인덱스 상의 ndarray를 추출, : 기호 사이에 시작 인덱스와 종료 인덱스를
#              표시하면 시작 인덱스에서 종료 인덱스-1 위치에 있는 인덱스를 반환
# 3. 팬시 인덱싱 - 일정한 인덱싱 집합을 리스트 또는 ndarray형태로 지정해 해당 위치에 있는 ndarray 반환
# 4. 불린 인덱싱 - 특정 조건에 해당하는지 여부인 True/False 값 인덱싱 집합을 기반으로 True에 해당하는 인덱스 반환


# 1. 단일값 추출
# ndarray는 axis를 기준으로 0부터 시작하는 위치 인덱스 값을 가짐, 마이너스가 인덱스로 사용되면 맨 뒤에서부터 지정

# 2. 슬라이싱
# array[:] = 전체, array[3:] = 3번 인덱스부터 끝까지
# array[:3] = 처음부터 3번 인덱스 전까지 !!!, 2번 인덱스까지 ! = array[0:3]

# 3. 팬시 인덱싱
# array1[[2, 4, 7]] = 2, 4, 7번 인덱스의 값
# 이 세개 잘 모르겠다...
#   1. array2d[[0,1], 2]
#   2. array2d[[0,1], 0:2]
#   3. array2d[[0,1]]

# 4. 불린 인덱싱
# 불린 인덱싱 사용 X
array1d = np.arange(start=1, stop=10)
target = []

for i in range(0, 9) :
    if array1d[i] > 5 :
        target.append(array1d[i])

array_selected = np.array(target)
print(array_selected)

# 불린 인덱싱 사용 O
array1[array1 > 5]


print('-----------------------')


### ndarray의 인덱싱을 통한 데이터 세트 선택하기 _ 2
# 1. 특정 위치의 단일값 추출
# 1에서부터 9까지의 1차원 ndarray 생성
array1 = np.arange(start=1, stop=10)
print('array1 : ', array1)

# 인덱스는 0부터 시작하므로 array1[2]는 3번째 인덱스의 데이터값을 의미
value = array1[2]
print('value : ', value)
print(type(value))

print('맨 뒤의 값 : ', array1[-1], ', 맨 뒤에서 두번째 값 : ', array1[-2])

array1[0] = 9
array1[8] = 0
print('array1 : ', array1)


print('-----------------------')


array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)

print('(row=0, col=0) index 가리키는 값 : ', array2d[0,0])
print('(row=0, col=1) index 가리키는 값 : ', array2d[0,1])
print('(row=1, col=0) index 가리키는 값 : ', array2d[1,0])
print('(row=2, col=2) index 가리키는 값 : ', array2d[2,2])


print('-----------------------')


# 2. 슬라이싱
array1 = np.arange(start=1, stop=10)
print(array1)
array3 = array1[0:3]
print(array3)
print(type(array3))

array1 = np.arange(start=1, stop=10)
array4 = array1[:3]
print(array4)
array5 = array1[3:]
print(array5)
array6 = array1[:]
print(array6)

print('-----------------------')

array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print('array2d : \n', array2d)
# 슬라이싱 어렵다 . . .
print('array2d[0:2, 0:2] \n', array2d[0:2, 0:2])
print('array2d[1:3, 0:3] \n', array2d[1:3, 0:3])
print('array2d[1:3, :] \n', array2d[1:3, :])
print('array2d[:, :] \n', array2d[:, :])
print('array2d[:2, 1:] \n', array2d[:2, 1:])
print('array2d[:2, 0] \n', array2d[:2, 0])


print('-----------------------')


# 3. 팬시 인덱싱
array1d = np.arange(start=1, stop=10)
array2d = array1d.reshape(3, 3)
print(array2d)

array3 = array2d[[0,1], 2]
print('array2d[[0,1], 2] => ', array3.tolist())

array4 = array2d[[0,2], 0:2]
print('array2d[[0,2], 0:2] => ', array4.tolist())

array5 = array2d[[0,1]]
print('array2d[[0,1]] => ', array5.tolist())


print('-----------------------')


# 4. 불린 인덱싱
array1d = np.arange(start=1, stop=10)
print(array1d)

print(array1d > 5)
var1 = array1d > 5
print('var1 : ', var1)
print(type(var1))

# [ ] 안에 array1d > 5 불린 인덱싱 적용
print(array1d)
array3 = array1d[array1d > 5]
print('array1d > 5 불린 인덱싱 결과 값 : ', array3)

boolean_indexes = np.array([False, False, False, False, False, True, True, True, True])
array3 = array1d[boolean_indexes]
print('불린 인덱스로 필터링 결과 : ', array3)

indexes = np.array([5, 6, 7, 8])
array4 = array1d[ indexes ]
print('일반 인덱스로 필터링 결과 : ', array4)


print('-----------------------')


### 넘파이 ndarray의 정렬과 선형대수 연산
# 행열의 정렬 - sort(), argsort()
# np.sort() : 원 행렬은 그대로 유지한 채 원 행렬의 정렬된 행렬을 반환
# ndarray.sort() : 원 행렬 자체를 정렬한 형태로 변환, 반환 값은 None
# 기본적으로 오름차순 정렬
# 내림차순으로 정렬하기 위해서는 [::-1] 적용
# argsort() : 정렬한 행렬의 원본 행렬 인덱스!!!를 반환

# 선형대수 연산
# 행렬 내적 - np.dot(A, B)
# 전치 행렬 - np.transpose(A)

org_array = np.array([3, 1, 9, 5])
print('원본 행렬 : ', org_array)

#np.sort()로 정렬
sort_array1 = np.sort(org_array)
print('np.sort() 호출 후 반환된 정렬 행렬 : ', sort_array1)
print('np.sort() 호출 후 원본 행렬 : ', org_array)

# ndarray.sort()로 정렬
sort_array2 = org_array.sort()
org_array.sort()
print('org_array.sort() 호출 후 반환된 정렬 행렬 : ', sort_array2)
print('org_array.sort() 호출 후 원본 행렬 : ', org_array)

sort_array1_desc = np.sort(org_array[::1])
print('내림차순으로 정렬 : ', sort_array1_desc)

array2d = np.array([[8, 12],
                    [7, 1]])
sort_array2d_axis0 = np.sort(array2d, axis=0)
print('로우 방향으로 정렬 : \n ', sort_array2d_axis0)
sort_array2d_axis1 = np.sort(array2d, axis=1)
print('컬럼 방향으로 정렬 : \n ', sort_array2d_axis1)


print('-----------------------')


# argsort
org_array = np.array([3, 1, 9, 5])
print(np.sort(org_array))
sort_indices = np.argsort(org_array)
print(type(sort_indices))
print('행렬 정렬 시 원본 행렬의 인덱스 : ', sort_indices)

org_array = np.array([3, 1, 9, 5])
print(np.sort(org_array)[::-1])
sort_indices_desc = np.argsort(org_array)[::1]
print('행렬 내림차순 정렬 시 원본 행렬의 인덱스 : ', sort_indices_desc)

print('-----------------------')

name_array = np.array(['Jogn', 'Mike', 'Sarah', 'Kate', 'Samuel'])
score_array = np.array([78, 95, 84, 98, 88])

# score_array의 정렬된 값에 해당하는 원본 행렬 위치 인덱스를 반환하고 이를 이용하여 name_array에서 name 값 추출.
sort_indices = np.argsort(score_array)
print('sort indices : ', sort_indices)

name_array_sort = name_array[sort_indices]
score_array_sort = score_array[sort_indices]
print(name_array_sort)
print(score_array_sort)


print('-----------------------')


# 행렬 내적
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

dot_product = np.dot(A, B)
print('행렬 내적 결과 : \n', dot_product)

# 전치 행렬
A = np.array([[1, 2],
              [3, 4]])
tarnspose_mat = np.transpose(A)
print('A의 전치 행렬 : \n ', tarnspose_mat)


# Numpy Summary
# 넘파이 API는 매우 넓은 범위를 다루므로, 핵심 개념 위주로 숙지하는 것이 좋다.
# 판다스에 비해 친절한 API를 제공하지 않으므로, 2차원의 데이터라면 판다스가 더 효율적이다.