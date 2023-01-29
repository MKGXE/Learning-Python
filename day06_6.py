# 문제1 : 머신러닝을 사용해서 300명이 방문했을 때 판매량을 예측해보세요
import sklearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

원 = pd.read_csv('kyobo.csv', encoding='cp949')

X = 원.iloc[:,:-1].values
y = 원.iloc[:,-1].values

선 = LinearRegression()
선.fit(X, y)

print(선.predict([[300]]),'개')

# 175.6213448개