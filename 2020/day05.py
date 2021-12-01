"""Day 5"""
from typing import Tuple, List, Dict
from math import ceil
INS = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

Seat = Tuple[int, int]

coor = {'F': 0, 'B': 1, 'L': 0, 'R': 1}


def get_seat(raw: str) -> Seat:
    row_coor = [coor[c] for c in raw[:7]]
    col_coor = [coor[c] for c in raw[7:]]
    r = find_coor(128, row_coor)
    c = find_coor(8, col_coor)
    return (r, c)


def find_coor(length: int, cmd: List[int]) -> int:
    coors = list(range(length))
    for c in cmd:
        mid = ceil(len(coors) / 2)
        coors = [coors[:mid], coors[mid:]][c]
    return coors[0]


def parse(raw: str) -> List[Seat]:
    seats = []
    for line in raw.split('\n'):
        seats.append(get_seat(line.strip()))
    return seats[:-1]


seats = parse(INS)
print(seats)

with open('data/day05.txt') as f:
    seats = parse(f.read())
    print(max(s[0] * 8 + s[1] for s in seats))

# Part II
with open('data/day05.txt') as f:
    seats = parse(f.read())
    all_seats = [r * 8 + c for r in range(128) for c in range(8)]
    taken_seats = [s[0] * 8 + s[1] for s in seats]
    empty = [seat for seat in all_seats if seat not in taken_seats]
    print(empty)
