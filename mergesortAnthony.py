# Tuan Tran
# 10/4/19
# CS 325 Homework 1 

import string

# Source: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr): 
    # del arr[0]  #delete the first element
    if len(arr) > 1: 
        mid = len(arr)//2 #Finding the mid of the array 
        lefthalf = arr[:mid] # Dividing the array elements  
        righthalf = arr[mid:] # into 2 halves 
  
        mergeSort(lefthalf) # Sorting the first half 
        mergeSort(righthalf) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(lefthalf) and j < len(R): 
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
testArray = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

mergeSort(testArray)
print(testArray)


# # Write over file with empty string
# with open('merge.txt', 'w') as filehandle:
#     filehandle.write('') 


# # Read in Data from Data.txt
# # Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
# with open('data.txt') as f:
#     for line in f:
#         line = line.split()     #Gets rid of blank space
#         testArray = line        #Assign testArray to line

#         for i in range(0, len(testArray)):
#             testArray[i] = int(testArray[i])    #Convert str into int 
#         del testArray[0]                #delete the first element in testArray since it is not needed
#         mergeSort(testArray)            #Use mergeSort to rearrange array

#          # Write array to file
#         with open('merge.txt', 'a') as filehandle:
#             for k in range(0, len(testArray)):
#                 filehandle.write(str(testArray[k]))
#                 filehandle.write(' ')   #Put a space between each number
#             filehandle.write('\n')      #After array has been written to txt file then add a newline character



