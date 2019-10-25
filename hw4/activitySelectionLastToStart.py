# Tuan Tran
# Homework 4 Problem 4 Activity Selection Last to Start


# Class for all the activites
class Activity:
    def __init__(self, activityNumber, startTime, endTime):
        self.activityNumber = activityNumber
        self.startTime = startTime
        self.endTime = endTime

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
            if L[i].endTime > R[j].endTime:         #Sorting by endTime; Greatest/Latest End Time will be first
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


def optimizeActivity(arr):
  result = []
  if len(result) == 0:  #Add first item in array to result array
    result.append(arr[0])
  tempStartTime = result[0].startTime
  for i in arr:
    if tempStartTime >= i.endTime:
      result.append(i)
      tempStartTime = i.startTime
      
  return result

# ********** Variables for Activity Selection ****************
# ************************************************************

# Initalize Blank List
testArray = []
isSetLine = True    #is this a set line 
numActivities = 0   # counter to keep track of how many activities in each set
count = 0       # counter to track which line we are on in the act.txt file
setNumber = 1   # keep track of which activitiy set currently on

# ************************************************************

# Read in Data from act.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('act.txt') as f:

    testArray = f.read().splitlines()       # read in each line; then split and assign to testArray

    # tempSet = []    # tempSet list to hold strings how many activies in a set
    
    for line in testArray:              # Loop through each line in the testArray
        if isSetLine == False:          # If the line contains data for an activity (activity number, start time, end time)

            tempActivityList = []                # Initalize a tempActivity list to hold activity number, start time, end time from act.txt
            
            for i in line.split():          # Split line (which contains activity num, startTime, endTime) into separate entries
                i = int(i)                  # Convert str to int
                tempActivityList.append(i)      # Add to tempActivity list

            #Temp variables to store 
            tempActivityNum = -1
            tempStartTime = -1
            tempEndTime = -1

            for i in range(len(tempActivityList)):
                if i == 0:
                    tempActivityNum = tempActivityList[i]
                elif i == 1:
                    tempStartTime = tempActivityList[i]
                elif i == 2:
                    tempEndTime = tempActivityList[i]
            
            tempSet[count-1] = Activity(tempActivityNum, tempStartTime, tempEndTime)    # Assign the string inside of tempSet into an Activity Object


            # print("Activity Number:", tempSet[count-1].activityNumber, "Start Time:", tempSet[count-1].startTime, "End Time:", tempSet[count-1].endTime)
            # print("tempSet[",count, "]", tempSet[count-1].activityNumber) # test print
            # print("Temp Set", tempSet)            # test print
            # print("Count", count)
            # print("tempActivity", tempActivity)     # test print
            

            if count == numActivities:  # reached the next set of activities
                isSetLine = True        # next line will be the number of activies in next set
                count = 0               # reset count to track new set of activities
                
                # print("Before Merge Sort")          # test print
                # for i in tempSet:                   # test print
                #     print("ActivityNum:", i.activityNumber, "Start Time:", i.startTime, "End Time:", i.endTime) # test print

                # *************** Run Merge Sort here ******************
                mergeSort(tempSet)
                # ************************************************************

                # print("After Merge Sort")                       # test print
                # for i in tempSet:                               # test print
                #     print("ActivityNum:", i.activityNumber, "Start Time:", i.startTime, "End Time:", i.endTime) # test print


                # for i in tempSet:                               # test print
                #     # print("set1Activity", i.activityNumber, " = Activity(",i.activityNumber, ", ", i.startTime, ", ", i.endTime , ")", sep="") # test print
                #     print("testArr.append(set1Activity", i.activityNumber, ")", sep="")     # test print

                # *************** Compare/Choose Which Activities ******************
                result = []
                result = optimizeActivity(tempSet)
                print("Number of activities selected =", len(result))
                print("Activities: ", end="")
                for i in result[::-1]:
                    print(i.activityNumber, end="")
                    print(" ", end="")
                print("\n")
                # ********************************************************************
                
            else:
                count += 1              # Increment count var to keep track of when the next set

        else:                           # current line is the number of activities in the current set
            tempSet = []    # tempSet list to hold strings how many activies in a set
            numActivities = int(line)                   # set the number of activites in the set and convert from string to int 
            count += 1
            isSetLine = False                           # next line will be the activity number, start time, and end time
            print("Set", setNumber)                  # Test Print
            # print("Number of Activities:", numActivities)   # Test Print

            for i in range(numActivities):
                activityObj = "set" + str(setNumber) + "activity" + str(i+1)
                tempSet.append(activityObj)
                # print(activityObj)          #test print

            setNumber += 1
            
        # print("Count:", count)
        # print(line)


    # print("Temp Set", tempSet)

    #     for i in range(0, len(testArray)):
    #         testArray[i] = int(testArray[i])    #Convert str into int 
    #     # del testArray[0]                #delete the first element in testArray since it is not needed

    

        # k = 0
        # j = len(testArray) - 1
        # stoogeSort(testArray, k, j)            #Use mergeSort to rearrange array

        #  # Write array to file
        # with open('stooge.txt', 'a') as filehandle:
        #     for k in range(0, len(testArray)):
        #         filehandle.write(str(testArray[k]))
        #         filehandle.write(' ')   #Put a space between each number
        #     filehandle.write('\n')      #After array has been written to txt file then add a newline character
