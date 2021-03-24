### 결정 트리
from sklearn.tree import DecisionTreeClassifier
from  sklearn.model_selection import train_test_split
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# 생성
dt_clf = DecisionTreeClassifier(random_state=156)
# 데이터 로딩, 학습과 테스트 데이터 세트로 분리
train_df = pd.read_csv('./workout_train_features.csv')
train_labels_df = pd.read_csv('./workout_train_labels.csv')
test_df = pd.read_csv('./workout_test_features.csv')
submission_df = pd.read_csv('./sample_submission.csv')

train_data = train_df.groupby('id').agg
X_train, X_test, y_train, y_test = train_test_split(train_data.data, train_data.target, test_size = 0.2)


### 랜덤 포레스트
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")



print()