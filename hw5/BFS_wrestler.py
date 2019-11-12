# Tuan Tran
# Homework 5
# Problem 3
# 11/8/19

import sys
from collections import deque   # use a queue

# Create a Wrestler Class
class Wrestler: 
    def __init__(self, name, group="None", assigned=False):
        self.name = name
        self.group = group
        self.rivals = []
        self.assigned = False

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
# 
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

tempRivalsList = []             # Testing This list to store the strings of the rivalries

# Testing wrester list ; contains objects of type wrestler
wrestlerList = []

rivalList1 = []     #trying to put rivals into a list since having trouble with dictionary
rivalList2 = []     

# ****************************************************************

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
            # print(line)                       # Test Print
            # print("Line Count", lineCount)    # Test Print
            tempRivalsList.append(line)                                 # storing rivalries into a string list to later be broken up/parsed
            addToRivalryPairDictionary(line, rivalryPairsDictionary)    # Add Wrestlers from File to Rival Dictionary

        lineCount += 1                  # Increment Line Count To Know Where We Are In File

# print(numOfWrestlers)     # Test Print
# print(numOfRivalries)     # Test Print
# print(babyfaces)          # Test Print
# print(wrestlerNamesUnassigned)    # Test Print
# print(rivalryPairsDictionary)   # Test Print

# Parsing through tempRivalsList and braking string up into 2 lists: rivalsList1 and rivalsList2
for i in tempRivalsList:
    tempCount = 0
    for j in i.split():
        if tempCount == 0:
            rivalList1.append(j)
        else:
            rivalList2.append(j)
        tempCount += 1

# Returns True if wrestler name is in the babyface list
def isBabyface(name):
    if name in babyfaces:
        return True
    else:
        return False

# Returns True if wrestler name is in the heels list
def isHeel(name):
    if name in heels:
        return True
    else:
        return False

# Returns the Index of Where the wrestler is in the Wrestler List
def getWrestlerListIndex(name):
    for i in wrestlerList:
        if name == i.name:
            return wrestlerList.index(i)

def isKeyInRivalPairDictionary(name):
    # list out keys and values separately 
    key_list = list(rivalryPairsDictionary.keys()) 
    val_list = list(rivalryPairsDictionary.values()) 
    if name in key_list:
        return True
    else: 
        return False
        
# ************************************************************************************************
# Breath First Search
# Some code taken from Chapter 6 Breadth-First Search From Grokking Alogrithms
# ************************************************************************************************s

def BFS():

    search_queue = deque()  # Create a queue to search wrestlers
    search_queue += rivalList1

    searched = []       # Keep track of which wrestlers I've already searched

    while search_queue:     # while search_queue is not empty
        # print(search_queue)     # Test Print
        person = search_queue.popleft()
        if person not in searched:
            tempIndex = getWrestlerListIndex(person)
            if wrestlerList[tempIndex].assigned == False:    # Wrestler is not assigned; need to assign rivals and babyface/heel
                print(person)
                if isKeyInRivalPairDictionary(person):      # Make sure Wrestler is a Key in the RivalPair Dictionary
                    for i in rivalryPairsDictionary[person]:
                        wrestlerList[tempIndex].rivals.append(i)    # Assigning Rivals
                    
                    for j in wrestlerList[tempIndex].rivals:        # Assigning Groups: babyfaces/heels
                        if isBabyface(j):
                            wrestlerList[tempIndex].group = "heels"
                        elif isHeel(j):
                            wrestlerList[tempIndex].group = "babyfaces"
                        tempRivalIndex = getWrestlerListIndex(j)
                        if wrestlerList[tempRivalIndex].assigned == False:
                            search_queue.append(j)
                else:                                       # Wrestler is a Value and not a Key in the RivalPair Dictionary
                    print("Do Something", wrestlerList[tempIndex].name)
                    

                wrestlerList[tempIndex].assigned = True
            
            searched.append(person)
   
        
  
        

# ************************************************************************************************
# ********************************  Main Code  ***************************************************
# ************************************************************************************************


# list out keys and values separately 
# key_list = list(rivalryPairsDictionary.keys()) 
# val_list = list(rivalryPairsDictionary.values()) 

# Create and Add Wrestler Objects To List
for i in wrestlerNamesUnassigned: 
    wrestlerList.append(Wrestler(i))

# Fill out data for the first name/wrestler in the list; assign them to babyface squad
wrestlerList[0].group = "babyfaces"
wrestlerList[0].assigned = True
for i in rivalryPairsDictionary[wrestlerList[0].name]:
    wrestlerList[0].rivals.append(i)

# Need to Take Care of the Rival as well
for i in wrestlerList[0].rivals:
    tempIndex = getWrestlerListIndex(i)   
    wrestlerList[tempIndex].group = "heels"
    wrestlerList[tempIndex].assigned = True
    for j in rivalryPairsDictionary[i]:
        wrestlerList[tempIndex].rivals.append(j)


# print(tempRivalsList)   # Test Print


# print(rivalList1)   # Test Print
# print(rivalList2)   # Test Print
# print("**************\n")    # Test Print

# # Prints out wrestlerList with only names assigned
# for i in wrestlerList:
#     print("Name" ,i.name, "Group", i.group)
#     print("Rivals", i.rivals)
#     print("Assigned", i.assigned)

# print("**************\n")

# # # Assign Rivals in Wrestler List
# for i in wrestlerList:
#     print("Name:" ,i.name)
#     if i.name in rivalList1:    # If Name is on the left hand side of the rivalry pair assign rival
#         tempIdx = rivalList1.index(i.name)
#         i.rivals.append(rivalList2[tempIdx])
#     print("Rival of ", i.name, "is ", i.rivals)

# print("index", rivalList1.index("Bear"))

# print(key_list)   # Test Print
# print(val_list)   # Test Print
# print(val_list[1])    # Test Print


#           Print Keys from RivalDictionary
# print(rivalryPairsDictionary.keys())

#           Print Values from RivalDictionary
# print(rivalryPairsDictionary.values())

# ************************************ 
#       Trying BFS 
# ************************************ 

BFS()

# ************************************ 

# print(rivalryPairsDictionary)   # Test Print

# print(wrestlerList[0].name)     # Test Print
# print(wrestlerList[0].group)     # Test Print
# print(wrestlerList[0].rivals)   # Test Print
# print(wrestlerList[0].assigned) # Test Print

# print(wrestlerList[4].name)     # Test Print
# print(wrestlerList[4].group)     # Test Print
# print(wrestlerList[4].rivals)   # Test Print
# print(wrestlerList[4].assigned) # Test Print

# print(wrestlerList[5].name)     # Test Print
# print(wrestlerList[5].group)     # Test Print
# print(wrestlerList[5].rivals)   # Test Print
# print(wrestlerList[5].assigned) # Test Print

# print (isBabyface(wrestlerList[0].name)) # Test Print

for i in wrestlerList:
    print("name:", i.name)      # Test Print
    print(i.group)
    print(i.rivals)
    print(i.assigned)



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