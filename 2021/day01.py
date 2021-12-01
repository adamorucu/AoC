#!/usr/bin/python
data = [int(line.strip()) for line in open('data/01.txt').readlines()]

## Part 1
count = 0
for i in range(len(data) - 1):
    if data[i] < data[i+1]:
        count += 1

print(count)


## Part 2
sums = []
for i in range(len(data) - 2):
    sums.append(sum(data[i:i+3]))

count = 0
for i in range(len(sums) - 1):
    if sums[i] < sums[i+1]:
        count += 1

print(count)
