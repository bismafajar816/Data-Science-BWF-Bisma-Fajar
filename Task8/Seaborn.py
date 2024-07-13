import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].apply(lambda x: iris.target_names[x])

print(df.head())

# Scatter plot
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df)
plt.title('Sepal Length vs Sepal Width')
plt.show()

# Pair plot
sns.pairplot(df, hue='species')
plt.show()

# Box plot
sns.boxplot(x='species', y='petal length (cm)', data=df)
plt.title('Petal Length by Species')
plt.show()

# Violin plot
sns.violinplot(x='species', y='petal width (cm)', data=df)
plt.title('Petal Width by Species')
plt.show()

# Heatmap
corr = df.iloc[:, :-1].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
