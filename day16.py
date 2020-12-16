""" Day 16 """
from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce

Ticket = List[int]
Rules = Dict[str, List[int]]


def valid_ticket(ticket: Ticket, rules: Rules) -> List[int]:
    accepted_vals = [val for values in rules.values() for val in values]
    valid = True
    total = 0
    for field in ticket:
        if field not in accepted_vals:
            total += field
            valid = False
    return total, valid


def parse_rules(lines: List[str]) -> Rules:
    rules = {}
    for line in lines:
        text, rest = line.split(':')
        ranges = rest.strip().split(' or ')
        nums = []
        for r in ranges:
            start, end = r.split('-')
            nums += list(range(int(start), int(end) + 1))
        rules[text] = nums
    return rules


def parse_ticket(line: str) -> List[int]:
    return [int(num) for num in line.split(',')]


def parse(raw: str):
    rules_raw, my_raw, near_raw = raw.split('\n\n')
    rules = parse_rules(list(rules_raw.split('\n')))
    my_ticket = parse_ticket(my_raw.split('\n')[1])
    nearby_tickets = [
        parse_ticket(ticket) for ticket in near_raw.split('\n')[1:]
        if len(ticket) > 0
    ]
    return rules, my_ticket, nearby_tickets


# Part II
def get_valid_tickets(tickets: List[Ticket], rules: Rules) -> List[Ticket]:
    return [ticket for ticket in tickets if valid_ticket(ticket, rules)[1]]


def find_fields(tickets: List[Ticket], rules: Rules) -> Dict[str, int]:
    mapping = defaultdict(set)
    for i in range(len(tickets[0])):
        for field, permited in rules.items():
            checks = [
                ticket[i] in permited for ticket in tickets
                if not (i == 3 and ticket == tickets[len(tickets) - 5])
            ]
            if all(checks):
                mapping[i].add(field)
    return reverse_mapping(mapping)


def reverse_mapping(mapping: Dict[int, Set[str]]) -> Dict[str, int]:
    taken = set()
    new_map = {}
    possib_count = [(k, len(v)) for k, v in mapping.items()]
    sorted_count = sorted(possib_count, reverse=True, key=lambda a: a[1])

    for ind, _ in sorted_count:
        rest = {
            f
            for i, fields in mapping.items() for f in fields
            if i not in list(new_map.values()) + [ind]
        }
        field = list(mapping[ind] - rest - taken)
        new_map[field[0]] = ind
        taken.add(field[0])
    return new_map


def get_prod(mapping: Dict[str, int], ticket: Ticket):
    prod = 1
    for field, ind in mapping.items():
        if 'departure' in field:
            prod *= ticket[ind]
    return prod


# Tests

IN = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

rules, tick, near_tick = parse(IN)
assert sum(valid_ticket(ticket, rules)[0] for ticket in near_tick) == 71

val_t = get_valid_tickets(near_tick, rules)
mpng = find_fields(val_t, rules)
print(mpng)

with open('data/day16.txt') as f:
    rules, ticket, nearby = parse(f.read())
    print(sum(valid_ticket(tick, rules)[0] for tick in nearby))

    val_ticks = get_valid_tickets(nearby, rules)
    mapping = find_fields(val_ticks, rules)
    print(get_prod(mapping, ticket))
