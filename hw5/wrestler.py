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

# ********************************

#       Program Variables 
# ********************************
lineCount = 1
numOfWrestlers = -99
numOfRivalries = -99

impossibleSolution = False     # Boolean: If Impossible Solution

babyfaces = []                  # Empty List for Babyfaces
heels = []                      # Empty List for Heels

wrestlerNamesUnassigned = []    # Empty List for Unassigned Wrestlers
rivalryPairsDictionary = {}               # Dictionary for Rivalry Pairs

tempRivalsList = []             # Testing This list to store the strings of the rivalries

# Testing wrester list ; contains objects of type wrestler
wrestlerList = []

rivalList1 = []     #trying to put rivals into a list since having trouble with dictionary
rivalList2 = []     

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
            
            # if lineCount == 2:                                      # Assign 1st Wrestler to BabyFace Squad
            #     babyfaces.append(line)
       
        elif (lineCount > numOfWrestlers + 2) and (lineCount < numOfWrestlers + numOfRivalries + 3):   # Add to RivalryPair Dictionary
            # print(line)
            # print("Line Count", lineCount)
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
    tempIndex = getWrestlerListIndex(name)
    
    if wrestlerList[tempIndex].group == "babyfaces":
        return True
    else:
        return False

# Returns True if wrestler name is in the heels list
def isHeel(name):
    tempIndex = getWrestlerListIndex(name)
    
    if wrestlerList[tempIndex].group == "heels":
        return True
    else:
        return False

# Returns the Index of Where the wrestler is in the Wrestler List
def getWrestlerListIndex(name):
    for i in wrestlerList:
        if name == i.name:
            return wrestlerList.index(i)

# Returns True if name is a Key in Rival Pair Dictionary
def isKeyInRivalPairDictionary(name):
    # list out keys and values separately 
    key_list = list(rivalryPairsDictionary.keys()) 
    val_list = list(rivalryPairsDictionary.values()) 
    if name in key_list:
        return True
    else: 
        return False

# This function loops and adds all rivals to each wrestler in the wrestler list
def addRivalries():
    tempRivalListIndex = -1
    isRivalList1 = True
    
    for i in range(len(rivalList1)):
        tempIndex = getWrestlerListIndex(rivalList1[i])
        wrestlerList[tempIndex].rivals.append(rivalList2[i])  # append rivalry to wrestler object 

    for i in range(len(rivalList2)):
        tempIndex = getWrestlerListIndex(rivalList2[i])
        wrestlerList[tempIndex].rivals.append(rivalList1[i])

# ************************************************************************************************
# Breath First Search
# Some code taken from Chapter 6 Breadth-First Search From Grokking Alogrithms
# ************************************************************************************************s

def BFS(name):
    count = 1
    search_queue = deque()  # Create a queue to search wrestlers
    # search_queue += rivalList1
    search_queue.append(name)
    searched = []       # Keep track of which wrestlers I've already searched
    global impossibleSolution       # let function know that this is a global variable

    while search_queue:     # while search_queue is not empty
        print("current queue", search_queue)     # Test Print
        # print("size of search queue", len(search_queue))    # Test Print
        person = search_queue.popleft()
        print("Wrestler currently being searched:", person)     # Test Print
        if person not in searched:
            tempIndex = getWrestlerListIndex(person)
            for i in wrestlerList[tempIndex].rivals:        # Add Rivals to Search Queue
                if i not in searched:
                    search_queue.append(i)

            if count == 1:                      # This is the first wrestler; assign babyface
                # print(person, "is the first wrestler. Assigning Babyfaces\n")    #Test print
                wrestlerList[tempIndex].group = "babyfaces"
                wrestlerList[tempIndex].assigned = True
            
            else:
                # Need to check if person/wrestler is assigned a group
                if wrestlerList[tempIndex].assigned == False:
                    # Check rivals to see if they are assigned

                    for j in wrestlerList[tempIndex].rivals:                    # gets list of rivals
                        tempRivalIndex = getWrestlerListIndex(j)

                        if wrestlerList[tempRivalIndex].assigned == True:       #Check if rival is already assigned
                            
                            if isBabyface(wrestlerList[tempRivalIndex].name) :   # if rival is babyface then assign heel 
                                if (wrestlerList[tempIndex].group == wrestlerList[tempRivalIndex].group):
                                    impossibleSolution = True
                                else:
                                    print(person, "'s rival", wrestlerList[tempRivalIndex].name, "is a babyface")    #Test print
                                    print(person, " is being assigned heels\n")    #Test print
                                    wrestlerList[tempIndex].group = "heels"
                            elif isHeel(wrestlerList[tempRivalIndex].name) :
                                if (wrestlerList[tempIndex].group == wrestlerList[tempRivalIndex].group):
                                    impossibleSolution = True
                                else:
                                    print(person, "'s rival", wrestlerList[tempRivalIndex].name, "is a heel")    #Test print
                                    print(person, " is being assigned babyfaces\n")    #Test print
                                    wrestlerList[tempIndex].group = "babyfaces"
                            # else:
                            #     print(person, "'s rival", wrestlerList[tempRivalIndex].name,
                            #             "is neither baby or heel")               #Test print 
                            #     global impossibleSolution       # let function know that this is a global variable
                            #     impossibleSolution = True
                            
                            wrestlerList[tempIndex].assigned = True

                        


                                
            # # Quick test print of current stats 
            print("\n*****************************************")
            print("Wrestler:", wrestlerList[tempIndex].name)    #Test print
            print("Group:", wrestlerList[tempIndex].group)    #Test print
            print("Rivals:", wrestlerList[tempIndex].rivals)    #Test print
            print("Assigned:", wrestlerList[tempIndex].assigned)    #Test print
            print("*****************************************\n")
            searched.append(person)
            count += 1

        elif len(search_queue) == 0:          # Check for any unconnected rivalries
            # print("length of search queue is 0")    #Test print
            count = 1                       # Set Count to 1 so that we can set first new vertex to babyface
            for i in wrestlerList:
                if i.assigned == False:
                    # print(i.name)               #Test print
                    search_queue.append(i.name)

# ************************************************************************************************
# ********************************  Main Code  ***************************************************
# ************************************************************************************************

# Create and Add Wrestler Objects To List
for i in wrestlerNamesUnassigned: 
    wrestlerList.append(Wrestler(i))

addRivalries()

startingVertex = wrestlerList[0].name
BFS(startingVertex)

# print("\n\n*****************************************")
# for i in wrestlerList:
#     print("Name" ,i.name, "Group", i.group)
#     print("Rivals", i.rivals)
#     print("Assigned", i.assigned)
#     print()

for i in wrestlerList:
    if i.group == "babyfaces":
        babyfaces.append(i.name)
    elif i.group == "heels":
        heels.append(i.name)
    else:
        print("We have a problem here")


if impossibleSolution:
    print("Impossible")
else:
    # Yes Possbile
    print("Yes Possible")

    # This are the babyfaces 
    print("Babyfaces: ", sep=" ", end="")        #Need to change into "Babyfaces: Bear Maxx Duke"; Current Output -> Babyfaces: ['Bear']
    for i in babyfaces:
        print(i, sep=" ", end=" ")
    print()                             # print newline for formatting

    # This are the heels 
    print("Heels:", sep=" ", end=" ")
    for i in heels:
        print(i, sep=" ", end=" ")
    print()                             # print newline for formatting