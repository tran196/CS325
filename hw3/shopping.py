# Tuan Tran
# CS325 Assignment 3
# Problem 4 Shopping Spree


def shoppingSpreeOptimization(testCaseCount, priceList, familyList):
    totalPrice = 0
    tempList = []
    for i in range(len(priceList)):
        for j in priceList[i]:
            temp = int(j)
            tempList.append(temp)
    # print("This is shopping optimization")    #Test print
    print("Price List: ", priceList)            #Test print
    # print("Family List: ", familyList)        #Test print
    # print("Test Case ", testCaseCount)        #Test print
    # print("Total Price ", totalPrice)         #Test print

    print("Temp List: ", tempList)              #Test print        





# ************** Variables for shopping.txt *****************
testCaseCount = 0
numTestCases = 0
currentTextCaseIndex = 0
numItems = 0
familySize = 0
isNumItemLine = False
isPriceWeightLine = False
isFamilySizeLine = False
isFamilyWeightLine = False
isNextTestCase = False

# ***********************************************************


# Write over file with empty string
# with open('shoppingResults.txt', 'w') as filehandle:
#     filehandle.write('') 


# Read in Data from shopping.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('shopping.txt') as f:
    currentLine = 0                         # use currentLine to keep track of what line I'm on in file
    count = 0
    for line in f:
        if currentLine == 0:
            numTestCases = int(line)        # first line in shoppping.txt used for number of test cases
            isNumItemLine = True            # next line is the number of items in test case
            
        elif isFamilyWeightLine == True:
            # print("Family Weight Line")    #Test print
            if count < familySize:
                # line = line.split()
                line = int(line)
                familyList.append(line)
                count += 1
                if count == familySize:
                    isFamilyWeightLine = False
                    isNumItemLine = True
                    count = 0
                    testCaseCount += 1
                    # print("Family List = ", familyList) # Test Print
                # Need to do optimization here **********************************
                    shoppingSpreeOptimization(testCaseCount, priceList,familyList)
                    
                # ********************************************************************

        elif isFamilySizeLine == True:
            # print("Family Size Line")       #Test print
            isFamilyWeightLine = True
            isFamilySizeLine = False
            familySize = int(line)          # Assign Family Size Value
            print("Family Size = ", familySize) #Test print


        elif isPriceWeightLine == True:   
            # print("Price/Weight Line")  #Test print
            if count < numItems:
                line = line.split() 
                priceList.append(line)          # Assign Item Price & Weight 

                count += 1
                if count == numItems:
                    isPriceWeightLine = False
                    isFamilySizeLine = True
                    count = 0
                    # print("Price List = ", priceList)   # Test Print


        elif isNumItemLine == True:
            # print("Num Item Line")      #Test print

            numItems = int(line)            # set the number of Items variable
            priceList = []                  # initalize price/weight list  
            familyList = []                 # initalize family list  
            isNumItemLine = False           # setting isNumItemLine = false; No longer on numItem Line of Testcase
            isPriceWeightLine = True 

        else:
            print("I'm lost")
        
        # elif isNextTestCase == True:
        #     isNextTestCase = False
        #     print("At next Test case")
        #     isNumItemLine = True
            
        # *********Testing *********
            # for i in range(0, numItems):    # Assign Item Price & Weight 
            #     column = []                 # source: https://www.ict.social/python/basics/multidimensional-lists-in-python
            #     for j in range(0, numItems):
            #         column.append(line)
            #     priceList.append(column)

        # *********Testing *********

            

        # print("Current Line Number = ", currentLine)     #test print
        currentLine += 1                    # Increment current line



        # line = line.split()     #Gets rid of blank space
        # testArray = line        #Assign testArray to line
    
    # print("numTestCases = ", numTestCases)         #test print
    # print("numItems = ", numItems)                  #test print
    # print("isNumItemLine = ", isNumItemLine)         #test print
    # print("Current Line Number = ", currentLine)     #test print

    # print("Price List = ", priceList)
    # print("Family List = ", familyList)

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
