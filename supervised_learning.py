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

print("Model creation")
model = LogisticRegression(random_state=0, solver='lbfgs', max_iter=8000)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)

print("Model training")
model.fit(x_train,y_train)

predictions = model.predict(x_test)
lr_acc_score = metrics.accuracy_score(y_test, predictions)
print("\nAccuracy_score = ", int(lr_acc_score*100), "%")