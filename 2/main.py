dat = []
with open("input.txt") as f:
    for i in f.readlines():
        temp = []
        for j in i.split():
            temp.append(int(j))
        dat.append(temp)

count = 0
for i in dat:
    count += max(i) - min(i)
print("1:", count)

count = 0
for lst in dat:
    for i, val in enumerate(lst):
        for j in lst[i+1:]:
            if val/j == val//j:
                count += val // j
            elif j/val == j // val:
                count += j // val
print("2:", count)