lens = [129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108]
# lens = [3,4,1,5]

rope_len = 256
rope = list(range(rope_len))

pos = 0
skipsize = 0

def hash(rope,lens,pos,skipsize):
    for i in lens:
        if pos + i > len(rope):
            rope *= 2
        flip = list(reversed(rope[pos:pos+i]))
        rope = rope[:pos] + flip + rope[pos+i:]
        if len(rope) > rope_len:
            rope = rope[rope_len:pos+i] + rope[pos+i-rope_len:rope_len]
        pos = (pos + i + skipsize)%rope_len
        skipsize += 1
    return (rope,lens,pos,skipsize)

rope,lens,pos,skipsize = hash(rope,lens,pos,skipsize)

print("1:", rope[0]*rope[1]) # 20592 too high

inp = '129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108'
lens = [ord(i) for i in inp]
lens += [17,31,73,47,23]
rope = rope = list(range(rope_len))
pos = 0
skipsize = 0

for i in range(64):
    rope,lens,pos,skipsize = hash(rope,lens,pos,skipsize)

pos = 0
res = []
for i in range(0,rope_len,16):
    r = 0
    for j in range(i,i+16):
        r ^= rope[j]
    if len(hex(r)) == 4:
        res.append(hex(r)[2:])
    else:
        res.append(0 + hex(r)[3])

print("2:",''.join(res))
