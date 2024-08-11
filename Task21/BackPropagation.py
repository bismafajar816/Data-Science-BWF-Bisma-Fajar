import numpy as np  # Import numpy for matrix operations

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Sigmoid function

def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of the sigmoid function

# Initialize the neural network
input_layer_neurons = 2  # Number of input neurons (for XOR: 2 inputs)
hidden_layer_neurons = 2  # Number of hidden neurons
output_neurons = 1  # Number of output neurons (for XOR: 1 output)

# Initialize weights and biases with random values
weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

# Training data for XOR
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input data
expected_output = np.array([[0], [1], [1], [0]])  # Expected output

# Training parameters
learning_rate = 0.1  # Learning rate
epochs = 10000  # Number of iterations

# Training loop
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_activation = np.dot(inputs, weights_input_hidden) + bias_hidden  # Activation of hidden layer
    hidden_layer_output = sigmoid(hidden_layer_activation)  # Output of hidden layer
    
    output_layer_activation = np.dot(hidden_layer_output, weights_hidden_output) + bias_output  # Activation of output layer
    predicted_output = sigmoid(output_layer_activation)  # Output of output layer
    
    # Calculate error
    error = expected_output - predicted_output  # Difference between expected and predicted output

    # Backward propagation
    d_predicted_output = error * sigmoid_derivative(predicted_output)  # Gradient of the error with respect to the output
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)  # Error propagated to the hidden layer
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)  # Gradient of the error with respect to the hidden layer
    
    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate  # Update weights from hidden to output layer
    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate  # Update biases of the output layer
    weights_input_hidden += inputs.T.dot(d_hidden_layer) * learning_rate  # Update weights from input to hidden layer
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate  # Update biases of the hidden layer

# Print final weights and biases
print("Weights from Input to Hidden Layer:\n", weights_input_hidden)  # Display updated weights from input to hidden layer
print("Weights from Hidden to Output Layer:\n", weights_hidden_output)  # Display updated weights from hidden to output layer
print("Biases of Hidden Layer:\n", bias_hidden)  # Display updated biases of the hidden layer
print("Biases of Output Layer:\n", bias_output)  # Display updated biases of the output layer

# Test the network
print("Predicted Output:\n", predicted_output)  # Display the final predicted output after training