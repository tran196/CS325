# Tuan Tran
# 12/4/19
# CS 325 Homework 8

import string
import timeit

#Compute BIN Packing Time
#Source: https://www.geeksforgeeks.org/timeit-python-examples/
SETUP_CODE = ''' 
import random
# Source: https://www.geeksforgeeks.org/insertion-sort/
# Source: https://www.khanacademy.org/computing/computer-science/algorithms/insertion-sort/a/insertion-sort
def insertionSort(arr):
    del arr[0]  #delete the first element
    for i in range(1, len(arr)):    #Range starting at 1 aka 2nd element
        key = arr[i] 
        j = i-1                     #Index of item left of i    
        while j >=0 and key < arr[j]: 
                arr[j+1] = arr[j]   #shift number in slot j to slot j+1
                j -= 1
        arr[j+1] = key
'''
TEST_CODE_1000 = '''
mylist = [random.randint(1, 10000) for x in range(1000)]
insertionSort(mylist)
'''

TEST_CODE_2500 = '''
mylist = [random.randint(1, 10000) for x in range(2500)]
insertionSort(mylist)
'''

TEST_CODE_5000 = '''
mylist = [random.randint(1, 10000) for x in range(5000)]
insertionSort(mylist)
'''

TEST_CODE_10000 = '''
mylist = [random.randint(1, 10000) for x in range(10000)]
insertionSort(mylist)
'''

TEST_CODE_12500 = '''
mylist = [random.randint(1, 10000) for x in range(12500)]
insertionSort(mylist)
'''

TEST_CODE_15000 = '''
mylist = [random.randint(1, 10000) for x in range(15000)]
insertionSort(mylist)
'''

TEST_CODE_20000 = '''
mylist = [random.randint(1, 10000) for x in range(20000)]
insertionSort(mylist)
'''

TEST_CODE_22500 = '''
mylist = [random.randint(1, 10000) for x in range(22500)]
insertionSort(mylist)
'''

TEST_CODE_25000 = '''
mylist = [random.randint(1, 10000) for x in range(25000)]
insertionSort(mylist)
'''

TEST_CODE_30000 = '''
mylist = [random.randint(1, 10000) for x in range(30000)]
insertionSort(mylist)
'''

# Timeit Statement 1000
print(  "Insertion Sort Time ",
        "Array Size: 1000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1000,
                        number = 1))

# Timeit Statement 2500
print(  "Insertion Sort Time ",
        "Array Size: 2500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_2500,
                        number = 1))                        

# Timeit Statement 5000
print(  "Insertion Sort Time ",
        "Array Size: 5000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_5000,
                        number = 1))

# Timeit Statement 10000
print(  "Insertion Sort Time ",
        "Array Size: 10000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_10000,
                        number = 1))

# Timeit Statement 12500
print(  "Insertion Sort Time ",
        "Array Size: 12500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_12500,
                        number = 1))                       

# Timeit Statement 15000
print(  "Insertion Sort Time ",
        "Array Size: 15000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_15000,
                        number = 1))

# Timeit Statement 20000
print(  "Insertion Sort Time ",
        "Array Size: 20000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_20000,
                        number = 1))

# Timeit Statement 22500
print(  "Insertion Sort Time ",
        "Array Size: 22500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_22500,
                        number = 1))

# Timeit Statement 25000
print(  "Insertion Sort Time ",
        "Array Size: 25000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_25000,
                        number = 1))                        

# Timeit Statement 30000
print(  "Insertion Sort Time ",
        "Array Size: 30000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_30000,
                        number = 1))
