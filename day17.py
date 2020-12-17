""" Day 17 """
import numpy as np
from typing import List
from itertools import product
from collections import Counter


# Solution
class Pocket:
    neighbors = list(product(range(-1, 2), repeat=3))

    def __init__(self, layers: List[str]):
        self.layers = layers

    def run_cycles(self, nb_cycles: int):
        for _ in range(nb_cycles):
            self.cycle()
        return np.count_nonzero(self.layers == 1)

    def cycle(self):
        new = np.zeros((self.layers.shape[0] + 2, self.layers.shape[1] + 2,
                        self.layers.shape[2] + 2))
        new[1:-1, 1:-1, 1:-1] = self.layers
        self.layers = new
        lshape = self.layers.shape
        # print(self.layers)

        to_change = []
        for k in range(0, lshape[0]):
            for j in range(0, lshape[1]):
                for i in range(0, lshape[2]):
                    # count = Counter([
                    #     self.layers[k + dk, j + dj, i + di]
                    #     for (di, dj, dk) in self.neighbors
                    #     if 0 <= k + dk < lshape[0] - 1 and 0 <= j +
                    #     dj < lshape[1] - 1 and 0 <= i + di < lshape[2] -
                    #     1  #and (i, j, k) != (0, 0, 0)
                    # ])
                    neighs = []
                    for (di, dj, dk) in self.neighbors:
                        try:
                            if (di, dj, dk) != (0, 0, 0):
                                neighs.append(self.layers[k + dk, j + dj,
                                                          i + di])
                        except:
                            pass
                    count = Counter(neighs)

                    # print(k, j, i)
                    # if k == 1:
                    #     print(j, i, self.layers[k, j, i], count)
                    if self.change_state(self.layers[k, j, i], count):
                        to_change.append((k, j, i))
        for k, j, i in to_change:
            self.layers[k, j, i] = 1 if self.layers[k, j, i] == 0 else 0

    def change_state(self, state: str, count: Counter) -> bool:
        # print(state, count[1])
        if state == 1 and count[1] not in {2, 3}:
            return True
        elif state == 0 and count[1] == 3:
            return True
        return False


def parse(raw: str) -> Pocket:
    return Pocket(
        np.array([[[0 if p == '.' else 1 for p in row]
                   for row in raw.split('\n')]]))


# Part 2
def parse2(raw: str) -> Pocket:
    return Pocket2(
        np.array([[[[0 if p == '.' else 1 for p in row]
                    for row in raw.split('\n')]]]))


class Pocket2:
    neighbors = list(product(range(-1, 2), repeat=4))

    def __init__(self, layers: List[str]):
        self.layers = layers

    def run_cycles(self, nb_cycles: int):
        for _ in range(nb_cycles):
            self.cycle()
        return np.count_nonzero(self.layers == 1)

    def cycle(self):
        new = np.zeros((self.layers.shape[0] + 2, self.layers.shape[1] + 2,
                        self.layers.shape[2] + 2, self.layers.shape[3] + 2))
        new[1:-1, 1:-1, 1:-1, 1:-1] = self.layers
        self.layers = new
        lshape = self.layers.shape
        # print(self.layers)

        to_change = []
        for k in range(0, lshape[0]):
            for j in range(0, lshape[1]):
                for i in range(0, lshape[2]):
                    for w in range(0, lshape[3]):
                        neighs = []
                        for (dw, di, dj, dk) in self.neighbors:
                            try:
                                if (dw, di, dj, dk) != (0, 0, 0, 0):
                                    neighs.append(self.layers[k + dk, j + dj,
                                                              i + di, w + dw])
                            except:
                                pass
                        count = Counter(neighs)
                        if self.change_state(self.layers[k, j, i, w], count):
                            to_change.append((k, j, i, w))
        for k, j, i, w in to_change:
            self.layers[k, j, i, w] = 1 if self.layers[k, j, i, w] == 0 else 0

    def change_state(self, state: str, count: Counter) -> bool:
        # print(state, count[1])
        if state == 1 and count[1] not in {2, 3}:
            return True
        elif state == 0 and count[1] == 3:
            return True
        return False


# Tests
IN = """.#.
..#
###"""
# p = parse(IN)
# print(p.layers)
# p.run_cycles(1)
# print(p.layers)

assert parse(IN).run_cycles(6) == 112
assert parse2(IN).run_cycles(6) == 848

# Results
DATA = """######.#
##.###.#
#.###.##
..#..###
##.#.#.#
##...##.
#.#.##.#
.###.###"""

print(parse(DATA).run_cycles(6))
print(parse2(DATA).run_cycles(6))
