import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

print('Choose three different features of the dataset (between fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol)')
first_value = input("First parameter : ")
second_value = input("Second parameter : ")
third_value = input("Third parameter : ")

range = input("\nChoose range of point of the dataset (between 0 and 1143): ")

if ((first_value != 'fixed acidity') and (first_value != 'volatile acidity') and (first_value != 'citric acid') and (first_value != 'residual sugar') and (first_value != 'chlorides') and (first_value != 'free sulfur dioxide') and (first_value != 'total sulfur dioxide') and (first_value != 'density') and (first_value != 'pH') and (first_value != 'sulphates') and (first_value != 'quality')):
    first_value = 'fixed acidity'


if (second_value and ((second_value == 'fixed acidity') or (second_value == 'volatile acidity') or (second_value == 'citric acid') or (second_value == 'residual sugar') or (second_value == 'chlorides') or (second_value == 'free sulfur dioxide') or (second_value == 'total sulfur dioxide') or (second_value == 'density') or (second_value == 'pH') or (second_value == 'sulphates') or (second_value == 'quality'))):
    if (second_value == first_value):
        second_value = 'residual sugar'
else:
    second_value = 'residual sugar'


if (third_value and ((third_value == 'fixed acidity') or (third_value == 'volatile acidity') or (third_value == 'citric acid') or (third_value == 'residual sugar') or (third_value == 'chlorides') or (third_value == 'free sulfur dioxide') or (third_value == 'total sulfur dioxide') or (third_value == 'density') or (third_value == 'pH') or (third_value == 'sulphates') or (third_value == 'quality'))):
    if ((third_value == first_value) or (third_value == second_value)):
        third_value = 'alcohol'
else:
    third_value = 'alcohol'


if (range and range.isdigit()):
    if (int(range) < 0 or int(range) >= 1144):
        range = '1143'
else:
    range = '1143'


df_pc = pd.DataFrame()
df_pc[first_value] = df[first_value].copy()
df_pc[second_value] = df[second_value].copy()
df_pc[third_value] = df[third_value].copy()
df_pc["quality"] = df["quality"].copy()

fig = px.parallel_coordinates(df_pc.sample(int(range)), color='quality',
                    color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=5.5)

fig.show()
