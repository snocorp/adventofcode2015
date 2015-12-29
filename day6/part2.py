import numpy
import re

width = 1000
height = 1000

grid = numpy.zeros((width, height))

command_pattern = r'.*?(\d+),(\d+) through (\d+),(\d+)'
command_re = re.compile(command_pattern)

def turn_on(x):
    return x + 1
    
def turn_off(x):
    return max(x - 1, 0)
    
def toggle(x):
    return x + 2

def handle_command(cmd):
    m = command_re.match(line)
    if m:
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))
        
        x = x1
        while x <= x2:
            y = y1
            while y <= y2:
                grid[x,y] = cmd(grid[x,y])
                y = y + 1
            x = x + 1
    else:
        print 'No match for line: ' + line

with open('input.txt', 'r') as f:
    for line in f:
        if line.find('turn on') == 0:
            handle_command(turn_on)
        elif line.find('turn off') == 0:
            handle_command(turn_off)
        elif line.find('toggle') == 0:
            handle_command(toggle)
        # print int(grid.sum())
            
print grid.sum()