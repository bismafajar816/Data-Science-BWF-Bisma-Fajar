from keras.models import Sequential  # Importing Sequential model class from Keras
from keras.layers import Dense, Input  # Importing Dense and Input layers from Keras
from keras.optimizers import Adam  # Importing Adam optimizer from Keras
from keras.models import load_model  # Importing load_model function to load saved models
import numpy as np  # Importing numpy for handling arrays and numerical operations

# Step 1: Define the model
model = Sequential()  # Creating a Sequential model instance
model.add(Input(shape=(10,)))  # Adding an Input layer, specifying the shape of the input data (10 features)
model.add(Dense(64, activation='relu'))  # Adding a Dense layer with 64 neurons and ReLU activation
model.add(Dense(32, activation='relu'))  # Adding another Dense layer with 32 neurons and ReLU activation
model.add(Dense(1, activation='sigmoid'))  # Adding a Dense layer with 1 neuron and sigmoid activation for binary classification

# Step 2: Compile the model
model.compile(loss='binary_crossentropy',  # Compiling the model with binary crossentropy loss function
              optimizer=Adam(learning_rate=0.001),  # Using Adam optimizer with a learning rate of 0.001
              metrics=['accuracy'])  # Tracking accuracy as a performance metric during training

# Generate synthetic data for demonstration
X_train = np.random.rand(100, 10)  # Generating 100 samples of training data with 10 features each
y_train = np.random.randint(2, size=100)  # Generating 100 binary labels (0 or 1) for the training data
X_test = np.random.rand(20, 10)  # Generating 20 samples of test data with 10 features each
y_test = np.random.randint(2, size=20)  # Generating 20 binary labels (0 or 1) for the test data

# Step 3: Train the model
model.fit(X_train, y_train, epochs=10, batch_size=10)  # Training the model on the training data for 10 epochs with a batch size of 10

# Step 4: Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)  # Evaluating the model on the test data, returning the loss and accuracy
print(f'Test loss: {loss}, Test accuracy: {accuracy}')  # Printing the test loss and accuracy

# Step 5: Make predictions
predictions = model.predict(X_test)  # Making predictions on the test data
print(predictions)  # Printing the predictions

# Step 6: Save the model
model.save('model.keras', save_format='keras')  # Saving the model in Keras format

# Step 7: Load the model
loaded_model = load_model('model.keras')  # Loading the saved model from file

# Step 8: Use the loaded model for predictions
loaded_predictions = loaded_model.predict(X_test)  # Making predictions with the loaded model on the test data
print(loaded_predictions)  # Printing the predictions from the loaded model
