# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Section 9.1: A Brief Matplotlib API Primer

# Figures and Subplots
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Colors, Markers, and Line Styles
fig, ax = plt.subplots()
ax.plot(x, y, color='r', linestyle='--', marker='o')
ax.set_title('Styled Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Ticks, Labels, and Legends
fig, ax = plt.subplots()
ax.plot(x, y, label='Sine Wave')
ax.set_xticks([0, 2, 4, 6, 8, 10])
ax.set_xticklabels(['zero', 'two', 'four', 'six', 'eight', 'ten'])
ax.legend()
ax.set_title('Plot with Custom Ticks and Legend')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Annotations and Drawing on a Subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.annotate('Max Value', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.set_title('Plot with Annotations')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Saving Plots to File
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Saved Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.savefig('saved_plot.png')
plt.show()

# Matplotlib Configuration
plt.rcParams['figure.figsize'] = (10, 5)
plt.rcParams['axes.titlesize'] = 20
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Configured Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

# Section 9.2: Plotting with Pandas and Seaborn

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].apply(lambda x: iris.target_names[x])

# Line Plots
data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})
data.plot(x='x', y='y', title='Pandas Line Plot')
sns.lineplot(x='x', y='y', data=data)
plt.title('Seaborn Line Plot')
plt.show()

# Bar Plots
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D'],
    'values': [3, 7, 8, 5]
})
data.plot(kind='bar', x='category', y='values', title='Pandas Bar Plot')
sns.barplot(x='category', y='values', data=data)
plt.title('Seaborn Bar Plot')
plt.show()

# Histograms and Density Plots
data = pd.DataFrame({
    'values': np.random.randn(1000)
})
data['values'].plot(kind='hist', bins=30, title='Pandas Histogram')
sns.histplot(data['values'], kde=True)
plt.title('Seaborn Histogram and Density Plot')
plt.show()

# Scatter or Point Plots
data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'category': np.random.choice(['A', 'B'], 100)
})
data.plot(kind='scatter', x='x', y='y', title='Pandas Scatter Plot')
sns.scatterplot(x='x', y='y', hue='category', data=data)
plt.title('Seaborn Scatter Plot')
plt.show()

# Facet Grids and Categorical Data
data = sns.load_dataset('tips')
g = sns.FacetGrid(data, col='time')
g.map(sns.histplot, 'total_bill')
plt.show()
sns.catplot(x='day', y='total_bill', hue='sex', kind='box', data=data)
plt.title('Seaborn Categorical Plot')
plt.show()

# Section 9.3: Other Python Visualization Tools

import plotly.express as px
data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'category': np.random.choice(['A', 'B'], 100)
})
fig = px.scatter(data, x='x', y='y', color='category', title='Plotly Scatter Plot')
fig.show()

# Section 9.4: Conclusion
print("Visualization practice complete.")
