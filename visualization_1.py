import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Wine.csv")

x_value = input("Choose one feature of the dataset (between fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, quality): ")
range = input("Choose range of point of the dataset (between 0 and 1143): ")

if ((x_value != 'fixed acidity') and (x_value != 'volatile acidity') and (x_value != 'citric acid') and (x_value != 'residual sugar') and (x_value != 'chlorides') and (x_value != 'free sulfur dioxide') and (x_value != 'total sulfur dioxide') and (x_value != 'density') and (x_value != 'pH') and (x_value != 'sulphates') and (x_value != 'quality')):
    x_value = 'density'

if (range and range.isdigit()):
    if (int(range) < 0 or int(range) >= 1144):
        range = '1143'
else:
    range = '1143'

fig, ax = plt.subplots(figsize=(9, 6))
sns.scatterplot(x=x_value, y='quality', data=df.sample(int(range)))

plt.show()
