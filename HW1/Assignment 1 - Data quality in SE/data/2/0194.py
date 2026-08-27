from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from matplotlib import pyplot as plt
import numpy as np

#1. 정제된 데이터 세팅

x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])

x_pred = np.array([11,12,13])

#2. 모델 구성
model = Sequential()
model.add(Dense(3, input_dim=1, activation='relu'))
model.add(Dense(5))
model.add(Dense(1))

#3. 데이터 모델 훈련
model.compile(loss='mse', optimizer='adam'
, metrics=['mae','acc']
)
hist = model.fit(x_train, y_train, epochs=500, batch_size=1 )

#loss, acc = model.evaluate(x, y)
#4.평가
loss = model.evaluate(x_train, y_train, batch_size=1)

#print('acc:',acc)
print('loss: ',loss)

y_predict = model.predict(x_pred)
print(y_predict)

#######

# for y in y_predict:
#     print(round(float(y)))

##evaluate에서 가장 중요한 것은 loss 이다. metrics는 보조지표를 추가하는 파라미터 이다 즉 ['보조지표1', '보조지표2'] + evaluate에 반환값 추가