#!/usr/bin/python
from collections import defaultdict
text = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

text = open('data/2.in').read()
data = [t for t in text.split()]

## Part 1
dic = defaultdict(int)
for i in range(0, len(data), 2):
    dic[data[i]] += int(data[i+1])

res = dic['forward'] * (dic['down'] - dic['up'])
print(res)

## Part 2
aim, horz, depth = 0, 0, 0
for i in range(1, len(data), 2):
    x = int(data[i])
    if data[i-1] == 'forward':
        depth += x
        horz += aim*x
    elif data[i-1] == 'down':
        aim += x
    else:
        aim -= x

print(depth*horz)
