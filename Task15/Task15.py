#NDArray 
import numpy as np
#Create a 1D array of numbers from 0 to 9
array = np.arange(10)
print("1D array of numbers from 0 to 9: ",array)
#Create a 3×3 NumPy array of all True’s
array = np.ones((3,3),dtype=bool)
print("3x3 NumPy array of all True’s: ",array)
#Extract all odd numbers from array of 1-10
array = np.arange(1,11)
odd = array[array%2==1]
print("Odd numbers from array of 1-10: ",odd)
#Replace all odd numbers in an array of 1-10 with the value -1
array = np.arange(1,11)
array[array%2==1] = -1
print("Replace all odd numbers in an array of 1-10 with the value -1: ",array)
#Convert a 1D array to a 2D array with 2 rows
array = np.arange(10)
array = array.reshape(2,-1)
print("Convert a 1D array to a 2D array with 2 rows: ",array)
import numpy as np
#Convert a 1D array to a 2D array with 2 rows
array = np.arange(10)
print("1D array of numbers from 0 to 9: ",array)
array = array.reshape(2,-1)
print("Convert a 1D array to a 2D array with 2 rows: ",array)

#Convert a 1D array to a 2D array with 4 rows
arr = np.arange(8)
array = arr.reshape(4,-1) # -1 means that calculate the dimension of rows, 4 rows and 2 columns
array = np.reshape(arr, (4, 2)) # 4 rows and 2 columns
print("Convert a 1D array to a 2D array with 4 rows: \n",array)

arr = np.arange(15)
array = arr.reshape(5,-1)
print("Convert a 1D array to a 2D array with 5 rows: \n",array)

array.ravel() #Convert the 2D array back to 1D array
print("Convert the 2D array back to 1D array by ravel: ",array.ravel())

array.flatten() #Convert the 2D array back to 1D array
print("Convert the 2D array back to 1D array by flatten : ",array.flatten())

#C versus Fortran Order
arr = np.arange(15).reshape(5,3)
print("Original array: \n",arr)
print("C order: \n",np.array(arr.ravel(order='C'))) #Writes as rows first
print("Fortran order: \n",np.array(arr.ravel(order='F'))) #Writes as columns first

#Concatenating and splitting arrays
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print("Original array 1: \n",arr1)
print("Original array 2: \n",arr2)
print("Concatenating the arrays: \n",np.concatenate((arr1,arr2),axis=0)) #Concatenating the arrays along the row  
  
result = np.vstack((arr2, arr1))
print("V stack:\n", result)

result = np.hstack((arr1, arr2))
print("H stack:\n", result)

arr = np.random.rand(5, 2)
print("Original array: \n", arr)
first, second, third = np.split(arr, [1, 3]) #Rows splitting
print("Splitting")
print("first :\n", first) #The first part contains the rows from the start up to (but not including) index 1.
print("second:\n",second) #The second part contains the rows from index 1 up to (but not including) index 3
print("third: \n",third) #The third part contains the rows from index 3 to the end.

arr = np.random.rand(6, 3)  # Adjusted to have more columns for horizontal splitting
print("Original array: \n", arr)

# Horizontally split the array into 2 parts
first, second,third = np.hsplit(arr, 3)
print("Horizontal Splitting")
print("first :\n", first)  # The first part contains the columns from the start up to (but not including) index 2.
print("second:\n", second)
print("third:\n",third)
