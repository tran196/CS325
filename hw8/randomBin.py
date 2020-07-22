import random

random.seed()

# python program to generate random items for bin packing

#generate num of test cases
numTestCase = random.randint(20, 1000)

print(numTestCase)

for i in range(numTestCase):
    print(random.randint(10, 30))   # random bin capacity
    
    numItems = random.randint(10, 50)   # random number of items
    print(numItems)

    for j in range(numItems):   # generate item weights
        print(random.randint(1,20), end=" ")     #generate random item weights

    print()

