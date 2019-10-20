
# Need to create item/weight matrix 
# weights as the rows and item # as column
# currently passing in list as [item1Price, item1Weight, item2Price, item2Weight, ....]
def createMatrix(priceWeightList, familyWeightList):
    # print("This is my matrix list", priceWeightList)    #test print
    columns = max(familyWeightList)        # Find max weight for the Family List
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
    print("Price", price)
    print("Weight", weight)

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
                 matrix[i][j] = max(price[i] + matrix[i-1][j-weight[i]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
            
            # for k in range(1, rows):
            #     if familyWeightList[i] <= i:
            #         if  

    print("Matrix = ",matrix)                            # Test Print
    # print("Matrix Length aka Items= ", len(matrix))      # Test print; Finding out if weight goes from 0 to max weight

tempPriceWeightList = [32, 16, 43, 12, 26, 4, 50, 8, 20, 3, 27, 9]
tempFamilyWeightList = [25, 23, 21, 19]



# Main Code
createMatrix(tempPriceWeightList, tempFamilyWeightList)

# print("PriceWeightList Length =", len(tempPriceWeightList))
# print("max family weight =", max(tempFamilyWeightList))