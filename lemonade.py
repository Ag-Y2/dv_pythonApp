import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

#filepath = "https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv"
filepath = './testlist.csv'#"./lemonade.csv"
data = pd.read_csv(filepath)
data.head()

independ = data[['가격']]#data[['온도']]
depend = data[['판매량']]
print(independ.shape, depend.shape)

x = tf.keras.layers.Input(shape=[1])
y = tf.keras.layers.Dense(1)(x)
model = tf.keras.models.Model(x , y)
model.compile(loss="mse")
#model.compile('sgd', 'mse')

'''
shape=[1] ==> 독립변수
Dense==> 종속 변수
compile==> 모델이 확인할 방법

epochs ==> 학습 횟수
    -loss 가 0에 가까움면 좋은것
verbose ==> 학습 도중 표시안함
'''


model.fit(independ, depend, epochs=10000, verbose=0)
#model.fit(independ, depend, epochs=10)
print(model.predict(independ).flatten())
prediction = model.predict(independ)
#print(prediction)

#prediction = model.predict([[30]])
#print("when 30 : ", prediction)
xysis = []


for x in prediction:
    xysis.append(x)



#x-sis should price and y-yis should tge prediction value
plt.plot(independ, xysis, 'ro')
#plt.axis([0, 6, 0, 20])
plt.show()



'''
프라이빗 쿠폰 기획전에서 활용법

기존 가격에서 적용되는 쿠폰 크기에 따른 변수 처리
가격별 확인 쿠폰 활용 사례


'''