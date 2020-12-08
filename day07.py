"""Day 7 - inspired by Joel Grus' solution"""
from typing import List, NamedTuple, Dict
from collections import defaultdict

IN = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

IN2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]


def parse(raw: str) -> List[Bag]:
    bags = []
    for line in raw.strip().split('\n'):
        bags.append(parse_bag(line.strip()))
    return bags


def parse_bag(raw_line: str) -> Bag:
    first, second = raw_line.split(' contain ')
    color = first[:-5]
    second = second.rstrip('.')
    contains = {}
    if 'no other bags' not in second:
        for constraints in second.split(', '):
            words = constraints.split(' ')
            contains[words[1] + ' ' + words[2]] = int(words[0])
    return Bag(color=color, contains=contains)


def get_containers(bags: List[Bag]) -> Dict[str, List[Bag]]:
    containers_of = defaultdict(list)
    for bag in bags:
        for contained in bag.contains:
            containers_of[contained].append(bag)
    return containers_of


def can_contain_bag(color: str, all_bags: List[Bag]) -> List[str]:
    containers_of = get_containers(all_bags)
    check = [color]
    can_contain = []
    while check:
        check_bag = check.pop()
        for container in containers_of.get(check_bag, []):
            if container not in can_contain:
                can_contain.append(container)
                check.append(container.color)
    return can_contain


with open('data/day07.txt') as f:
    bags = parse(f.read())
    can_cont = can_contain_bag('shiny gold', bags)
    print(len([bag.color for bag in can_cont]))


# Part II
def must_contain_bags(color: str, all_bags: List[Bag]) -> int:
    check = [color]
    bag_count = 0
    while check:
        check_bag = find_bag(check.pop(), all_bags)
        for color, amount in check_bag.contains.items():
            check += [color] * amount
            bag_count += amount
    return bag_count


def find_bag(color: str, all_bags: List[Bag]) -> Bag:
    for bag in all_bags:
        if bag.color == color:
            return bag
    return None


with open('data/day07.txt') as f:
    bags = parse(f.read())
    must_contain = must_contain_bags('shiny gold', bags)
    print(must_contain)
