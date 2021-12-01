""" Day 9 """
from typing import NamedTuple, List, Set

IN = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


class XMAS(NamedTuple):
    preamble_size: int
    preamble: List[int]

    def transmit(self, num: int) -> bool:
        if self.check_rule(self.preamble, num):
            self.preamble.append(num)
            self.preamble.pop(0)
            return True
        return False

    def check_rule(self, preamble: List[int], new: int) -> bool:
        mem = set(preamble)
        for num in mem:
            if new - num in mem - {num}:
                return True
        return False


def parse(raw: str, preamble_size: int) -> (XMAS, List[int]):
    nums = [int(line.strip()) for line in raw.split('\n') if len(line) >= 1]
    preamble = nums[:preamble_size]
    stream = nums[preamble_size:]
    return XMAS(preamble_size, preamble), stream


def start_transmission(port: XMAS, stream: List[int]) -> int:
    for num in stream:
        if not port.transmit(num):
            return num
    return None


def find_contiguous_set(total: int, stream: List[int]) -> Set[int]:
    for ind, num in enumerate(stream):
        contigs = [num]
        loc = ind
        while sum(contigs) < total:
            loc += 1
            contigs.append(stream[loc])
        if sum(contigs) == total:
            return set(contigs)
    return None


with open('data/day09.txt') as f:
    port, stream = parse(f.read(), 25)
    first_preamble = port.preamble
    invalid_num = start_transmission(port, stream)
    print(invalid_num)
    cont_set = find_contiguous_set(invalid_num, first_preamble + stream)
    print(max(cont_set) + min(cont_set))
