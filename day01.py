"""Solution for day01"""
INPUTS = [1721, 979, 366, 299, 675, 1456]


def product(expenses):
    """Find two expenses that add up to 2020 and multiply them"""
    missing = {2020 - ex for ex in expenses}

    for ex in expenses:
        if ex in missing:
            return ex * (2020 - ex)
    return None


assert product(INPUTS) == 514579

with open('data/day01.txt') as f:
    lns = f.readlines()
    ins = [int(ln.strip()) for ln in lns]
    res1 = product(ins)


def product3(expenses):
    """Finds three expenses that sum up to 2020 and returns their produt"""
    missing = {
        2020 - ex1 - ex2: [ex1, ex2]
        for ex1 in expenses for ex2 in expenses
    }

    for ex in expenses:
        if ex in missing:
            ex1, ex2 = missing[ex]
            return ex * ex1 * ex2
    return None


assert product3(INPUTS) == 241861950

with open('data/day01.txt') as f:
    lns = f.readlines()
    ins = [int(ln.strip()) for ln in lns]
    res2 = product3(ins)
    print(res2)
