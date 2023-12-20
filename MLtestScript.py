import numpy as np
from sklearn.preprocessing import Imputer
import pandas as pd

'''
data1 = np.array([34.1, 32.2, 40.0, 31.8, 36.6, 45.9, 35.8, 35.2, 18.3, 25.9, 32.9, 53.0, 34.5, 42.7, 35.1, 37.2, 43.2, 48.2, 41.7, 47.9, 24.1, 39.3, 39.8]).reshape((-1,1))
data2 = np.array([34.1, 32.2, 40.0, 31.8, 36.6, 45.9, 35.8, 35.2, 18.3, 25.9, 32.9, 53.0, 34.5, 42.7, 35.1, 37.2, 43.2, 48.2, 41.7, 47.9, 24.1, 39.3, 37.8])

model = LinearRegression()
model.fit(data1,data2)
pred = model.predict(data1)
print(pred)
'''
file = open('weatherData2.txt','r')
dataFrame = pd.read_csv(file)
print(dataFrame.shape)
