#!/usr/bin/python
import numpy as np
text = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

text = open('data/3.in').read()
l = len(text.split()[0])
l2 = len(text.split())
counts = [0] * l

for line in text.split():
    for i, num in enumerate(line):
        counts[i] += int(num)

bina = [str(round(c/l2)) for c in counts]
gamma = int('0b' + ''.join(bina), 2)

eps = [str(abs(int(b)-1)) for b in bina]
eps = int('0b' + ''.join(eps), 2)
print(gamma* eps)

## Part 2

dt = np.array([list(map(int, list(line))) for line in text.split()])
ox = dt.copy()

for i in range(l):
    o = int(sum(ox[:, i])/len(ox) >= 0.5)
    ox = ox[ox[:, i] == o]
    if len(ox) < 2:
        break

co2 = dt.copy()
for i in range(l):
    c = abs(int(sum(co2[:, i])/len(co2) >= 0.5) - 1)
    co2 = co2[co2[:, i] == c]
    if len(co2) < 2:
        break

oxg = int('0b' + ''.join(map(str, ox[0])) ,2)
co2s = int('0b' + ''.join(map(str, co2[0])) ,2)
print(oxg * co2s)
