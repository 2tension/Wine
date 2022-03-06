from tkinter import XView
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
df = df.drop('Id', axis=1)

print('Choose two different features of the dataset for the x and y axis :\n- fixed acidity\n- volatile acidity\n- citric acid\n- residual sugar\n- chlorides\n- free sulfur dioxide\n- total sulfur dioxide\n- density\n- pH\n- sulphates\n- alcohol\n- quality\n')
x_value = input("X axis : ")
y_value = input("Y axis : ")

#y_value = input("hoose the parameters on the y axis from fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, quality: ")
range = input("Choose range of point of the dataset between 0 and 1143: ")

if (range and range.isdigit()):
    if (int(range) < 1 or int(range) >= 1144):
        range = '1143'
else:
    range = '1143'

if (x_value and y_value):
    if ((x_value != 'fixed acidity') and (x_value != 'volatile acidity') and (x_value != 'citric acid') and (x_value != 'residual sugar') and (x_value != 'chlorides') and (x_value != 'free sulfur dioxide') and (x_value != 'total sulfur dioxide') and (x_value != 'density') and (x_value != 'pH') and (x_value != 'sulphates') and (x_value != 'quality')):
        x_value = 'alcohol'
    if ((y_value != 'fixed acidity') and (y_value != 'volatile acidity') and (y_value != 'citric acid') and (y_value != 'residual sugar') and (y_value != 'chlorides') and (y_value != 'free sulfur dioxide') and (y_value != 'total sulfur dioxide') and (y_value != 'density') and (y_value != 'pH') and (y_value != 'sulphates') and (y_value != 'alcohol')):
        y_value = 'quality'
    
    sns.regplot(x=x_value, y=y_value, data=df.sample(int(range)), line_kws={"color": "red"}).set(title='Scatter plot and regression line of ' + x_value + ' by ' + y_value)
else:
    df = df.rename(columns={"fixed acidity": "fix acd", "volatile acidity": "vlti acd", "citric acid": "citr acd", "residual sugar": "resid sgr", "chlorides": "chlor", "free sulfur dioxide": "free sf dx", "total sulfur dioxide": "total sf dx", "density": "dens", "sulphates": "sulpha", "alcohol": "alcl", "quality": "qual"})
    scatter_matrix(df.sample(int(range)), figsize=(40,30))
    plt.suptitle('Matrix of scatter plots')

plt.show()
