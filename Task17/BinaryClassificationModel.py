"""
Binary Classification Model using Scikit-Learn and Iris Dataset
===============================================================

This script trains a binary classification model using Scikit-Learn and the Iris dataset.

**Importing Libraries**
-----------------------

The following libraries are imported:
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

"""
**Loading Iris Dataset**
------------------------

The Iris dataset is loaded:
"""
iris = load_iris()
X = iris.data
y = iris.target

"""
**Converting to Binary Classification Problem**
-----------------------------------------------

The target data is converted to a binary classification problem (0 vs. not 0):
"""
y_binary = (y == 0).astype(int)

"""
**Splitting Data into Training and Testing Sets**
-------------------------------------------------

The data is split into training and testing sets:
"""
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

"""
**Defining and Training the Logistic Regression Model**
-------------------------------------------------------

The logistic regression model is defined and trained on the training data:
"""
model = LogisticRegression()
model.fit(X_train, y_train)

"""
**Evaluating the Model**
------------------------

The model is evaluated on the testing data:
"""
accuracy = model.score(X_test, y_test)
print(f'Test accuracy: {accuracy:.3f}')

"""
**Using the Model to Make Predictions**
---------------------------------------

The model is used to make predictions on the testing data:
"""
predictions = model.predict(X_test)

"""
**Printing Classification Report**
----------------------------------

The classification report is printed:
"""
print(classification_report(y_test, predictions))

"""
**Printing Confusion Matrix**
-----------------------------

The confusion matrix is printed:
"""
print(confusion_matrix(y_test, predictions))

"""
**Plotting Decision Boundary**
------------------------------

The decision boundary of the model is plotted:
"""
# Plotting function
def plot_decision_boundary(model, X, y):
    # Define the bounds of the plot
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    # Predict the class using the trained model
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k', cmap=plt.cm.RdYlBu)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Decision Boundary')

# Reducing to 2 features for visualization purposes
X_train_vis = X_train[:, :2]
X_test_vis = X_test[:, :2]

# Training the model again with reduced features
model_vis = LogisticRegression()
model_vis.fit(X_train_vis, y_train)

# Plotting
plt.figure(figsize=(10, 6))
plot_decision_boundary(model_vis, X_train_vis, y_train)
plt.show()
