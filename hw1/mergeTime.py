# Tuan Tran
# 10/4/19
# CS 325 Homework 1 

import string
import timeit

#Compute Merge Sort Time
#Source: https://www.geeksforgeeks.org/timeit-python-examples/
SETUP_CODE = ''' 
import random
# Source: https://www.geeksforgeeks.org/merge-sort/
# Source: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php
def mergeSort(arr): 

    if len(arr) > 1: 
        mid = len(arr)//2 #Finding the mid of the array/list 
        L = arr[:mid] # Dividing the array/list elements from first element to mid 
        R = arr[mid:] # into 2 halves from mid to last element
  
        # Use Recursion to Sort the Left and Right lists
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = 0
        j = 0
        k = 0
          
        # Copy data to temp arrays/list L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
'''
TEST_CODE_1000 = '''
mylist = [random.randint(1, 10000) for x in range(1000)]
mergeSort(mylist)
'''

TEST_CODE_2500 = '''
mylist = [random.randint(1, 10000) for x in range(2500)]
mergeSort(mylist)
'''

TEST_CODE_5000 = '''
mylist = [random.randint(1, 10000) for x in range(5000)]
mergeSort(mylist)
'''

TEST_CODE_10000 = '''
mylist = [random.randint(1, 10000) for x in range(10000)]
mergeSort(mylist)
'''

TEST_CODE_12500 = '''
mylist = [random.randint(1, 10000) for x in range(12500)]
mergeSort(mylist)
'''

TEST_CODE_15000 = '''
mylist = [random.randint(1, 10000) for x in range(15000)]
mergeSort(mylist)
'''

TEST_CODE_20000 = '''
mylist = [random.randint(1, 10000) for x in range(20000)]
mergeSort(mylist)
'''

TEST_CODE_22500 = '''
mylist = [random.randint(1, 10000) for x in range(22500)]
mergeSort(mylist)
'''

TEST_CODE_25000 = '''
mylist = [random.randint(1, 10000) for x in range(25000)]
mergeSort(mylist)
'''

TEST_CODE_30000 = '''
mylist = [random.randint(1, 10000) for x in range(30000)]
mergeSort(mylist)
'''

# Timeit Statement 1000
print(  "Merge Sort Time ",
        "Array Size: 1000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1000,
                        number = 1))

# Timeit Statement 2500
print(  "Merge Sort Time ",
        "Array Size: 2500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_2500,
                        number = 1))                        

# Timeit Statement 5000
print(  "Merge Sort Time ",
        "Array Size: 5000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_5000,
                        number = 1))

# Timeit Statement 10000
print(  "Merge Sort Time ",
        "Array Size: 10000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_10000,
                        number = 1))

# Timeit Statement 12500
print(  "Merge Sort Time ",
        "Array Size: 12500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_12500,
                        number = 1))                       

# Timeit Statement 15000
print(  "Merge Sort Time ",
        "Array Size: 15000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_15000,
                        number = 1))

# Timeit Statement 20000
print(  "Merge Sort Time ",
        "Array Size: 20000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_20000,
                        number = 1))

# Timeit Statement 22500
print(  "Merge Sort Time ",
        "Array Size: 22500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_22500,
                        number = 1))

# Timeit Statement 25000
print(  "Merge Sort Time ",
        "Array Size: 25000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_25000,
                        number = 1))                        

# Timeit Statement 30000
print(  "Merge Sort Time ",
        "Array Size: 30000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_30000,
                        number = 1))

