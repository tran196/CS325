

# Need to create item/weight matrix 
# weights as the rows and item # as column
# currently passing in list as [item1Price, item1Weight, item2Price, item2Weight, ....]
def createMatrix(priceWeightList, familyWeightList):
    # print("This is my matrix list", priceWeightList)    #test print
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

    # TestPrint
    # print("Price", price)
    # print("Weight", weight)

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

    # Check to see which items are included/carried for each family member 
    
    for individualWeight in familyWeightList:
        print()                                                                     # Test Print
        print("Family Member #", familyWeightList.index(individualWeight) + 1)      #Test Print
        i = rows - 1           # n is total items 
        j = individualWeight
        currentWeightCapacity = individualWeight    #Checking each family member's weight capacity and showing which items they get
        itemsCarried = []       #Empty List for Items Carried

        # print("i = ", i)                    #Test Print
        # print("j = ", j)                    #Test Print
        print("currentWeightCapacity Before Adding Items= ", currentWeightCapacity)        #Test Print
        

        #Iterate through Matrix Bottom to Top
        while i > 0 and j > 0:
            if matrix[i][j] == matrix[i-1][j]:
                i = i - 1
            else:
                # print("i = ", i)
                itemsCarried.append(i)
                print("Item ", i, "Carried")            #Test Print
                print("Currently at Matrix[",i,"]","[",j,"] = ", matrix[i][j], sep="")            #Test Print
                print("Weight[", i, "] = ", weight[i], sep="")          #Test Print
                currentWeightCapacity = currentWeightCapacity - weight[i]
                
                j = j - weight[i]
                i = i - 1
                
                print("currentWeightCapacity = ", currentWeightCapacity)        #Test Print
        print("Items carried:", itemsCarried)           #Test Print

    

    # # print("Matrix = ",matrix)                            # Test Print
    # print("Matrix Num Rows aka Items= ", len(matrix))       # Test Print
    # print("Matrix Num Col aka Weights= ", len(matrix[0]))   # Test Print
    # print("Matrix Length aka Items= ", len(matrix))      # Test print; Finding out if items goes from 0 to total items (added 1 earlier)

    print("Matrix[6][25] = ",matrix[6][25])                            # Test Print
    print("Matrix[6][25] = ",matrix[6][23])                            # Test Print
    print("Matrix[6][25] = ",matrix[6][21])                            # Test Print
    print("Matrix[6][25] = ",matrix[6][19])                            # Test Print

tempPriceWeightList = [32, 16, 43, 12, 26, 4, 50, 8, 20, 3, 27, 9]
tempFamilyWeightList = [25, 23, 21, 19]



# Main Code
createMatrix(tempPriceWeightList, tempFamilyWeightList)

# print("PriceWeightList Length =", len(tempPriceWeightList))
# print("max family weight =", max(tempFamilyWeightList))