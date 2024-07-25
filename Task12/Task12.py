# steps to evaluate a model using precision, recall, accuracy, and visualizations using the Iris dataset.

# Data Preprocessing.
# Splitting the Data.
# Feature Scaling.
# Training the Model.
# Making Predictions.
# Evaluating the Model.
# Visualizing the Results

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
from sklearn.datasets import load_iris
iris = load_iris()

# Convert to DataFrame
data = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                    columns= iris['feature_names'] + ['target'])

# Display the first few rows of the dataset
print(data.head())

# Step 1: Data Preprocessing
X = data.iloc[:, :-1].values  # Features
y = data.iloc[:, -1].values   # Target variable

# Step 2: Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Feature Scaling
scaler = StandardScaler()   # The StandardScaler standardizes features by removing the mean and scaling to unit variance. This means that each feature will have a mean of 0 and a standard deviation of 1 after scaling.
X_train = scaler.fit_transform(X_train) #The fit_transform method first computes the mean and standard deviation of each feature in the training set and then uses these statistics to scale the training data.
X_test = scaler.transform(X_test)   #The transform method uses the mean and standard deviation computed by the fit method to scale the test data.

# Step 4: Training the Model
classifier = KNeighborsClassifier(n_neighbors=5) # The KNeighborsClassifier is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure.
classifier.fit(X_train, y_train) # The fit method is used to train the model using the training data.

# Step 5: Making Predictions
y_pred = classifier.predict(X_test)

# Step 6: Evaluating the Model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Step 7: Visualizing the Results
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=iris['target_names'], yticklabels=iris['target_names'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
