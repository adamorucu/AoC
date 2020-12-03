"""Day 03"""
INPUTS = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


class Field:
    def __init__(self, field):
        self.field = field.split('\n')
        self.height = len(self.field)
        self.width = len(self.field[0])
        self.trees = []
        for i, row in enumerate(self.field):
            for j, point in enumerate(row.strip()):
                if point == '#':
                    self.trees.append((i, j))

    def trees_on_slope(self, r, d):
        j = 0
        trees = 0
        for i in range(0, self.height, d):
            if (i, j) in self.trees:
                trees += 1
            j = (j + r) % self.width
        return trees


field = Field(INPUTS)
assert field.trees_on_slope(3, 1) == 7

with open('data/day03.txt') as f:
    field = Field(f.read())
    print(field.trees_on_slope(3, 1))

# -- Part II
field = Field(INPUTS)
r = [1, 3, 5, 7, 1]
d = [1, 1, 1, 1, 2]

product = 1
for i in range(len(r)):
    product *= field.trees_on_slope(r[i], d[i])
assert product == 336

with open('data/day03.txt') as f:
    field = Field(f.read())
    product = 1
    for i in range(len(r)):
        product *= field.trees_on_slope(r[i], d[i])
    print(product)
