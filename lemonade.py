import tensorflow as tf
import pandas as pd

#filepath = "https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv"
filepath = "./lemonade.csv"
data = pd.read_csv(filepath)
data.head()

independ = data[['온도']]
depend = data[['판매량']]
print(independ.shape, depend.shape)

x = tf.keras.layers.Input(shape=[1])
y = tf.keras.layers.Dense(1)(x)
model = tf.keras.models.Model(x , y)
model.compile(loss="mse")

'''
shape=[1] ==> 독립변수
Dense==> 종속 변수
compile==> 모델이 확슬할 방법

epochs ==> 학습 횟수
    -loss 가 0에 가까움면 좋은것
verbose ==> 학습 도중 표시안함
'''

model.fit(independ, depend, epochs=10000, verbose=0)
model.fit(independ, depend, epochs=10)


prediction = model.predict(independ)
print(prediction)