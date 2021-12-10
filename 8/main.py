f = open("input.txt")
dat = [i.split() for i in f.readlines()]

regs = dict()
operand = [">","<",">=","<=",'==','!=']
highest = dict()

for i in dat:
    factor = 1
    if i[1] == 'dec':
        factor *= -1

    if i[0] not in regs:
        regs[i[0]] = 0
        highest[i[0]] = 0

    if i[-3] not in regs:
        regs[i[-3]] = 0
        highest[i[-3]] = 0

    op = operand.index(i[-2])
    if op == 0:
        val = int(i[2]) if regs[i[-3]] > int(i[-1]) else 0
    elif op == 1:
        val = int(i[2]) if regs[i[-3]] < int(i[-1]) else 0
    elif op == 2:
        val = int(i[2]) if regs[i[-3]] >= int(i[-1]) else 0
    elif op == 3:
        val = int(i[2]) if regs[i[-3]] <= int(i[-1]) else 0
    elif op == 4:
        val = int(i[2]) if regs[i[-3]] == int(i[-1]) else 0
    elif op == 5:
        val = int(i[2]) if regs[i[-3]] != int(i[-1]) else 0

    regs[i[0]] += val*factor
    if regs[i[0]] > highest[i[0]]:
        highest[i[0]] = regs[i[0]]

print(max(list(regs.values())))
print(max(list(highest.values())))

