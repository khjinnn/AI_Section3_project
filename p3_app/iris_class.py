import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

df = pd.read_csv('iris.csv', names=['A', 'B', 'C', 'D', 'iris'], header=None) # 헤더를 초기화해주고, 헤더의 이름 넣어줌

X = df.drop('iris', axis=1) # 특성데이터 
y = df['iris'] # 타겟 데이터

X = np.array(X)
y = np.array(y)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# 전체 데이터를 훈련세트와 테스트세트로 나눔 (8:2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = SVC(kernel='linear').fit(X_train, y_train)

pickle.dump(model, open('iris.pkl','wb'))

# test
pred = model.predict([[5.9, 3. , 5.1, 1.8]])
print(pred)