# Tuan Tran
# 10/4/19
# CS 325 Homework 1 

import string

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

# Create Blank Array
testArray = []


# Write over file with empty string
with open('merge.txt', 'w') as filehandle:
    filehandle.write('') 


# Read in Data from Data.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('data.txt') as f:
    for line in f:
        line = line.split()     #Gets rid of blank space
        testArray = line        #Assign testArray to line

        for i in range(0, len(testArray)):
            testArray[i] = int(testArray[i])    #Convert str into int 
        del testArray[0]                #delete the first element in testArray since it is not needed
        mergeSort(testArray)            #Use mergeSort to rearrange array

         # Write array to file
        with open('merge.txt', 'a') as filehandle:
            for k in range(0, len(testArray)):
                filehandle.write(str(testArray[k]))
                filehandle.write(' ')   #Put a space between each number
            filehandle.write('\n')      #After array has been written to txt file then add a newline character



