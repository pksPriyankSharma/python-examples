# example of Array using arange
# arange can create one dimensional Array, and can not take user defined input

import numpy as np
a = np.arange(1, 10)
print("The Array details are as below:")
print(a)
print(a.shape)

print('printing the Array with a skip/ spacing of 2')
b = np.arange(1, 15, 2)
print(b)
print(b.shape)


print('printing the Array with a skip/ spacing of 2 in reducing order')
c = np.arange(15, 1, -2)
print(c)
print(c.shape)