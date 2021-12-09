regs = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
# regs = [0,2,7,0]

s = set()
a = []
while tuple(regs) not in s:
    s.add(tuple(regs))
    a.append(tuple(regs))
    m = max(regs)
    m_index = regs.index(m)
    regs[m_index] = 0
    m_index += 1
    for i in range(m):
        regs[(m_index + i)%len(regs)] += 1

print("1:",len(s))
print("2:",len(s) - a.index(tuple(regs)))


