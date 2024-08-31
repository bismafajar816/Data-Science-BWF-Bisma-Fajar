# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Set random seed for reproducibility
np.random.seed(42)

# Create a synthetic dataset with random values
# Assume this is our water quality dataset with various parameters
data = pd.DataFrame({
    'pH': np.random.uniform(6.5, 8.5, 100),                    # pH values between 6.5 and 8.5
    'Dissolved_Oxygen': np.random.uniform(5, 10, 100),          # Dissolved Oxygen values between 5 and 10 mg/L
    'Turbidity': np.random.uniform(1, 10, 100),                 # Turbidity values between 1 and 10 NTU
    'Electrical_Conductivity': np.random.uniform(100, 1000, 100), # Electrical Conductivity values between 100 and 1000 µS/cm
    'Temperature': np.random.uniform(10, 30, 100)               # Temperature values between 10 and 30 degrees Celsius
})

# Create a synthetic target variable 'WQI' (Water Quality Index) based on the other parameters
data['WQI'] = (
    0.3 * data['pH'] +
    0.4 * data['Dissolved_Oxygen'] -
    0.2 * data['Turbidity'] +
    0.1 * data['Electrical_Conductivity'] / 100 +
    0.1 * data['Temperature'] +
    np.random.normal(0, 0.5, 100)  # Adding some noise to the target variable
) * 10

# Preview the first few rows of the dataset
print(data.head())

# Exploratory Data Analysis (EDA)
# Print summary statistics of the dataset
print(data.describe())

# Visualize relationships between variables using pairplot
sns.pairplot(data)
plt.show()

# Display correlation matrix as a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Water Quality Parameters')
plt.show()

# Prepare data for machine learning
# Define feature variables (X) and target variable (y)
X = data.drop('WQI', axis=1)
y = data['WQI']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training data
rf_model.fit(X_train, y_train)

# Predict the Water Quality Index (WQI) on the test data
y_pred = rf_model.predict(X_test)

# Evaluate model performance using Mean Squared Error (MSE) and R-squared (R2) score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")

# Plot actual vs predicted WQI values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', lw=2)
plt.title('Actual vs Predicted Water Quality Index (WQI)')
plt.xlabel('Actual WQI')
plt.ylabel('Predicted WQI')
plt.show()

# Feature Importance Analysis
# Retrieve feature importances from the trained model
feature_importances = rf_model.feature_importances_

# Create a DataFrame to visualize feature importances
features_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})
features_df = features_df.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(8, 6))
sns.barplot(x='Importance', y='Feature', data=features_df, palette='viridis')
plt.title('Feature Importances in Predicting Water Quality Index (WQI)')
plt.show()
