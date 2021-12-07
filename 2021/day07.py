#!/usr/bin/python
from collections import defaultdict
text = """16,1,2,0,4,2,7,1,2,14"""

text = open('data/7.in').read()[:-1]

crabs = [int(p) for p in text.split(',')]

def calc_cost(crab, pos):
    return abs(crab - pos)

m = defaultdict(int)
for i in range(max(crabs) - min(crabs) + 1):
    m[i] = sum(range(0, i+1))

min_cost = 9e+10
best_pos = 9e+10
for pos in range(min(crabs), max(crabs)):
    cost = sum([calc_cost(c, pos) for c in crabs])
    if cost < min_cost:
        min_cost = cost
        best_pos = pos

print(min_cost)

def calc_cost2(crab, pos):
    return m[abs(crab - pos)]

min_cost = 9e+10
best_pos = 9e+10
for pos in range(min(crabs), max(crabs)):
    cost = sum([calc_cost2(c, pos) for c in crabs])
    if cost < min_cost:
        min_cost = cost
        best_pos = pos

print(min_cost)
