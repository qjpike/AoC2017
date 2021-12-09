import copy

f = open("input.txt")
dat = [int(i) for i in f.readlines()]
dat2 = copy.deepcopy(dat)
ptr = 0
max_ptr = len(dat)

count = 0
while -1 < ptr < max_ptr:
    n = dat[ptr]
    dat[ptr] += 1
    ptr += n
    count += 1

print(count)

# part 2 takes a bit to execute.
ptr = 0
count = 0
while -1 < ptr < max_ptr:
    n = dat2[ptr]
    if n >= 3:
        dat2[ptr] -= 1
    else:
        dat2[ptr] += 1
    ptr += n
    count += 1

print(count)