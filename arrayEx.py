# example of Array using
import numpy as np

a = np.array([1, 8, 24])
print("Printing the Array and it's shape")
print(a)
print(np.shape(a))

# another way of writing the Array

b = np.array([
    [11, 3],
    [2, 5],
    [5, 21]
    ])

print('the details of Array is as follows:')
print(b)
print('the shape of Array is as follows:')
print(np.shape(b))

print("Example of Array with varied length")
# Array can have elements with different lengths
d = []                 # initialize an empty list
a = np.arange(3)       # array([0, 1, 2])
d.append(a)            # [array([0, 1, 2])]
b = np.arange(3,-1,-1) # array([3, 2, 1, 0])
d.append(b)            # [array([0, 1, 2]), array([3, 2, 1, 0])]

print(d)