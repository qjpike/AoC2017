
f = open("input.txt")
dat = [i.strip().split() for i in f.readlines()]

import collections

count = len(dat)
for i in dat:
    deck = collections.deque(i)
    while len(deck) > 1:
        cur = deck.popleft()
        if cur in deck:
            count -= 1
            break
print(count)

count = 0
for i in dat:
    s = set()
    for j in i:
        s.add(frozenset(j))
    if len(s) == len(i):
        count += 1

print(count)