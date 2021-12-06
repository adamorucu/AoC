#!/usr/bin/python
from collections import defaultdict
text = """3,4,3,1,2"""

text = open('data/6.in').read()[:-1]
school = [int(num) for num in text.split(',')]

grouped = defaultdict(int)
for fish in school:
    grouped[fish] += 1
    
for d in range(256):
    temp = defaultdict(int)
    for fsh, cnt in grouped.items():
        if fsh == 0:
            temp[6] += cnt
            temp[8] = cnt
        else:
            temp[fsh-1] += cnt
    grouped = temp

print(sum(grouped.values()))

