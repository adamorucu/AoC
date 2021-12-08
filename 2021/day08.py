#!/usr/bin/python
text = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""

text = open('data/8.in').read()[:-1]


## Part 1
c1 = 0
poss = set()
for line in text.split('\n'):
    p1, p2 = line.split(' | ')
    p2 = p2.split()
    for d in p2:
        poss.add(''.join(sorted(d)))
        if len(d) in [2, 4, 3, 7]:
            c1 += 1
print(c1)


## Part 2
def find_map(inp):
    inp = sorted(inp, key=lambda x: len(x))
    m = {}
    m[1] = inp[0]
    m[4] = inp[2]
    m[7] = inp[1]
    m[8] = inp[9]
    for i in [9, 2, 1, 0]:
        del inp[i]

    fivetwo = []
    for d in inp:
        if len(d) == 6:
            if all(a in d for a in m[4]):
                m[9] = d
            elif all(a in d for a in m[7]):
                m[0] = d
            else:
                m[6] = d
        else:
            if all(a in d for a in m[7]):
                m[3] = d
            else:
                fivetwo.append(d)
    
    for d in fivetwo:
        if all(a in m[9] for a in d):
            m[5] = d
        else:
            m[2] = d
    return {''.join(sorted(v)): k for k, v in m.items()}

sum = 0
for line in text.split('\n'):
    p1, p2 = line.split(' | ')
    p1 = p1.split()
    m = find_map(p1)
    p2 = p2.split()
    out = 0
    for i, d in enumerate(reversed(p2)):
        out += m[''.join(sorted(d))] * 10**i
    sum += out
print(sum)
