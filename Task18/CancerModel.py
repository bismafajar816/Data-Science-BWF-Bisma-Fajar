#This model is for breast cancer prediction using the Wisconsin Breast Cancer dataset
#The dataset is available at https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
#The model uses the Random Forest Classifier algorithm to predict the breast cancer
#The model is trained on 80% of the dataset and tested on the remaining 20% of the dataset
#The model is evaluated using the confusion matrix and classification report

#Importing the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reading the dataset
df = pd.read_csv('data.csv')
df = df.drop(columns=['Unnamed: 32'])
print(df.head())  # Printing the first 5 rows of the dataset

# Checking the shape of the dataset
print("The shape of the dataset is: ", df.shape)  # The dataset has 569 rows and 33 columns
print("Description of the dataset: ", df.describe())  # Getting the summary statistics of the dataset
print("Information about the dataset: ", df.info())  # Getting the information about the dataset

# Plot pairplot of features colored by diagnosis
sns.pairplot(df, hue='diagnosis')
plt.show()