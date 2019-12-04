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

#  Put each item as you come to it into the first (earliest opened) 
#  bin into which it fits.  
#  If there is no available bin then open a new bin. 
def firstFit(testCase):
    # print("firstFit")  # Test Print
    # print(testCase.name)  # Test Print
    # print(testCase.name, "Bin Capacity", testCase.binCapacity)  # Test Print
    # print(testCase.name, "Unsorted Item Weight List", testCase.unsortedItemWeight)  # Test Print
    # print(testCase.name, "Bin List", testCase.binList)  # Test Print

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
        # print(testCase.name , "Bin List is empty")      # test Print
        # Create a new bin
        localBinList.append(Bin(localBinCapacity, [], 1, testCase))
        localBinCount += 1

    # # Loop through localUnsortedItemList
    # for i in localUnsortedItemList:
    #     for binElement in localBinList:
    #         # if localItemsAssigned <= len(localUnsortedItemList): # Make sure not to over assign items
            
    #         # Assign To Bin 
    #         if (i <= binElement.capacity) and (binElement.capacity > 0):
    #             tempIndex = localUnsortedItemList.index(i)
    #             binElement.itemsInBin.append(i)           # Add i to itemsInBin for bin1
    #             binElement.capacity = binElement.capacity - i   # Subtract i from bin.capacity
    #             localItemsAssigned += 1
    #             localUnsortedItemList.pop(tempIndex)

    #         # Else Create a new bin
    #         else:
    #             localBinCount += 1
    #             localBinList.append(Bin(localBinCapacity, [], localBinCount, testCase))

    while localQueue:
        i = localQueue.popleft()    # Far left value in queue
        isAssigned = False

        for binElement in localBinList:
            # print("******Bin Number", binElement.binNumber, "Current Bin Capacity", binElement.capacity)   # Test Print
            # print("Current Value of i=", i)                     # Test Print
            
            if (isAssigned == True):
                break
            
            # Assign To Bin 
            elif (i <= binElement.capacity) and (binElement.capacity > 0):
                binElement.itemsInBin.append(i)           # Add i to itemsInBin for current bin
                binElement.capacity -= i   # Subtract i from bin.capacity
                localItemsAssigned += 1
                # print("Just assigned value=", i, "to bin", binElement.binNumber) # Test Print
                isAssigned = True
                
            
        if (isAssigned == False):
            # Create a new bin
            localBinCount += 1
            localBinList.append(Bin(localBinCapacity, [], localBinCount, testCase))
            # print("***Just Created a New Bin", localBinCount)

        # Assign to Bin
        lastIndex = len(localBinList) - 1   # TempIndex for newly created bin
        if (i <= localBinList[lastIndex].capacity) and (localBinList[lastIndex].capacity > 0) and (isAssigned == False):
            localBinList[lastIndex].itemsInBin.append(i)   # Assign value of i to newly created bin
            localBinList[lastIndex].capacity -= i   # Subtract i from bin.capacity
            # print("Just assigned value=", i, "to bin", localBinList[lastIndex].binNumber) # Test Print

    # for i in localBinList:
    #     print(i.capacity, i.itemsInBin, i.binNumber)    # Test Print

    print("First Fit:", len(localBinList) , end=" ")


#  First sort the items in decreasing order by size,
#  then use First-Fit on the resulting list. 
 
def firstFitDecreasing():
    print("firstFitDecreasing")

# Place the items in the order in which they arrive. 
# Place the next item into the bin which will leave the 
# least room left over after the item is placed in the bin. 
# If it does not fit in any bin, start a new bin. 
def bestFit():
    print("bestFit")


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
with open('bin.txt') as f:

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
            
            # print() # Test Print for Formatting 
            isBinCapacityLine = True        # Next line is the binCapacityLine

            tempTestCaseName = "testCase" + str(currentTestCase) 

            tempBinCapacity = int(tempBinCapacity)  # Convert from str to int

            tempTestCase = TestCase(tempTestCaseName, tempBinCapacity, tempUnsortedItemWeight, tempBinList)

            # Run First Fit
            firstFit(tempTestCase)

            # Run First Fit Decreasing

            # Run Best Fit


            # Test Stop After 1st Test Case
            if currentTestCase == 1:
                sys.exit()            


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