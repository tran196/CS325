# import PuLP
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("ShortestPath", LpMinimize)
