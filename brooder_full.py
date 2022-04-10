import numpy as np
import pandas as pd

import gurobipy as gp
from gurobipy import GRB

distances_frame = pd.read_csv("data/distance.csv", header=None)
brooders_frame = pd.read_csv("data/brooder.csv")
finishers_frame = pd.read_csv("data/finisher.csv")

brooder_capacity = []
for index, row in brooders_frame.iterrows():
    brooder_capacity.append(row[0])
    
finisher_capacity = []
finisher_distance_k = []
for index, row in finishers_frame.iterrows():
    finisher_capacity.append(row[0])
    finisher_distance_k.append(row[1])
print(finisher_capacity)

distances = {}
for i, row in distances_frame.iterrows():
    for j in range(0, len(row)):
        distances[(i, j)] = row[j]

NUM_OF_BROODERS = len(finisher_capacity)
NUM_OF_FINISHERS = len(finisher_capacity)
BK = 6.715
FK = 2.944

m = gp.Model('brooder_allocation')

x = m.addVars(NUM_OF_BROODERS, NUM_OF_FINISHERS, vtype=GRB.BINARY, name='X')

m.addConstrs((gp.quicksum(x[b][f] for b in range(NUM_OF_BROODERS)) == 1 for f in range(NUM_OF_FINISHERS)), name="Assignment")

# m.addConstrs(
#     (gp.quicksum(FK * finisher_capacity[f] * x[b][f]
#         for f in range(0, NUM_OF_FINISHERS) >= BK * brooder_capacity[b])
#     ) for b in range(0, NUM_OF_BROODERS)
# )   

# m.addConstraint(
#     gp.quicksum(x[b][f] for b in range(0, NUM_OF_BROODERS)) == 1
#         for f in range(0, NUM_OF_FINISHERS)
#     )

m.setObjective((FK * gp.quicksum(distances.get(b,f)*x[b][f]) 
    for b in range(NUM_OF_BROODERS) for f in range(NUM_OF_FINISHERS)), GRB.MINIMIZE)

m.optimize()