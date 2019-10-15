# Tuan Tran
# 10/14/19
# CS 325 Homework 2

import string
import timeit

#Compute Stooge Sort Time
#Source: https://www.geeksforgeeks.org/timeit-python-examples/
SETUP_CODE = ''' 
import random
def stoogeSort (arr, i, j):

    if arr[i] > arr[j]:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    #If there are more than 3 elements in array
    if j - i + 1 > 2:   
        tempLength = (j - i + 1) // 3
        stoogeSort(arr, i, j - tempLength)      #Initial 2/3
        stoogeSort(arr, i + tempLength, j)      #Last 2/3 
        stoogeSort(arr, i, j - tempLength)      #Inital 2/3
'''
TEST_CODE_100 = '''
mylist = [random.randint(1, 10000) for x in range(100)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_250 = '''
mylist = [random.randint(1, 10000) for x in range(250)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_500 = '''
mylist = [random.randint(1, 10000) for x in range(500)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_650 = '''
mylist = [random.randint(1, 10000) for x in range(650)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_750 = '''
mylist = [random.randint(1, 10000) for x in range(750)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_1000 = '''
mylist = [random.randint(1, 10000) for x in range(1000)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_1100 = '''
mylist = [random.randint(1, 10000) for x in range(1100)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_1250 = '''
mylist = [random.randint(1, 10000) for x in range(1250)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_1500 = '''
mylist = [random.randint(1, 10000) for x in range(1500)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''

TEST_CODE_2000 = '''
mylist = [random.randint(1, 10000) for x in range(2000)]
i = 0
j = len(mylist) - 1
stoogeSort(mylist, i, j)
'''



# Timeit Statement 100
print(  "Stooge Sort Time ",
        "Array Size: 100",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_100,
                        number = 1))

# Timeit Statement 250
print(  "Stooge Sort Time ",
        "Array Size: 250",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_250,
                        number = 1))                        

# Timeit Statement 500
print(  "Stooge Sort Time ",
        "Array Size: 500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_500,
                        number = 1))

# Timeit Statement 650
print(  "Stooge Sort Time ",
        "Array Size: 650",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_650,
                        number = 1))

# Timeit Statement 750
print(  "Stooge Sort Time ",
        "Array Size: 750",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_750,
                        number = 1))

# Timeit Statement 1000
print(  "Stooge Sort Time ",
        "Array Size: 1000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1000,
                        number = 1))

# Timeit Statement 1100
print(  "Stooge Sort Time ",
        "Array Size: 1100",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1100,
                        number = 1))

# # Timeit Statement 1250
print(  "Stooge Sort Time ",
        "Array Size: 1250",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1250,
                        number = 1))                       

# Timeit Statement 1500
print(  "Stooge Sort Time ",
        "Array Size: 1500",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1500,
                        number = 1))

# Timeit Statement 2000
print(  "Stooge Sort Time ",
        "Array Size: 2000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_2000,
                        number = 1))


