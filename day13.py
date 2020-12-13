""" Day 13 - inspired by Joel Grus"""

from typing import List, Tuple
from functools import reduce


# Solution
def get_earliest_bus(buses: List[int], after: int) -> int:
    timestamp = after
    while True:
        for bus in buses:
            if timestamp % bus == 0:
                return (timestamp - after) * bus
        timestamp += 1
    return None


def parse(raw: str) -> Tuple[int, List[int]]:
    lines = raw.split('\n')
    after = int(lines[0].strip())
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    return buses, after


# Part II
def get_coin(buses: List[str]):
    inds = [(i, int(bus)) for i, bus in enumerate(buses) if bus != 'x']
    factors = [(bus, (bus - i) % bus) for i, bus in inds]
    divs, rems = zip(*factors)
    return int(chinese_remainder(divs, rems))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def parse2(raw: str) -> List[str]:
    line = raw.split('\n')[1]
    return [bus for bus in line.split(',')]


# Tests
IN = """939
7,13,x,x,59,x,31,19"""

buses, after = parse(IN)
assert get_earliest_bus(buses, after) == 295

buses = parse2(IN)
assert get_coin(buses) == 1068781
# Results

with open('data/day13.txt') as f:
    data = f.read()
    buses, after = parse(data)
    print(get_earliest_bus(buses, after))

    buses = parse2(data)
    print(get_coin(buses))
