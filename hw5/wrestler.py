# Tuan Tran
# Homework 5
# Problem 3
# 11/8/19

import sys

#       Program Variables 
# ********************************
lineCount = 1
numOfWrestlers = -99
numOfRivalries = -99

babyfaces = []  #Empty List for Babyfaces
heels = []      #Empty List for Heels

wrestlerNamesUnassigned = [] #Empty List for Unassigned Wrestlers

# ********************************

# Read in contents of input text file
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()             #Remove any newline characters
        if lineCount == 1:
            numOfWrestlers = line       # Assign numOfWrestlers and convert to int
            numOfWrestlers = int(numOfWrestlers)

        elif lineCount == numOfWrestlers + 2:   
            numOfRivalries = line       # Assign numOfRivalries and convert to int
            numOfRivalries = int(numOfRivalries)

        elif (lineCount > 1) and (lineCount < numOfWrestlers +2):   # Dealing with Wrestler Names Before Pair/Rivalry
            wrestlerNamesUnassigned.append(line)                    # Assign all Wrestlers to Unassigned Squad List
            
            if lineCount == 2:                                      # Assign 1st Wrestler to BabyFace Squad
                babyfaces.append(line)
       
        lineCount += 1                  # Increment Line Count To Know Where We Are In File

print(numOfWrestlers)
print(numOfRivalries)
print(babyfaces)

#Sample
# with open(sys.argv[1], 'r') as f:
#     contents = f.read()
#     print("Line Count ", lineCount)
#     lineCount += 1
# print(contents)