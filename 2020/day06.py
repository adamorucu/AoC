""" Day 6 """
from typing import Set, List
IN = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def get_group(group: str) -> Set:
    answers = []
    for person in group.split('\n'):
        answers += list(person)
    return set(answers)


def parse(raw: str) -> List[Set]:
    groups = []
    for group in raw.split('\n\n'):
        groups.append(get_group(group))
    return groups


assert sum(len(g) for g in parse(IN)) == 11

with open('data/day06.txt') as f:
    groups = parse(f.read())
    print(sum(len(g) for g in groups))


# Part II
def get_group2(group: str) -> Set:
    answers = ''.join(list(group.split('\n')))
    size = len(group.strip().split('\n'))
    return {a for a in set(answers) if answers.count(a) == size}


def parse2(raw: str) -> List[Set]:
    groups = []
    for group in raw.split('\n\n'):
        groups.append(get_group2(group))
    return groups


assert sum(len(g) for g in parse2(IN)) == 6

with open('data/day06.txt') as f:
    groups = parse2(f.read())
    print(sum(len(g) for g in groups))
