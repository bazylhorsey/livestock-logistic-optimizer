import numpy as np
import pandas as pd

import gurobipy as gp
from gurobipy import GRB

# Parameters

distances_frame = pd.read_csv("data/test/distance.csv", header=None)
brooders_frame = pd.read_csv("data/test/brooder.csv")
finishers_frame = pd.read_csv("data/test/finisher.csv")

brooder_capacity = []
for index, row in brooders_frame.iterrows():
    brooder_capacity.append(row[0])

finisher_capacity = []
finisher_distance_k = []
for index, row in finishers_frame.iterrows():
    finisher_capacity.append(row[0])
    finisher_distance_k.append(row[1])

distances = {}
for f, row in distances_frame.iterrows():
    for b in range(0, len(row)):
        distances[(b, f)] = row[b]
edge, distance = gp.multidict(distances)

NUM_OF_BROODERS = len(brooder_capacity)
NUM_OF_FINISHERS = len(finisher_capacity)
BK = 6.715
FK = 2.944

# MIP  model formulation

m = gp.Model("brooder_allocation")

x = m.addVars(NUM_OF_BROODERS, NUM_OF_FINISHERS, vtype=GRB.BINARY, name="X")
m.addConstrs(
    (
        gp.quicksum(x[b, f] for b in range(NUM_OF_BROODERS)) == 1
        for f in range(NUM_OF_FINISHERS)
    ),
    name="Assignment",
)
m.addConstrs(
    (
        gp.quicksum(
            FK * finisher_capacity[f] * x[b, f] for f in range(0, NUM_OF_FINISHERS)
        )
        >= BK * brooder_capacity[b]
        for b in range(0, NUM_OF_BROODERS)
    ),
    name="Capactiy",
)
m.setObjective(
    (
        FK
        * gp.quicksum(
            distances[b, f] * x[b, f]
            for b in range(NUM_OF_BROODERS)
            for f in range(NUM_OF_FINISHERS)
        )
    ),
    GRB.MINIMIZE,
)


m.optimize()
vals = m.getAttr("x", x)
selected = gp.tuplelist((i, j) for i, j in vals.keys() if vals[i, j] == 1.0)
df = pd.DataFrame(np.zeros((NUM_OF_FINISHERS, NUM_OF_BROODERS)))
vals = m.getAttr("x", x)
selected = gp.tuplelist((i, j) for i, j in vals.keys() if vals[i, j] > 0)
for i in selected:
    print(selected)
    df.at[i[1],i[0]]=distances.get(i,j) * FK
df
m.write("out.sol")
