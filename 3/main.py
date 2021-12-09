inp = 325489

x = y = 0

i = int(inp ** .5)

field = dict()
field[1] = (x,y)
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
cur_dir = 0

count = 0
x = y = nx = 0
ny = -1

while True:
    count += 1
    if count == inp:
        print("1:",abs(x) + abs(y))
        break
    if x == y or (x<0 and x == -y) or (x>0 and x == 1-y):
        nx,ny = -ny,nx
    x,y = x+nx,y+ny
# 1,0 -> 0,-1 -> ny,-nx
# 0,-1 -> -1,0 -> ny,nx
# -1,0 -> 0,1 -> ny,-nx
# 0,1-> 1,0 -> ny,nx

field = dict()
surrounds = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]
y = ny = 0
x = nx = 1
field[(0,0)] = 1

while field[(x-nx,y-ny)] < inp:
    count = 0
    for dx,dy in surrounds:
        if (x+dx,y+dy) in field:
            count += field[(x+dx,y+dy)]
    field[(x,y)] = count
    if x == y or (x<0 and x == -y) or (x>0 and x == 1-y):
        nx,ny = -ny,nx
    x,y = x+nx,y+ny

print("2:",field[(x-nx,y-ny)])