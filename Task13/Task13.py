#Handling Missing Data
import numpy as np
import pandas as pd
series = pd.Series([7, 'abc', np.nan, 0, None, 8])
print(series)
print(series.isnull())
print(series.dropna())  #drop missing values
print(series.fillna(0))
print(series.ffill()) #forward fill
print(series.bfill()) #backward fill

#Data Transformation
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': ['a', 'b', 'c', 'd', 'e']})
print(data)
print(data.T) #Transpose
print(data.sort_index(axis=1, ascending=False)) #sort by index
print(data.sort_values(by='A')) #sort by values
print(data.rename(columns={'A': 'AA'})) #rename columns
print(data.rename(index={1: 'x'})) #rename index
print(data.replace(1, 100)) #replace values
print(data.replace({1: 100, 2: 200})) #replace values   
print(data.replace({'A': 1, 'B': 'a'}, 100)) #replace values
print(data.replace({'A': 1, 'B': 'a'}, {'A': 100, 'B': 'z'})) #replace values
print(data.replace({'A': {1: 100}, 'B': {'a': 'z'}})) #replace values
print(data.replace({'A': {1: 100, 2: 200}, 'B': {'a': 'z', 'b': 'y'}})) #replace values

#Detecting and filtering outliers
data = pd.DataFrame(np.random.randn(1000, 4))   #generate random data
print(data.describe())

print(data[(np.abs(data) > 3).any(axis=1)]) # filtering outliers
print(data.describe())

