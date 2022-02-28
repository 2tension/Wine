import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Wine.csv")
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
    plt.figure(figsize=(10, 4))
    plt.title(f'{i} hist plot')
    plt.subplot(1, 3, 1)
    df[i].plot(kind='hist')
    plt.xlabel(f'{i}')
    plt.savefig(f'analysis_plots/{i} hist plot.pdf')
    
plt.close()
print(df.describe())