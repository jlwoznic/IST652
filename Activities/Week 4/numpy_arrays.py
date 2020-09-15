# NUMPY Arrays
import numpy as np

# 1. Write a Python program to convert a list and tuple into arrays.

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# convert to array
# List to array: [1 2 3 4 5 6 7 8] 
my_array = np.array(my_list)

# convert to tuple 
my_tuple = tuple(my_list)

# Tuple to array:
# [[8 4 6]  [1 2 3]]
new_list = [my_array[7], my_array[3], my_array[5]]
new_array = np.array(new_list)
final_array = np.append([new_array], [my_array[0:3]], axis = 0)
final_tuple = tuple(final_array)
# Discuss how the list and tuple differ from the arrays.


# 2. Write a Python program to append values to the end of an array. 
# Original array:
#  [10, 20, 30] 
start_array = np.array([10, 20, 30])
append_array = np.array([40, 50, 60, 70, 80, 90])
# Expected Output:

# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]
# NUMPY Arrays

def app_arr(array, to_append):
    new_array = np.append(array, to_append)
    return new_array;

appended_array = app_arr(start_array, append_array)


