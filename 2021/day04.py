#!/usr/bin/python
import numpy as np
text = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

data = text.split('\n\n')

data = open('data/4.in').read().split('\n\n')
numbers = list(map(int, data[0].split(',')))

def get_card(chunk):
    return np.array([[int(num) for num in line.split()] for line in chunk.split('\n')[:5]])
    
cards = [get_card(chunk) for chunk in data[1:]]
print(cards)

def calc_score(card, nums):
    isin = np.isin(card, chosen)
    print(card)
    print(isin == False)
    print( sum(card[isin == False]) , nums[-1])
    return sum(card[isin == False]) * nums[-1]


# for i in range(1, len(numbers)):
#     chosen = numbers[:i]
#     for card in cards:
#         isin = np.isin(card, chosen)
#         if np.any([np.all(isin[i, :]) for i in range(len(card))]):
#             print(calc_score(card, chosen))
#             exit()
#         if np.any([np.all(isin[:, i]) for i in range(len(card))]):
#             print(calc_score(card, chosen))
#             exit()

print('\n\n')

## Part 2
for i in range(1, len(numbers)):
    winners = []
    chosen = numbers[:i]
    for i, card in enumerate(cards):
        isin = np.isin(card, chosen)
        if np.any([np.all(isin[i, :]) for i in range(len(card))]):
            winners.append(i)
        if np.any([np.all(isin[:, i]) for i in range(len(card))]):
            winners.append(i)
    print(set(winners))
    for winner in sorted(set(winners), reverse=True):
        del cards[winner]

    if len(cards) == 1:
        print(card)
        for i in range(1, len(numbers)):
            chosen = numbers[:i]
            print(chosen)
            card = cards[0]
            isin = np.isin(card, chosen)
            if np.any([np.all(isin[i, :]) for i in range(len(card))]):
                print(calc_score(card, chosen))
                exit()
            if np.any([np.all(isin[:, i]) for i in range(len(card))]):
                print(calc_score(card, chosen))
                exit()
