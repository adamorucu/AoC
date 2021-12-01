"""My solutions to problem on day02"""
INPUTS = ['1-3 a: abcd', '1-3 b: cdef', '2-9 c: ccccccccc']


def checkvalidity(inputs):
    """Checks password is valid according to the policy"""
    occ, letter, password = inputs.split(' ')
    letter = letter[0]
    least, most = occ.split('-')
    occurance = password.count(letter)
    return int(least) <= occurance and int(most) >= occurance


assert sum([checkvalidity(i) for i in INPUTS]) == 2

with open('data/day02.txt') as f:
    lines = f.readlines()
    res = sum([checkvalidity(line) for line in lines])
    print(res)


def check_pos_validity(line):
    """Checks validity of password occording to a characters position in it"""
    posi, letter, password = line.split(' ')
    letter = letter[0]
    pos1, pos2 = posi.split('-')
    one = (password[int(pos1) - 1] == letter)
    two = (password[int(pos2) - 1] == letter)
    return one ^ two


assert sum([check_pos_validity(i) for i in INPUTS]) == 1

with open('data/day02.txt') as f:
    lines = f.readlines()
    res = sum([check_pos_validity(line) for line in lines])
    print(res)
