import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("data.csv")
print("Dataframe head:\n", df.head(), "\n")

df = df.drop('Id', axis=1)

x = df.drop('quality',axis=1)
y = df['quality']
print("x head:\n", x.head(), "\n")
print("y head:\n", y.head(), "\n")


print("Création du model")
model = LogisticRegression(random_state=0, solver='lbfgs', max_iter=100000)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

print("Entraînement du model")
model.fit(x_train,y_train)
print("\n")

predictions = model.predict(x_test)
print("Prediction à partir du jeu de test:")
print('Mean absolute error =', metrics.mean_absolute_error(y_test, predictions))
print('Mean squared error =', metrics.mean_squared_error(y_test, predictions))
print('Root mean squared error =', np.sqrt(metrics.mean_squared_error(y_test, predictions)))