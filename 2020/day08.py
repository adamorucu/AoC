""" Day 8 """
from typing import Dict, Tuple, List

IN = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

Instruction = Tuple[str, int]
BootCode = List[Instruction]


def parse(raw: str) -> BootCode:
    boot_code = []
    for line in raw.split('\n'):
        if len(line) >= 1:
            op, arg = line.strip().split(' ')
            boot_code.append((op, int(arg)))
    return boot_code


def find_loop(code: BootCode) -> int:
    visited = set()
    line = 0
    acc_val = 0
    while True:
        if line in visited:
            break
        visited.add(line)
        op, arg = code[line]
        if op == 'nop':
            pass
        elif op == 'acc':
            acc_val += arg
        elif op == 'jmp':
            line += arg
            continue
        else:
            raise ValueError()
        line += 1
    return acc_val


with open('data/day08.txt') as f:
    code = parse(f.read())
    print(find_loop(code))


# Part II
def run_program(code: BootCode) -> int:
    visited = set()
    line = 0
    acc_val = 0
    while True:
        if line in visited:
            return None
        if line >= len(code):
            return acc_val
        visited.add(line)
        op, arg = code[line]
        if op == 'nop':
            pass
        elif op == 'acc':
            acc_val += arg
        elif op == 'jmp':
            line += arg
            continue
        else:
            raise ValueError()
        line += 1
    return None


def fix_program(code: BootCode) -> int:
    for i, (op, arg) in enumerate(code):
        tmp = code[:]
        if op == 'nop':
            tmp[i] = ('jmp', arg)
        elif op == 'jmp':
            tmp[i] = ('nop', arg)
        else:
            continue
        res = run_program(tmp)
        if res != None:
            return res
    return None


with open('data/day08.txt') as f:
    code = parse(f.read())
    print(fix_program(code))
