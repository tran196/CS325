# Tuan Tran
# Homework 4 Problem 4 Activity Selection Last to Start


# Class for all the activites
class Activity:
    def __init__(self, activityNumber, startTime, endTime):
        self.activityNumber = activityNumber
        self.startTime = startTime
        self.endTime = endTime

# ********** Variables for Activity Selection ************
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
        if isSetLine == False:          # If the line is for an activity (activity number, start time, end time)

            tempActivity = []                # Initalize a tempActivity list to hold activity number, start time, end time
            
            for i in line.split():          # Split line (which contains activity num, startTime, endTime) into separate entries
                i = int(i)                  # Convert str to int
                tempActivity.append(i)      # Add to tempActivity list

            activityNum = -1
            startTime = -1
            endTime = -1

            for i in range(len(tempActivity)):
                if i == 0:
                    activityNum = tempActivity[i]
                elif i == 1:
                    startTime = tempActivity[i]
                elif i == 2:
                    endTime = tempActivity[i]
            
            tempSet[count-1] = Activity(activityNum, startTime, endTime)    # Assign the string inside of tempSet into an Activity Object

            print("tempSet[",count, "]", tempSet[count-1].activityNumber) # test print

            # print("Temp Set", tempSet)            # test print
            # print("Count", count)
            # print("tempActivity", tempActivity)     # test print
            

            if count == numActivities:  # reached the next set of activities
                isSetLine = True        # next line will be the number of activies in next set
                count = 0               # reset count to track new set of activities
            else:
                count += 1              # Increment count var to keep track of when the next set

        else:                           # current line is the number of activities in the current set
            tempSet = []    # tempSet list to hold strings how many activies in a set
            numActivities = int(line)                   # set the number of activites in the set and convert from string to int 
            count += 1
            isSetLine = False                           # next line will be the activity number, start time, and end time
            print("Set Number", setNumber)                  # Test Print
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
