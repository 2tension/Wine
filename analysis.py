import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Wine.csv")
print(df.head(), '\n')

df.dropna(inplace=True)
df.drop('Id', axis=1, inplace=True)

print(df.head(), '\n')
print(df.isna().sum(), '\n')

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df.corr(), cmap='magma', annot=True, ax=ax)
ax.set_title('Correlation Matrix of Dataset', fontsize=15)

plt.show()