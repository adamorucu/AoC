#!/usr/bin/python
from collections import defaultdict
text = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

text = open('data/5.in').read()[:-1]

def segment(line, part2=False):
    one, two = line.split(' -> ')
    x1, y1 = map(int, one.split(','))
    x2, y2 = map(int, two.split(','))
    if x1 == x2:
        diry = int((y2-y1)/abs(y2-y1))
        ys = range(y1, y2+1*diry, diry)
        segment = list(zip([x1] * len(ys), ys))
    elif y1 == y2:
        dirx = int((x2-x1)/abs(x2-x1))
        xs = range(x1, x2+1*dirx, dirx)
        segment = list(zip(xs, [y1] * len(xs)))
    else:
        dirx = int((x2-x1)/abs(x2-x1))
        diry = int((y2-y1)/abs(y2-y1))
        xs = range(x1, x2+1*dirx, dirx)
        ys = range(y1, y2+1*diry, diry)
        segment = list(zip(xs, ys)) if part2 else None
    return segment

## Part 1
d = defaultdict(int)
for line in text.split('\n'):
    seg = segment(line)
    if seg != None:
        for p in seg:
            d[str(p)] += 1

ct = 0
for k, v in d.items():
    if v >= 2:
        ct += 1
print(ct)

## Part 2
d = defaultdict(int)
for line in text.split('\n'):
    seg = segment(line, True)
    if seg != None:
        for p in seg:
            d[str(p)] += 1

ct = 0
for k, v in d.items():
    if v >= 2:
        ct += 1
print(ct)
