# Tuan Tran
# 10/12/19
# CS 325 Homework 2

#Source: https://en.wikipedia.org/wiki/Stooge_sort
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

# Create Blank Array
testArray = []


# Write over file with empty string
with open('stooge.txt', 'w') as filehandle:
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

        k = 0
        j = len(testArray) - 1
        stoogeSort(testArray, k, j)            #Use mergeSort to rearrange array

         # Write array to file
        with open('stooge.txt', 'a') as filehandle:
            for k in range(0, len(testArray)):
                filehandle.write(str(testArray[k]))
                filehandle.write(' ')   #Put a space between each number
            filehandle.write('\n')      #After array has been written to txt file then add a newline character
