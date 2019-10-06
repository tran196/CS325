import string
import timeit

#Compute Insertion Sort Time
#Source: https://www.geeksforgeeks.org/timeit-python-examples/
SETUP_CODE = ''' 
import random
# Source: https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(arr):
    del arr[0]  #delete the first element
    for i in range(1, len(arr)): #Range starting at 1 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
'''
TEST_CODE_1000 = '''
mylist = [random.randint(1, 1000) for x in range(1000)]
insertionSort(mylist)
'''

TEST_CODE_5000 = '''
mylist = [random.randint(1, 1000) for x in range(5000)]
insertionSort(mylist)
'''

# Timeit Statement
print(  "Insertion Sort Time ",
        "Array Size: 1000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_1000,
                        number = 1))

# Timeit Statement
print(  "Insertion Sort Time ",
        "Array Size: 5000",
        "Execution Time (Seconds):",
         timeit.timeit( setup = SETUP_CODE, 
                        stmt = TEST_CODE_5000,
                        number = 1))


