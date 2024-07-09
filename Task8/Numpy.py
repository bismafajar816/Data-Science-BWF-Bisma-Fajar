import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Perform basic arithmetic operations
sum_array = np.sum(array)
mean_array = np.mean(array)
product_array = np.prod(array)

print("Array:", array)
print("Sum:", sum_array)
print("Mean:", mean_array)
print("Product:", product_array)

#Using built-in functions
arr_zeros = np.zeros((3, 3))    # Create a 3x3 array of zeros
arr_ones = np.ones((2, 4))      # Create a 2x4 array of ones
arr_arange = np.arange(0, 10, 2)    # Create an array of numbers from 0 to 10 with a step of 2
arr_linspace = np.linspace(0, 1, 5)   # Create an array of 5 numbers between 0 and 1
print("Array of zeroes: ", arr_zeros)
print("Array of ones: ",arr_ones)
print("Array arrangement: ",arr_arange)
print("Array of 5 numbers bw 0 and 1: ",arr_linspace)

#Arithmetic operations on two arrays 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Arithmetic operations
print("Array addition:", arr1 + arr2)
print("Array subtraction:", arr1 - arr2)
print("Array multiplication:", arr1 * arr2)
print("Array division:", arr1 / arr2)

# Broadcasting
print("Broadcasting (adding 5):", arr1 + 5)

#Indexing and Slice
#One dimensional array
arr = np.array([1, 2, 3, 4, 5])
print("First element:", arr[0])
print("Second element:", arr[1])
print("Last element:", arr[-1])
print("Elements between index 1 and 4 :", arr[1:4])

#Two dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element in row 1 and column 2:", arr[0, 1])
print("First row:", arr[0, :])
print("First column:", arr[:, 0])
print("Elements in rows 0 and 1 and columns 1 and 2:", arr[0:2, 1:3])


#Array Manipulation
#Reshaping an array
arr = np.arange(1, 7)   # Create an array of numbers from 1 to 6
reshaped_arr = arr.reshape((2, 3)) # Reshape the array to a 2x3 matrix
print("Reshaped array:\n", reshaped_arr)

#Flattening an array
flattened_arr = reshaped_arr.flatten() # Flatten the array to a 1D array
print("Flattened array:", flattened_arr)

#Concatenating arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated array:", concatenated_arr)

#splitting an array
arr = np.array([1, 2, 3, 4, 5, 6]) # Create an array of numbers from 1 to 6
split_arr = np.split(arr, 3) # Split the array into 3 subarrays
print("Split array:", split_arr)


#Random number generation
# Generate random numbers
rand_num = np.random.rand() # Generate a random number between 0 and 1
rand_num_arr = np.random.rand(3) # Generate an array of 3 random numbers
print("Random number:", rand_num)
print("Array of random numbers:", rand_num_arr)

random_arr = np.random.rand(3, 3)
print("Randomly generated array:\n", random_arr)

# Create an array of random integers between 10 and 100 with shape (3, 4)
random_int_array = np.random.randint(10, 100, size=(3, 4))

print("Random integer array:\n", random_int_array)
#Random sampling
arr = np.arange(10)
sample = np.random.choice(arr, 5)
print("Random sample from the array:", sample)

#File Handling
# Save an array to a file
arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)
print("Array saved to 'my_array.npy'.")
# Load an array from a file
loaded_arr = np.load('my_array.npy')
print("Loaded array:", loaded_arr)