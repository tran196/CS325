# Tuan Tran
# CS325 Assignment 3
# Problem 4 Shopping Spree


# Need to create item/weight matrix 
# weights as the rows and item # as column
def createMatrix(priceWeightList, familyWeightList):
    columns = max(familyWeightList) + 1       # Find max weight for the Family List; Add 1 to go from 0 to max
    rows = ( len(priceWeightList)//2 ) + 1  # Get total number of items; Add 1 so we can start counting from 1

    # Need to separate price weight list into separate lists
    price = []
    weight = []
    for i in range(len(priceWeightList)):
        if i % 2 == 0:
            price.append(priceWeightList[i])
        else:
            weight.append(priceWeightList[i])

    #Append 0 to beginning of each list
    price.insert(0, 0)
    weight.insert(0, 0)

    # Create 2D list
    # Source: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html

    # rows go from 0 to total number of items 
    # columns = weights from 0 to max(familyWeightList)
    matrix = [ ([0] * columns) for row in range(rows) ] 

    for i in range(rows):           #rows = items from 0 to item 6 (Starts from 1 to 6)
        for j in range(columns):    #columns = weight from 0 to 25; (25 is max of family list)
            if i == 0:
                matrix[0][j] = 0    # 0's for when Item == 0
            elif j == 0:
                matrix[i][0] = 0    #0's when Weight == 0
            elif weight[i] <= j:
                 matrix[i][j] = max( price[i] + matrix[i - 1][j - weight[i]], matrix[i - 1][j] )
            else:
                matrix[i][j] = matrix[i-1][j]

    return matrix

def itemsCarried(priceWeightList,familyWeightList, matrix):

    totalPrice = 0
    rows = ( len(matrix) )  # Get total number of items; Add 1 so we can start counting from 1

    # Need to separate price weight list into separate lists
    price = []
    weight = []
    for i in range(len(priceWeightList)):
        if i % 2 == 0:
            price.append(priceWeightList[i])
        else:
            weight.append(priceWeightList[i])

    #Append 0 to beginning of each list
    price.insert(0, 0)
    weight.insert(0, 0)

    # Add to get Total Price
    for i in familyWeightList:
        temp = matrix[len(price) - 1][i]
        totalPrice = totalPrice + temp
    print("Total Price", totalPrice)    #Test Print
    print("Member Items:")              #Test Print
    # Check to see which items are included/carried for each family member 
    count = 1
    for individualWeight in familyWeightList:
        i = rows - 1           # i is total items 
        j = individualWeight
        currentWeightCapacity = individualWeight    #Checking each family member's weight capacity and showing which items they get
        itemsCarried = []       #Empty List for Items Carried
        
        #Iterate through Matrix Bottom to Top
        while i > 0 and j > 0:
            if matrix[i][j] == matrix[i-1][j]:
                i = i - 1
            else:
                itemsCarried.append(i)
                currentWeightCapacity = currentWeightCapacity - weight[i]
                
                j = j - weight[i]
                i = i - 1
        print(count, ": ", itemsCarried[::-1] , sep="")         #Test Print
        count += 1


        

def shoppingSpreeOptimization(testCaseCount, itemPriceWeightList, familyWeightList):
    totalPrice = 0
    tempList = []
    # Convert itemPriceWeightList from "string" to "int"
    for i in range(len(itemPriceWeightList)):
        for j in itemPriceWeightList[i]:
            temp = int(j)
            tempList.append(temp)
    # print("This is shopping optimization")    #Test print
    # print("Item Price Weight List: ", itemPriceWeightList)            #Test print
    # print("Family Max Weight List: ", familyWeightList)        #Test print
    # print("Test Case ", testCaseCount)        #Test print
    # print("Total Price ", totalPrice)         #Test print

    # print("Temp List: ", tempList)              #Test print    

    matrix = createMatrix(tempList, familyWeightList)
    familyItemsCarried = itemsCarried(tempList, familyWeightList, matrix)




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
with open('shoppingResults.txt', 'w') as filehandle:
    filehandle.write('') 



# Main Code

# Read in Data from shopping.txt
# Source: https://www.w3resource.com/python-exercises/file/python-io-exercise-7.php
with open('shopping.txt') as f:
    currentLine = 0                         # use currentLine to keep track of what line I'm on in file
    count = 0                               # count variable to keep track of certain things
    for line in f:
        if currentLine == 0:
            numTestCases = int(line)        # first line in shoppping.txt used for number of test cases
            isNumItemLine = True            # next line is the number of items in test case
            
        elif isFamilyWeightLine == True:
            # print("Family Weight Line")    #Test print
            if count < familySize:
                # line = line.split()
                line = int(line)
                familyWeightList.append(line)
                count += 1
                if count == familySize:
                    isFamilyWeightLine = False
                    isNumItemLine = True
                    count = 0
                    testCaseCount += 1
                    # print("Family List = ", familyWeightList) # Test Print

                # Need to do optimization here **********************************
                #          # Write array to file
                    # with open('shoppingResults.txt', 'a') as filehandle:
                    #     for k in range(0, len(testArray)):
                    #         filehandle.write(str(testArray[k]))
                    #         filehandle.write(' ')   #Put a space between each number
                    #     filehandle.write('\n')      #After array has been written to txt file then add a newline character
                    print("Test Case ", testCaseCount)        #Test print
                    shoppingSpreeOptimization(testCaseCount, itemPriceWeightList,familyWeightList)
                    
                # ********************************************************************

        elif isFamilySizeLine == True:
            # print("Family Size Line")       #Test print
            isFamilyWeightLine = True
            isFamilySizeLine = False
            familySize = int(line)          # Assign Family Size Value
            # print("Family Size = ", familySize) #Test print


        elif isPriceWeightLine == True:   
            # print("Price/Weight Line")  #Test print
            if count < numItems:
                line = line.split()             # Splits the Price and Weight i.e. 77 7 thats on the same line
                itemPriceWeightList.append(line)          # Assign Item Price & Weight 

                count += 1
                if count == numItems:
                    isPriceWeightLine = False
                    isFamilySizeLine = True
                    count = 0
                    # print("Price List = ", itemPriceWeightList)   # Test Print


        elif isNumItemLine == True:
            # print("Num Item Line")      #Test print

            numItems = int(line)            # set the number of Items variable
            itemPriceWeightList = []                  # initalize item price/weight list  ; or resets for next test case
            familyWeightList = []           # initalize family weight list  ; or resets for next test case
            isNumItemLine = False           # setting isNumItemLine = false; No longer on numItem Line of Testcase
            isPriceWeightLine = True 

        # else:
        #     print("I'm lost")
        


            

        # print("Current Line Number = ", currentLine)     #test print
        currentLine += 1                    # Increment current line



        # line = line.split()     #Gets rid of blank space
        # testArray = line        #Assign testArray to line
    
    # print("numTestCases = ", numTestCases)         #test print
    # print("numItems = ", numItems)                  #test print
    # print("isNumItemLine = ", isNumItemLine)         #test print
    # print("Current Line Number = ", currentLine)     #test print

    # print("Price List = ", priceList)
    # print("Family List = ", familyWeightList)

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
