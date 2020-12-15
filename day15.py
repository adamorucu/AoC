""" Day 15 """


class Game:
    def __init__(self, initials):
        self.spoken_nums = initials

    def next_turn(self):
        last = self.spoken_nums[-1]
        if self.spoken_nums.count(last) == 1:
            self.spoken_nums.append(0)
        else:
            newest = list(reversed(self.spoken_nums)).index(last)
            prev = list(reversed(self.spoken_nums)).index(last, newest + 1)
            self.spoken_nums.append(prev - newest)

    def play(self, turns):
        for i in range(turns - len(self.spoken_nums)):
            self.next_turn()
        return self.spoken_nums[-1]


assert Game([0, 3, 6]).play(2020) == 436
assert Game([2, 1, 3]).play(2020) == 10
assert Game([3, 1, 2]).play(2020) == 1836

print(Game([20, 0, 1, 11, 6, 3]).play(2020))

# Part II


def play(initials, rounds):
    history = {}
    last_spoken = None

    for i, init in enumerate(initials):
        history[init] = i + 1
        # print(f'Round: {i + 1}, speak {init}')

    for r in range(len(initials), rounds):
        if last_spoken not in history:
            speak = 0
        else:
            speak = r - history[last_spoken]
        # print(f'Round: {r + 1}, speak {speak}, last: {last_spoken}')
        history[last_spoken] = r
        last_spoken = speak
    return speak


assert play([0, 3, 6], 30000000) == 175594

print(play([20, 0, 1, 11, 6, 3], 30000000))
