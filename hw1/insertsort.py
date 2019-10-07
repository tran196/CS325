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

# Create Blank Array
testArray = []

# Write over file with empty string
with open('insert.txt', 'w') as filehandle:
    filehandle.write('') 

# Read in Data from Data.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('data.txt') as f:
    for line in f:
        line = line.split()     #Gets rid of blank space
        testArray = line        #Assign testArray to line

        for i in range(0, len(testArray)):
            testArray[i] = int(testArray[i])    #Convert str into int 
        
        insertionSort(testArray)            #Use insertionSort to rearrange array

        # Write array to file
        with open('insert.txt', 'a') as filehandle:
            for k in range(0, len(testArray)):
                filehandle.write(str(testArray[k]))
                filehandle.write(' ')   #Put a space between each number
            filehandle.write('\n')      #After array has been written to txt file then add a newline character



