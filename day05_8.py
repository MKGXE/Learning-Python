# 머신러닝

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

운동시간 = [[1],[2],[3],[4],[5]]
근육량 = [[1],[2],[3],[3.5],[3.7]]

lin = LinearRegression()
# 인공지능 학습 fit(x,y)
lin.fit(운동시간, 근육량)

근육량예측 = lin.predict(운동시간)
print(근육량예측)

plt.scatter(운동시간, 근육량예측, color='green')    # 점 (제공데이터)
plt.plot(운동시간, 근육량, color='')            # 선 (예측값)
plt.show()

print(lin.predict(([2.5])))         # 2.5시간 운동하면 근육량이 얼마일까?