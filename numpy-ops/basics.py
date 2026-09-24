import numpy as np

arr1 = np.array([1,2,3,4])

# Number of rows and columns.
print("Number of rows and columns. ", arr1.shape)

reshaped_arr = arr1.reshape(2,2)
print(reshaped_arr)

# Number of dimensions.
print("Number of dimensions. ",arr1.ndim)

# Total number of elements.
print("Total number of elements. ", arr1.size)

# dtype Data type
print("Datatype ", arr1.dtype)

# ndim  → dimensions
# shape → structure
# size  → total elements
# dtype → data type



# basic maths operations

arr1 = np.array([
    [1,2,3],
    [4,5,6]
])

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

add_arr = arr1 + arr2
sub_arr = arr1 - arr2
mul_arr = arr1 * arr2
div_arr = arr1 / arr2

arr3 = np.array([
    [1,2,3],
    [4,5,6]
])

# NumPy automatically applies to every element.

# This is called broadcasting.
prod_2_arr = arr3 * 2
prices = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(prices + 10)

print(prod_2_arr)

print(add_arr)
print(sub_arr)
print(mul_arr)
print(div_arr)

# Special NumPy arrays
print(np.zeros(5))
print(np.zeros((3, 4)))
print(np.ones(5))
print(np.ones((2,3)))
print(np.arange(1, 1, 11))

# 2D indexing
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[1, 1])
