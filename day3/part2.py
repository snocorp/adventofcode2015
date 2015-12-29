
with open('input.txt', 'r') as f:
    input = f.read()

grid = {'0,0': 1}
s = [
    {'x': 0, 'y': 0},
    {'x': 0, 'y': 0}
]
santa = 0
count = 0
for c in input:
    sled = s[santa]
    
    if c == '^':
        sled['y'] = sled['y'] - 1
    elif c == 'v':
        sled['y'] = sled['y'] + 1
    elif c == '<':
        sled['x'] = sled['x'] - 1
    elif c == '>':
        sled['x'] = sled['x'] + 1
    pos = str(sled['x'])+','+str(sled['y'])
    count += 1
    santa = 1 - santa
    
    grid[pos] = grid.get(pos, 0) + 1
    
    # print str(count)+': '+pos+'='+str(grid[pos])
    
print len(grid)