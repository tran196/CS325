# Tuan Tran
# Homework 8
# Problem 1 Bin Packing
# 12/3/19

import sys
from collections import deque   # use a queue

class TestCase:
    def __init__(self, name, binCapacity, unsortedItemWeight, binList):
        self.name = name
        self.binCapacity = binCapacity
        self.unsortedItemWeight = unsortedItemWeight
        self.binList = binList

class Bin:
    def __init__(self, capacity, itemsInBin, binNumber = -1, testCase = "N/A"):
        self.capacity = capacity
        self.itemsInBin = itemsInBin
        self.binNumber = binNumber
        self.testCase = testCase

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
            if L[i] > R[j]:         #Sorting by value; Greatest Value will be first
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

#  Put each item as you come to it into the first (earliest opened) 
#  bin into which it fits.  
#  If there is no available bin then open a new bin. 
def firstFit(testCase):
    # ******* Local First Fit Variables **************
    # *************************************************
    localBinCount = 0           # Local Bin Count
    localBinCapacity = testCase.binCapacity     # Assign local bin capacity to testCase Bin Capacity
    localBinList = []       # List of Bin Objects
    isAssigned = False      # is the current value/ item assigned yet
    localUnsortedItemList = testCase.unsortedItemWeight      
    localItemsAssigned = 0      # Counter To Keep Track of Items Assigned
    localQueue = deque() # Create queue to go through items
    for i in localUnsortedItemList:
        localQueue.append(i) 
    # ********************************************************
    if not testCase.binList:       # Bin List is Empty
        # Create a new bin
        localBinList.append(Bin(localBinCapacity, [], 1, testCase))
        localBinCount += 1

    while localQueue:
        i = localQueue.popleft()    # Far left value in queue
        isAssigned = False

        for binElement in localBinList:
            if (isAssigned == True):
                break
            # Assign To Bin 
            elif (i <= binElement.capacity) and (binElement.capacity > 0):
                binElement.itemsInBin.append(i)           # Add i to itemsInBin for current bin
                binElement.capacity -= i   # Subtract i from bin.capacity
                localItemsAssigned += 1
                isAssigned = True
            
        if (isAssigned == False):
            # Create a new bin
            localBinCount += 1
            localBinList.append(Bin(localBinCapacity, [], localBinCount, testCase))

        # Assign to Bin
        lastIndex = len(localBinList) - 1   # TempIndex for newly created bin
        if (i <= localBinList[lastIndex].capacity) and (localBinList[lastIndex].capacity > 0) and (isAssigned == False):
            localBinList[lastIndex].itemsInBin.append(i)   # Assign value of i to newly created bin
            localBinList[lastIndex].capacity -= i   # Subtract i from bin.capacity

    print("First Fit:", len(localBinList) , end=" ")


#  First sort the items in decreasing order by size,
#  then use First-Fit on the resulting list. 
 
def firstFitDecreasing(testCase):
    # ******* Local First Fit Decreasing Variables **************
    # *************************************************
    localBinCount = 0           # Local Bin Count
    localBinCapacity = testCase.binCapacity     # Assign local bin capacity to testCase Bin Capacity
    localBinList = []       # List of Bin Objects
    isAssigned = False      # is the current value/ item assigned yet
    localUnsortedItemList = testCase.unsortedItemWeight      
    localItemsAssigned = 0      # Counter To Keep Track of Items Assigned
    localQueue = deque()        # Create queue to go through items

    mergeSort(localUnsortedItemList)
    
    for i in localUnsortedItemList:     # Append Int Values to Queue
        localQueue.append(i) 
    # ********************************************************

    if not testCase.binList:       # Bin List is Empty
        localBinList.append(Bin(localBinCapacity, [], 1, testCase))
        localBinCount += 1

    while localQueue:
        i = localQueue.popleft()    # Far left value in queue
        isAssigned = False

        for binElement in localBinList:
            if (isAssigned == True):
                break
            
            # Assign To Bin 
            elif (i <= binElement.capacity) and (binElement.capacity > 0):
                binElement.itemsInBin.append(i)           # Add i to itemsInBin for current bin
                binElement.capacity -= i   # Subtract i from bin.capacity
                localItemsAssigned += 1
                isAssigned = True
                
        if (isAssigned == False):
            # Create a new bin
            localBinCount += 1
            localBinList.append(Bin(localBinCapacity, [], localBinCount, testCase))

        # Assign to Bin
        lastIndex = len(localBinList) - 1   # TempIndex for newly created bin
        if (i <= localBinList[lastIndex].capacity) and (localBinList[lastIndex].capacity > 0) and (isAssigned == False):
            localBinList[lastIndex].itemsInBin.append(i)   # Assign value of i to newly created bin
            localBinList[lastIndex].capacity -= i   # Subtract i from bin.capacity

    print("First Fit Descreasing:", len(localBinList) , end=" ")





