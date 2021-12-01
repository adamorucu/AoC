"""Day 4"""
import re
from typing import List, Dict

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

passport = Dict[str, str]


def parse_passport(raw: str) -> passport:
    pas = {}
    for line in raw.split('\n'):
        for field in line.split(' '):
            if field == '':
                continue
            k, v = field.split(':')
            pas[k] = v
    return pas


def parse_all(raw: str) -> List[passport]:
    pass_list = []
    for pass_raw in raw.split('\n\n'):
        pass_list.append(parse_passport(pass_raw))
    return pass_list


pl = parse_all(INPUT)

needed = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def validate(pas: passport) -> bool:
    keys = [k for k in pas.keys()]
    for field in needed:
        if field not in keys:
            return False
    return True


s = sum(validate(p) for p in pl)
assert s == 2

with open('data/day04.txt') as f:
    data = f.read()
    pl = parse_all(data)
    print(sum(validate(p) for p in pl))


def validate2(pas: passport) -> bool:
    if not validate(pas):
        return False
    valid = [
        1920 <= int(pas.get('byr', -1)) <= 2002,
        2010 <= int(pas.get('iyr', -1)) <= 2020,
        2020 <= int(pas.get('eyr', -1)) <= 2030,
        check_height(pas.get('hgt', '')),
        re.match(r'^#[0-9a-f]{6}$', pas.get('hcl', '')),
        pas.get('ecl') in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        re.match(r'^[0-9]{9}$', pas.get('pid', ''))
    ]
    return all(valid)


def check_height(hgt: str) -> bool:
    if hgt.endswith('cm'):
        hgt = hgt.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif hgt.endswith("in"):
        hgt = hgt.replace("in", "")
        try:
            return 59 <= int(hgt) <= 76
        except:
            return False

    return False


with open('data/day04.txt') as f:
    data = f.read()
    pl = parse_all(data)
    print(sum(validate2(p) for p in pl))
