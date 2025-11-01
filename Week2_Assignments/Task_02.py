#  Task 2: Lists and NumPy Arrays

'''
1. Create a list of 10 random integers. 
2. Perform the following operations: 
    Add and remove elements. 
    Find the maximum and minimum values. 
    Sort the list. 
3. Convert the list into a NumPy array and calculate: 
    Mean, Median, and Standard Deviation. 
'''

import numpy as np
import random

print("\n--- Task 2: Lists & NumPy ---")

# Creating a list of 10 random integers
my_list = [random.randint(1, 100) for _ in range(10)]
print("Original List:", my_list)

# Adding and removing elements
my_list.append(50)
print("After Adding 50:", my_list)

my_list.remove(50)
print("After Removing 50:", my_list)

# Max, Min, Sort
print("Maximum Value:", max(my_list))
print("Minimum Value:", min(my_list))

my_list.sort()
print("Sorted List:", my_list)

# Convert to NumPy Array
arr = np.array(my_list)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))