# Place the items in the order in which they arrive. 
# Place the next item into the bin which will leave the 
# least room left over after the item is placed in the bin. 
# If it does not fit in any bin, start a new bin. 
def bestFit(testCase):
    # ******* Local First Fit Decreasing Variables **************
    # *************************************************
    localBinCount = 0           # Local Bin Count
    localBinCapacity = testCase.binCapacity     # Assign local bin capacity to testCase Bin Capacity
    localBinList = []       # List of Bin Objects
    isAssigned = False      # is the current value/ item assigned yet
    localUnsortedItemList = testCase.unsortedItemWeight      
    localItemsAssigned = 0      # Counter To Keep Track of Items Assigned
    localQueue = deque()        # Create queue to go through items

    tempHighestBinCapacity = localBinCapacity * 2

    isOptimal = False           # Is Value Being Assigned Optimal Bin for Best Fit

    # mergeSort(localUnsortedItemList)
    
    for i in localUnsortedItemList:     # Append Int Values to Queue
        localQueue.append(i) 
    # ********************************************************

    if not testCase.binList:       # Bin List is Empty
        localBinList.append(Bin(localBinCapacity, [], 1, testCase)) # Add bin to localBinList
        localBinCount += 1

    while localQueue:
        i = localQueue.popleft()    # Far left value in queue
        isAssigned = False
        isOptimal = False           

        # ******* Test Print Area *********
        # *********************************
        print("Current Value i:", i)
        # *********************************

        for binElement in localBinList:
            if (isAssigned == True):
                break
            
            # Assign To Bin 
            elif (i <= binElement.capacity) and (binElement.capacity > 0):
                # Check if Assignment to bin is optimal
                 
                
                # ******* Test Print Area *********
                # *********************************
                print("Assigning i:", i, "to bin", binElement.binNumber)
                # *********************************
                
                binElement.itemsInBin.append(i)           # Add i to itemsInBin for current bin
                binElement.capacity -= i   # Subtract i from bin.capacity
                localItemsAssigned += 1
                isAssigned = True
                
        if (isAssigned == False):
            # Create a new bin
            localBinCount += 1
            localBinList.append(Bin(localBinCapacity, [], localBinCount, testCase))

        # Assign to Bin
        lastIndex = len(localBinList) - 1   # TempIndex for newly created bin
        if (i <= localBinList[lastIndex].capacity) and (localBinList[lastIndex].capacity > 0) and (isAssigned == False):
            # ******* Test Print Area *********
            # *********************************
            print("Assigning i:", i, "to bin", localBinList[lastIndex].binNumber)
            # *********************************
            localBinList[lastIndex].itemsInBin.append(i)   # Assign value of i to newly created bin
            localBinList[lastIndex].capacity -= i   # Subtract i from bin.capacity

    print("Best Fit:", len(localBinList) , end=" ")




# ********** Variables for Bin Packing ****************
# ************************************************************
testArray = []
currentTestCase = 1
numTestCases = 0
numOfItems = 0

