import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
print(df.head(), '\n')

df.dropna(inplace=True)
df.drop('Id', axis=1, inplace=True)

print(df.head(), '\n')
print(df.isna().sum(), '\n')

fig, ax = plt.subplots(figsize=(15, 15))
sns.heatmap(df.corr(), cmap='magma', annot=True)
ax.set_title('Correlation Matrix of Dataset', fontsize=15)

plt.show()

for i in df.columns:
    mean = sum(df[i] / len(df[i]))
    standard_deviation = np.std(df[i])
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)

    df[i].plot(kind='hist')
    plt.title(f'{i} histogram plot: $\mu = {round(mean, 2)}$ $\sigma = {round(standard_deviation, 2)}$ \n')
    plt.xlabel(f'{i}')
    plt.savefig(f'analysis_plots/{i} histogram plot.pdf')
    
plt.close()