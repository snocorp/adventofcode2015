

with open('input.txt', 'r') as f:
    input = f.read()
    
level = 0
position = 1
for c in input:
    if c == '(':
        level += 1
    elif c == ')':
        level -= 1
    if level < 0:
        break
    position += 1

print position
        