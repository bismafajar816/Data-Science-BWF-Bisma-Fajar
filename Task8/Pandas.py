#Pandas Library
import pandas as pd
import numpy as np

#Series
#Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). The axis labels are collectively referred to as the index.
#Creating a Series
#Creating a series from a list
data = [10, 2, 30, 4, -50]
series = pd.Series(data)
print("Series from a list:\n", series)

#Creating a series from a dictionary
data = {'a': 10, 'b': 2, 'c': 30, 'd': 4, 'e': -50}
series = pd.Series(data)
print("Series from a dictionary:\n", series)

print('b' in series)


#Nan Values
#NaN (Not a Number) is a special floating-point value recognized by all systems that use the standard IEEE floating-point representation.
#Creating a series with NaN values


data = [1, 2, np.nan, 4, np.nan, 6]
s = pd.Series(data)

print("Not a number\n", s.isna())    # Detects NaN values
print("Detects Null\n", s.isnull())  # Equivalent to isna()

print("Detect number\n",s.notna())    # Detects non-NaN values
print("Detects not null",s.notnull())  # Equivalent to notna()
print("Drops not a number values \n ",s.dropna())  # Drops NaN values

print("Replaces NaN with 0\n",s.fillna(0))  # Replaces NaN with 0

# Forward fill (fill NaN with the previous value)
print("fill NaN with the previous value\n",s.ffill())

# Backward fill (fill NaN with the next value)
print("fill NaN with the next value\n",s.bfill())

print("Estimate missing values\n", s.interpolate())


#DataFrames
#A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns).
#Creating a DataFrame
#Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Zob', 'Charlie','Edward' , 'David', 'Frank', 'George'],
    'Age': [25, 22, 23, 27, 24, 29, 30],    
    'Score': [85, 89, 92, 78, 95, 88, 92]
}

df = pd.DataFrame(data)
print("Dataframe\n",df)
# We can apply same methods for data frames

print("Dataframe shape:", df.shape) # Get the shape of the DataFrame
print("Dataframe size:", df.size) # Get the size of the DataFrame
print("Dataframe index:", df.index) # Get the index of the DataFrame
print("Dataframe columns:", df.columns) # Get the columns of the DataFrame
print("Dataframe values:\n", df.values) # Get the values of the DataFrame
print("Dataframe info:\n", df.info()) # Get the info of the DataFrame
print("Dataframe describe:\n", df.describe()) # Get the description of the DataFrame
print("Dataframe head:\n", df.head(3)) # Get the first n rows of the DataFrame
print("Dataframe tail:\n", df.tail(3)) # Get the last n rows of the DataFrame

#Indexing and Slicing
#Selecting columns
print("Selecting a column:\n", df['Name']) # Select the 'Name' column
print("Selecting multiple columns:\n", df[['Name', 'Age']]) # Select the 'Name' and 'Age' columns

#Selecting rows
print("Selecting a row:\n", df.iloc[0]) # Select the first row
print("Selecting multiple rows:\n", df.iloc[0:3]) # Select the first three rows

#Indexing and reindexing
#Setting the index
df.set_index('Name', inplace=True) # Set the 'Name' column as the index
print("Dataframe after setting index:\n", df)

df_reset = df.reset_index()
print("\nDataFrame after resetting index:")
print(df_reset)

print("\nDataFrame after resetting index with drop=True:")
print(df.reset_index(drop=True))

#Arithmetic Operations
#Adding a new column
df['Grade'] = ['A', 'B', 'B', 'C', 'A', 'B', 'B']
print("Dataframe after adding a new column:\n", df)

#Dropping a column
df.drop(columns=['Grade'], inplace=True)
print("Dataframe after dropping a column:\n", df)

#Sorting
#Sorting by index
df.sort_index(inplace=True) # Sort the DataFrame by index
print("Dataframe after sorting by index:\n", df)

#Sorting by values
df.sort_values(by='Age', inplace=True) # Sort the DataFrame by 'Age'
print("Dataframe after sorting by values:\n", df)

#Aritmetic Operations between DataFrames and Series

# Create two DataFrames
data1 = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

data2 = {
    'A': [9, 8, 7],
    'B': [6, 5, 4],
    'C': [3, 2, 1]
}

df1 = pd.DataFrame(data1, index=['a', 'b', 'c'])
df2 = pd.DataFrame(data2, index=['a', 'b', 'c'])

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Arithmetic operations between DataFrames
df_add = df1 + df2
print("\nAddition of DataFrame 1 and DataFrame 2:")
print(df_add)

df_sub = df1 - df2
print("\nSubtraction of DataFrame 1 and DataFrame 2:")
print(df_sub)

df_mul = df1 * df2
print("\nMultiplication of DataFrame 1 and DataFrame 2:")
print(df_mul)

df_div = df1 / df2
print("\nDivision of DataFrame 1 by DataFrame 2:")
print(df_div)

# Create a Series
s = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
print("\nSeries:")
print(s)

# Arithmetic operations between DataFrame and Series
df_add_series = df1 + s
print("\nAddition of DataFrame 1 and Series:")
print(df_add_series)

df_sub_series = df1 - s
print("\nSubtraction of Series from DataFrame 1:")
print(df_sub_series)

df_mul_series = df1 * s
print("\nMultiplication of DataFrame 1 and Series:")
print(df_mul_series)

df_div_series = df1 / s
print("\nDivision of DataFrame 1 by Series:")
print(df_div_series)

# Broadcasting along rows
s_row = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("\nSeries for row operations:")
print(s_row)

df_add_row = df1.add(s_row, axis=0)
print("\nAddition of DataFrame 1 and Series along rows:")
print(df_add_row)
