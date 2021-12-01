""" Day 12 """
from typing import List, Tuple, NamedTuple
import numpy as np

direct = {
    'N': [1, 0],
    'S': [-1, 0],
    'E': [0, 1],
    'W': [0, -1],
    '0': [1, 0],
    '180': [-1, 0],
    '270': [0, -1],
    '90': [0, 1]
}


class Ship:
    def __init__(self):
        self.pos: np.ndarray = np.array([0, 0])
        self.ang: int = 90

    @property
    def manhattan_distance(self):
        return np.abs(self.pos[0]) + np.abs(self.pos[1])

    def move(self, act: str, val: int) -> None:
        if act == 'L' or act == 'R':
            self.ang += val if act == 'R' else -val
            self.ang = np.mod(self.ang, 360)
        elif act == 'F':
            self.pos = self.pos + np.array(direct[str(self.ang)]) * val
        else:
            self.pos += np.array(direct[act]) * val


class Ship2:
    def __init__(self):
        self.pos: np.ndarray = np.array([0, 0])
        self.waypoint: np.ndarray = np.array([1, 10])

    @property
    def manhattan_distance(self):
        return np.abs(self.pos[0]) + np.abs(self.pos[1])

    def apply_instruction(self, act: str, val: int) -> None:
        if act == 'F':
            self.move_ship(val)
        else:
            self.move_waypoint(act, val)

    def move_waypoint(self, act: str, val: int) -> None:
        if act == 'L' or act == 'R':
            if val == 180:
                self.waypoint *= [-1, -1]
                return None
            elif val == 270:
                val = 90
                act = 'R' if act == 'L' else 'L'
            if act == 'R':
                temp = self.waypoint[0]
                self.waypoint[0] = -self.waypoint[1]
                self.waypoint[1] = temp
            elif act == 'L':
                temp = self.waypoint[0]
                self.waypoint[0] = self.waypoint[1]
                self.waypoint[1] = -temp
            else:
                raise ValueError
        else:
            self.waypoint += np.array(direct[act]) * val

    def move_ship(self, val: int) -> None:
        self.pos += self.waypoint * val


def parse(raw: str) -> List[Tuple[str, int]]:
    instrucs = []
    for line in raw.split('\n'):
        if len(line) > 0:
            act = line[0]
            val = int(line[1:])
            instrucs.append((act, val))
    return instrucs


# Tests

IN = """F10
N3
F7
R90
F11"""

s1 = Ship()
cmds = parse(IN)
for act, val in cmds:
    s1.move(act, val)
assert s1.manhattan_distance == 25

s2 = Ship2()
for act, val in cmds:
    s2.apply_instruction(act, val)
assert s2.manhattan_distance == 286

# Results
with open('data/day12.txt') as f:
    ship = Ship()
    ship2 = Ship2()
    actions = parse(f.read())
    for act, val in actions:
        ship.move(act, val)
        ship2.apply_instruction(act, val)
    print(ship.manhattan_distance)
    print(ship2.manhattan_distance)