tempBinCapacity = 0
tempNumberOfItems = 0

isNewTestCaseLine = False
isBinCapacityLine = False
isNumOfItemLine = False
isListOfItemWeight = False

tempUnsortedItemWeight = []         # Empty List of Unsorted Item Weights
tempBinList = []                    # Empty List of Bin Objects

count = 0                           # counter to keep track of number of items



# Read in Data from bin.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php

# with open('bin.txt') as f:
with open('bin1.txt') as f:             # ********* Remember to change back to bin.txt

    testArray = f.read().splitlines()       # read in each line; then split and assign to testArray
    #  print(testArray)   # Test Print

    for line in testArray: # Loop through each line in the testArray
        # if isListOfItemWeight == True:          # If the line contains data for an Item Weight
        #     testUnsortedItemWeight = []         # Initalize a tempActivity list to hold activity number, start time, end time from act.txt

        if count == 0:
            numTestCases = line
            isBinCapacityLine = True        # Next line is the binCapacityLine

        elif isBinCapacityLine == True:     # Current Line is Bin Capacity
            tempBinCapacity = line          # Set tempBinCapacity
            isNumOfItemLine = True          # Next line is the number of Items 
            isBinCapacityLine = False

            # # Test print type binCapacity
            # print("TempBinCapacity", tempBinCapacity)
            # print(type(tempBinCapacity))

        elif isNumOfItemLine == True:       # Current Line is Number of Items
            tempNumberOfItems = line
            isListOfItemWeight = True       # Next line is the list of Item Weights
            isNumOfItemLine = False

        elif isListOfItemWeight == True:     # Current Line is List of Unsorted Item Weights
            for i in line.split():          # Split line
                i = int(i)                  # Convert str to int
                tempUnsortedItemWeight.append(i)
            isListOfItemWeight = False

        if (isBinCapacityLine == False) and (isNumOfItemLine == False) and (isListOfItemWeight == False):
            print("Test Case", currentTestCase, end=" ")
            
            print() # Test Print for Formatting 
            isBinCapacityLine = True        # Next line is the binCapacityLine

            tempTestCaseName = "testCase" + str(currentTestCase) 

            tempBinCapacity = int(tempBinCapacity)  # Convert from str to int

            tempTestCase = TestCase(tempTestCaseName, tempBinCapacity, tempUnsortedItemWeight, tempBinList)


            # print("numTestCases",numTestCases) # Test Print
            # print("tempBinCapacity",tempBinCapacity) # Test Print
            # print("tempNumberOfItems",tempNumberOfItems) # Test Print
            # print("tempUnsortedItemWeight",tempUnsortedItemWeight) # Test Print

            # # Run First Fit

            # firstFit(tempTestCase)
            # # print("********************\n")     # Test print for formatting

            # # Run First Fit Decreasing
            # firstFitDecreasing(tempTestCase)
            # # print("********************\n")     # Test print for formatting

            # # Run Best Fit
            # bestFit(tempTestCase)
            # print("********************\n")     # Test print for formatting

            if currentTestCase == 3:
                firstFit(tempTestCase)
                print("********************\n")     # Test print for formatting
                firstFitDecreasing(tempTestCase)
                print("********************\n")     # Test print for formatting
                bestFit(tempTestCase)
                print("********************\n")     # Test print for formatting

            # # Test Stop After 1st Test Case
            # if currentTestCase == 1:
            #     sys.exit()            


            # Reset Variables
            tempTestCaseName = "N/A"
            tempBinCapacity = 0
            tempUnsortedItemWeight = []
            tempBinList = []

            currentTestCase += 1
     
        count += 1
        

        # print(line) # Test Print

    # print("numTestCases",numTestCases) # Test Print
    # print("tempBinCapacity",tempBinCapacity) # Test Print
    # print("tempNumberOfItems",tempNumberOfItems) # Test Print
    # print("tempUnsortedItemWeight",tempUnsortedItemWeight) # Test Print