""" Day 11 - inspired by Joel Grus"""

from typing import List
from collections import Counter

# Solution
Layout = List[List[str]]

neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1],
             [-1, -1]]


def next_round(layout: Layout) -> Layout:
    return [[new_value(i, j, layout) for j in range(len(layout[0]))]
            for i in range(len(layout))]


def new_value(i: int, j: int, layout: Layout) -> str:
    count = Counter([
        layout[i + di][j + dj] for di, dj in neighbors
        if 0 <= i + di < len(layout) and 0 <= j + dj < len(layout[0])
    ])

    if layout[i][j] == 'L' and count['#'] == 0:
        return '#'
    if layout[i][j] == '#' and count['#'] >= 4:
        return 'L'
    return layout[i][j]


def final_taken_seats(layout: Layout) -> int:
    while True:
        new_layout = next_round(layout)
        if new_layout == layout:
            break
        layout = new_layout
    return sum(s == '#' for row in layout for s in row)


# Part II


def next_round2(layout: Layout) -> Layout:
    return [[new_value2(i, j, layout) for j in range(len(layout[0]))]
            for i in range(len(layout))]


def new_value2(i: int, j: int, layout: Layout) -> str:
    count = Counter([
        first_seat(i, j, di, dj, layout) for di, dj in neighbors
        if 0 <= i + di < len(layout) and 0 <= j + dj < len(layout[0])
    ])

    if layout[i][j] == 'L' and count['#'] == 0:
        return '#'
    if layout[i][j] == '#' and count['#'] >= 5:
        return 'L'
    return layout[i][j]


def final_taken_seats2(layout: Layout) -> int:
    while True:
        new_layout = next_round2(layout)
        if new_layout == layout:
            break
        layout = new_layout
    return sum(s == '#' for row in layout for s in row)


def first_seat(i: int, j: int, di: int, dj: int, layout: Layout) -> str:
    while True:
        i, j = i + di, j + dj
        if 0 <= i < len(layout) and 0 <= j < len(layout[0]):
            if layout[i][j] in ['#', 'L']:
                return layout[i][j]
        else:
            return '.'


# Test
IN = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

layout = [list(line) for line in IN.split('\n')]
assert final_taken_seats(layout) == 37
assert final_taken_seats2(layout) == 26

# Result

with open('data/day11.txt') as f:
    layout = [list(line) for line in f.read().split('\n') if len(line) > 0]
    print(final_taken_seats(layout))
    print(final_taken_seats2(layout))
