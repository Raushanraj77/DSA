#Create array with inbuilt array module and external package numpy in python.

import array

my_array = array.array('i')   #Empty array
print(my_array)

# my_array1 = array.array('i', [1,2,3,4])      #Space complexity : O(N)
# print(my_array1)
# my_array1.insert(0, 5)
# print(my_array1)


# #Create array using NumPy. need install this module.

# import numpy as np

# np_array = np.array([], dtype=int)      #Empty array
# print(np_array)
# np_array1 = np.array([1,2,3,4])         #Space complexity : O(N)
# print(np_array1)
