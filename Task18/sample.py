import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Reading the dataset
file_path = 'data.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Dropping unnecessary column
df = df.drop(columns=['Unnamed: 32'], errors='ignore')  # Adjust in case the column is not present
print("Column Names are: ", df.columns)  # Getting the column names of the dataset
print("The shape of the dataset is: ", df.shape)  # The dataset has 569 rows and 32 columns
print("Description of the dataset: ", df.describe())  # Getting the summary statistics of the dataset

# Encode the 'diagnosis' column to numeric values for plotting
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Select a subset of features to avoid constant columns
selected_features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean']

# Plot scatter matrix of features colored by diagnosis
scatter_matrix(df[selected_features + ['diagnosis']], alpha=0.2, figsize=(12, 12), diagonal='hist', c=df['diagnosis'])
plt.show()

# Splitting the dataset into features (X) and target (y)
X = df.drop(['diagnosis'], axis=1)
y = df['diagnosis']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiating the model
model = RandomForestClassifier(random_state=42)

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Displaying classification report
print(classification_report(y_test, y_pred))

# Displaying confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 6))
plt.imshow(conf_matrix, cmap='Blues', alpha=0.5)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.xticks(np.arange(2), ['Benign', 'Malignant'])
plt.yticks(np.arange(2), ['Benign', 'Malignant'])

for i in range(len(conf_matrix)):
    for j in range(len(conf_matrix)):
        plt.text(j, i, conf_matrix[i, j], ha='center', va='center', color='black')

plt.colorbar()
plt.show()

# Feature importance visualization
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(10, 6))
plt.barh(features, importances)
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.show()
