# Tuan Tran
# CS325 Assignment 3
# Problem 4 Shopping Spree


# This function creates item/weight matrix; takes in the item price weight and the family carrying weight list and returns a matrix

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

# This function takes in the item Price/Weight List, the family max carrying weight list and the matrix of values and writes to results.txt file
def itemsCarried(priceWeightList,familyWeightList, matrix):

    totalPrice = 0
    rows = ( len(matrix) )  # Get total number of items; Add 1 so we can start counting from 1

    # Need to separate price and weight into separate lists
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

    # Write to Total Price results file
    with open('results.txt', 'a') as filehandle:
        filehandle.write("Total Price ") 
        filehandle.write(str(totalPrice))
        filehandle.write('\n')      #After array has been written to txt file then add a newline character
        filehandle.write("Member Items:\n")

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

        # Write Items Carried by Family Members results file
        with open('results.txt', 'a') as filehandle:
            filehandle.write(str(count))
            filehandle.write(": ")
            for i in itemsCarried[::-1]:
                filehandle.write(str(i))
                filehandle.write(" ")
            filehandle.write('\n') 
        count += 1

    with open('results.txt', 'a') as filehandle:        #added extra newline for formatting 
            filehandle.write('\n') 

    # This function converts item price weight list from string to int then calls the createMatrix function and the itemsCarried function
def shoppingSpreeOptimization(itemPriceWeightList, familyWeightList):
    tempList = []
    # Convert itemPriceWeightList from "string" to "int"
    for i in range(len(itemPriceWeightList)):
        for j in itemPriceWeightList[i]:
            temp = int(j)
            tempList.append(temp)

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
with open('results.txt', 'w') as filehandle:
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
            
        elif isFamilyWeightLine == True:    # On line for Individal Family Weight Capacities
            if count < familySize:
                line = int(line)
                familyWeightList.append(line)
                count += 1
                if count == familySize:
                    isFamilyWeightLine = False
                    isNumItemLine = True
                    count = 0
                    testCaseCount += 1

                # Need to do optimization here **********************************
                # Write array to file
                    with open('results.txt', 'a') as filehandle:
                        filehandle.write("Test Case ")
                        filehandle.write(str(testCaseCount))
                        filehandle.write('\n')      # add a newline character
                    shoppingSpreeOptimization(itemPriceWeightList,familyWeightList)
                # ********************************************************************

        elif isFamilySizeLine == True:      # On line where give you How Many Family Members in Test Case
            isFamilyWeightLine = True       # Next line will be Individal Family Weight Capacities
            isFamilySizeLine = False
            familySize = int(line)          # Assign Family Size Value

        elif isPriceWeightLine == True:   
            if count < numItems:
                line = line.split()             # Splits the Price and Weight i.e. 77 7 thats on the same line
                itemPriceWeightList.append(line)          # Assign Item Price & Weight 

                count += 1
                if count == numItems:
                    isPriceWeightLine = False
                    isFamilySizeLine = True
                    count = 0


        elif isNumItemLine == True:
            numItems = int(line)            # set the number of Items variable
            itemPriceWeightList = []                  # initalize item price/weight list  ; or resets for next test case
            familyWeightList = []           # initalize family weight list  ; or resets for next test case
            isNumItemLine = False           # setting isNumItemLine = false; No longer on numItem Line of Testcase
            isPriceWeightLine = True 

        currentLine += 1                    # Increment current line