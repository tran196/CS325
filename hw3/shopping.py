# Tuan Tran
# CS325 Assignment 3
# Problem 4 Shopping Spree


# ************** Variables for shopping.txt *****************
numTestCases = 0
currentTextCaseIndex = 0
numItems = 0
isNumItemLine = False
isPriceWeightLine = False
isNextTestCase = False


# ***********************************************************


# Write over file with empty string
# with open('shoppingResults.txt', 'w') as filehandle:
#     filehandle.write('') 


# Read in Data from shopping.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('shopping.txt') as f:
    currentLine = 0                         # use currentLine to keep track of what line I'm on in file
    for line in f:
        if currentLine == 0:
            numTestCases = int(line)        # first line in shoppping.txt used for number of test cases
            isNumItemLine = True            # next line is the number of items in test case
            
        elif isNumItemLine == True:
            numItems = int(line)            # set the number of Items variable
            priceList = []  #initalize price/weight list    
            isNumItemLine = False           #setting isNumItemLine = false; No longer on numItem Line of Testcase

        elif isPriceWeightLine == False:   
            line = line.split() 
            priceList.append(line)      # Assign Item Price & Weight 
            
        # *********Testing *********
            # for i in range(0, numItems):    # Assign Item Price & Weight 
            #     column = []                 # source: https://www.ict.social/python/basics/multidimensional-lists-in-python
            #     for j in range(0, numItems):
            #         column.append(line)
            #     priceList.append(column)

        # *********Testing *********

            isNextTestCase = True


        currentLine += 1                    # Increment current line



        # line = line.split()     #Gets rid of blank space
        # testArray = line        #Assign testArray to line
    
    print("numTestCases = ", numTestCases)         #test print
    print("numItems = ", numItems)                  #test print
    print("isNumItemLine = ", isNumItemLine)         #test print
    print("Current Line Number = ", currentLine)     #test print

    print("Price List = ", priceList)

#         for i in range(0, len(testArray)):
#             testArray[i] = int(testArray[i])    #Convert str into int 
#         del testArray[0]                #delete the first element in testArray since it is not needed

#         k = 0
#         j = len(testArray) - 1
#         stoogeSort(testArray, k, j)            #Use mergeSort to rearrange array

#          # Write array to file
#         with open('shoppingResults.txt', 'a') as filehandle:
#             for k in range(0, len(testArray)):
#                 filehandle.write(str(testArray[k]))
#                 filehandle.write(' ')   #Put a space between each number
#             filehandle.write('\n')      #After array has been written to txt file then add a newline character
