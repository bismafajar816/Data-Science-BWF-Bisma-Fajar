#Support Vector Machine
#It is a supervised learning used for both classification and regression problems.
#It is used to classify the data points based on features.
#It is used to predict the continuous values.
#It draws a best fit hyperplane that divides the dataset into classes.
#Margin: It is the maximum distance between the data points and the hyperplane.
#Support Vectors: The data points that are closest to the hyperplane are called support vectors.
#Big margin is chosen. It helps in reducing the error and overfitting.
#Types of SVM
#Linear SVM: It is used to classify linearly separable data points.
#Non-Linear SVM: It is used to classify non-linearly separable data points.

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC 
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train the SVM model
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the model
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Optional: Visualize the results (if applicable)
# Note: Visualization is typically done for 2D data. Modify as needed for your dataset.
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='winter')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='autumn', marker='x')
plt.title('SVM Classification Results')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

