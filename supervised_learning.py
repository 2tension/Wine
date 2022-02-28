import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("Wine.csv")
print("Dataframe head:\n", df.head(), "\n")

df = df.drop('Id', axis=1)

x = df.drop('quality',axis=1)
y = df['quality']
print("x head:\n", x.head(), "\n")
print("y head:\n", y.head(), "\n")

model = LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)
model.fit(x_train,y_train)

predictions = model.predict(x_test)

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))