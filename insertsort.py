import string


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

# This function reads in a file and prints the contents of a file as an array
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php

# Create Blank Array
testArray = []

# Read in Data from Data.txt
with open('data.txt') as f:
    for line in f:
        line = line.split()     #Gets rid of blank space
        testArray = line        #Assign testArray to line

        for i in range(0, len(testArray)):
            testArray[i] = int(testArray[i])    #Convert str into int 
        
        #Before Insertion Sort
        print("Before Insertion Sort:")
        print(testArray)        #Test Print 

        #After Insertion Sort
        print("After Insertion Sort:")
        insertionSort(testArray)
        print(testArray)        #Test Print


        


