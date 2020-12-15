""" Day 14 """
import re
from itertools import permutations, combinations, product


class Memory:
    def __init__(self):
        self.mem = {}

    def write_memory(self, mask, value, loc):
        val = bin(value).replace('0b', '')
        res = ''
        for _ in range(len(mask) - len(val)):
            val = '0' + val
        for i, m in enumerate(mask):
            if m == 'X':
                res += val[i]
            else:
                res += m
        self.mem[loc] = int(res, 2)


def parse(raw):
    lines = []
    for line in raw.split('\n'):
        if len(line) > 0:
            lines.append(line)
    return lines


def run(memory, lines):
    mask = ''
    for line in lines:
        if line.startswith('mask'):
            mask = line[-36:]
        else:
            loc = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
            value = line.split(' = ')[-1]
            memory.write_memory(mask, int(value), loc)
    return memory


# Part II
def get_destinations(mask, address):
    addr = bin(address).replace('0b', '')
    for _ in range(len(mask) - len(addr)):
        addr = '0' + addr
    new = ''
    for i, m in enumerate(mask):
        if m == '0':
            new += addr[i]
        else:
            new += m
    combs = []
    comb_count = new.count('X')
    for vals in product(*[['0', '1'] for _ in range(comb_count)]):
        temp = new
        for val in vals:
            temp = temp.replace('X', str(val), 1)
        combs.append(int(temp, 2))
    return combs


def run2(lines):
    mem = {}
    mask = ''
    for line in lines:
        if line.startswith('mask'):
            mask = line[-36:]
        else:
            loc = re.search(r"\[([A-Za-z0-9_]+)\]", line).group(1)
            value = line.split(' = ')[-1]
            for dest in get_destinations(mask, int(loc)):
                mem[dest] = int(value)
    return mem


# Tests
IN = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

IN2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

memory = Memory()
memory = run(memory, parse(IN))
assert sum(memory.mem.values()) == 165
mem = run2(parse(IN2))
assert sum(mem.values()) == 208

with open('data/day14.txt') as f:
    lines = parse(f.read())
    memory = Memory()
    memory = run(memory, lines)
    print(sum(memory.mem.values()))

    mem = run2(lines)
    print(sum(mem.values()))
