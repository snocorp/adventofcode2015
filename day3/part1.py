
with open('input.txt', 'r') as f:
    input = f.read()

grid = {'0,0': 1}
x = 0
y = 0
count = 0
for c in input:
    if c == '^':
        y = y - 1
    elif c == 'v':
        y = y + 1
    elif c == '<':
        x = x - 1
    elif c == '>':
        x = x + 1
    pos = str(x)+','+str(y)
    count += 1
    
    grid[pos] = grid.get(pos, 0) + 1
    
    # print str(count)+': '+pos+'='+str(grid[pos])
    
print len(grid)