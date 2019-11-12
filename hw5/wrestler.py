# Tuan Tran
# Homework 5
# Problem 3
# 11/8/19

import sys
from collections import deque   # use a queue

# Create a Wrestle Class
class Wrestler: 
    def __init__(self, name, group="None", assigned=False):
        self.name = name
        self.group = group
        rivals = []
        assigned = False

#   This function takes a string of 2 wrestlers
#   splits the string and adds to the rivalryPairs dictionary
# ********************************
def addToRivalryPairDictionary(s , tempDictionary):
    # print(s)    # Test Print
    s1 = ""     # Empty String 1
    s2 = ""     # Empty String 2
    count = 1

    for i in s.split():
        if count == 1:
            s1 = i 
        else:
            s2 = i
        count += 1

    tempDictionary.setdefault(s1, [])   # Allow key/value pair to hold more than 1 value; sets values as a list instead of just 1 key to 1 pair
    tempDictionary[s1].append(s2)
    # print(s1)   # Test Print
    # print(s2)   # Test Print
    # print("*****")  # Test Print

#   This function takes a dictonary of wrestler as input 
#   and assigns wrestlers to either babyfaces or heel group 
# ********************************
def determineBabyOrHeel(tempRivalPairDictionary, tempBabyfacesList, tempHeelsList):
    # print("Determine Baby Or Heel Function")  # Test Print

    # print("Rival Pair Dictionary", tempRivalPairDictionary)     # Test Print
    # print("How many wrestlers", len(tempRivalPairDictionary))   # Test Print

    # Start with first babyface
    print(tempBabyfacesList[0])

    # print out value (aka rival) of first babyface in Dictionary
    tempRivalsName = str( tempRivalPairDictionary.get(tempBabyfacesList[0]) ) 
    tempRivalsName = tempRivalsName[2:-2]       # Remove first 2 characters and last 2 character; Ex. ['Samson'] -> Samson
    print(tempRivalsName)         # Test Print

    print(tempBabyfacesList[0], "'s Rival is = ", tempRivalsName)   # Test Print



# ********************************

#       Program Variables 
# ********************************
lineCount = 1
numOfWrestlers = -99
numOfRivalries = -99

impossibleSolution = False      # Bool: If Impossible Solution

babyfaces = []                  # Empty List for Babyfaces
heels = []                      # Empty List for Heels

wrestlerNamesUnassigned = []    # Empty List for Unassigned Wrestlers
rivalryPairsDictionary = {}               # Dictionary for Rivalry Pairs

# Testing wrester list ; type wrestler
wrestlerList = []

# ********************************

# Read in contents of input text file
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()             # Remove any newline characters
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
       
        elif (lineCount > numOfWrestlers + 2) and (lineCount < numOfWrestlers + numOfRivalries + 3):   # Add to RivalryPair Dictionary
            # print(line)
            # print("Line Count", lineCount)
            addToRivalryPairDictionary(line, rivalryPairsDictionary)    # Add Wrestlers from File to Rival Dictionary

        lineCount += 1                  # Increment Line Count To Know Where We Are In File

# print(numOfWrestlers)     # Test Print
# print(numOfRivalries)     # Test Print
# print(babyfaces)          # Test Print
# print(wrestlerNamesUnassigned)    # Test Print
# print(rivalryPairsDictionary)   # Test Print


def BFS(name):
    print("This is BFS")

    search_queue = deque()  # Create a queue to search wrestlers
    search_queue += rivalryPairsDictionary[name]    # Add all the neighbors/rivals into the search_queue
    print(search_queue)

    searched = []       # Keep track of which wrestlers I've already searched

    while search_queue:     # while search_queue is not empty
        # print(search_queue)  
        person = search_queue.popleft()
        
        if person not in searched: # only search this wrestler/person if you haven't searched for them yet
            if True:            # need to assign either babyface or heel
                print("Do something")
            else:                # Else add this person's/wrestler's neighbors to the search queue
                search_queue += rivalryPairsDictionary[person]
                searched.append(person)         # Add person/wrestler to already searched
                print("Doing something else")

# Main Code

# determineBabyOrHeel(rivalryPairsDictionary, babyfaces, heels)

# Create and Add Wrestler Objects To List
for i in wrestlerNamesUnassigned: 
    wrestlerList.append(Wrestler(i))

BFS(wrestlerList[0].name)

# print(wrestlerList[0].name)     # Test Print
# print(wrestlerList[0].group)     # Test Print

# for i in wrestlerList:
#     print(i.name, type(i))      # Test Print


# if (impossibleSolution == True):
#     print("Impossible")
# else:
#     # Yes Possbile
#     print("Yes Possible")

#     # This are the babyfaces 
#     print("Babyfaces: ", sep=" ", end="")        #Need to change into "Babyfaces: Bear Maxx Duke"; Current Output -> Babyfaces: ['Bear']
#     for i in babyfaces:
#         print(i, sep=" ", end="")
#     print()                             # print newline for formatting

#     # This are the heels 
#     print("Heels:", sep=" ", end="")
#     for i in heels:
#         print(i, sep=" ", end="")
#     print()                             # print newline for formatting