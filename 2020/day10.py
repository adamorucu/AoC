""" Day 10 - Inspired by Joel Grus"""
from typing import List, Dict
from collections import Counter

IN = """16
10
15
5
1
11
7
19
6
12
4"""

IN2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def parse(raw: str) -> List[int]:
    adapters = [int(line) for line in raw.split('\n') if len(line) > 0]
    device = max(adapters) + 3
    return [0] + adapters + [device]


def get_differences(jolts: List[int]) -> Dict:
    sorted_jolts = jolts[:]
    sorted_jolts.sort()
    jolt_diffs = [
        sorted_jolts[i + 1] - sorted_jolts[i]
        for i in range(len(sorted_jolts) - 1)
    ]
    counts = Counter(jolt_diffs)
    return counts


def get_prod(jolts: List[int]) -> int:
    diffs = get_differences(jolts)
    return diffs[3] * diffs[1]


# Part II
def get_dist_arrangements(jolts: List[int]) -> int:
    ways2get2 = [0] * (jolts[-1] + 1)
    ways2get2[:2] = [1, 1]
    ways2get2[2] = 2 if 2 in jolts and 1 in jolts else 1 if 2 in jolts else 0

    for i in range(3, max(jolts) + 1):
        if i in jolts:
            ways2get2[i] = sum(ways2get2[i - 3:i])
    return ways2get2[-1]


with open('data/day10.txt') as f:
    jolts = parse(f.read())
    print(get_prod(jolts))
    print(get_dist_arrangements(jolts))
