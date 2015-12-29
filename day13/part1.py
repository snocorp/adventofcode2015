import re

h_pattern = r'(.*?) would (.*?) (\d+) happiness units by sitting next to (.*?)\.'
h_re = re.compile(h_pattern)

def find_happiness(h_map, table=[], delta=0):
    max_delta = None
    if len(table) == 0:
        for s in h_map:
            h = find_happiness(h_map, [s], 0)
            if max_delta is None or h > max_delta:
                max_delta = h
    elif len(table) == len(h_map):
        last = table[-1]
        first = table[0]
        max_delta = delta + h_map[last][first] + h_map[first][last]
    else:
        last = table[-1]
        for s in h_map:
            if s not in table:
                h = find_happiness(h_map, table + [s], delta + h_map[last][s] + h_map[s][last])
                if max_delta is None or h > max_delta:
                    max_delta = h
    return max_delta
        
def add_me(h_map):
    h_map['me'] = {}
    for s in h_map:
        h_map[s]['me'] = 0
        h_map['me'][s] = 0

happy_map = {}

with open('input.txt', 'r') as f:
    for line in f:
        m = h_re.match(line)
        if m:
            subject = m.group(1)
            action = m.group(2)
            amount = int(m.group(3))
            other = m.group(4)
            if subject not in happy_map:
                happy_map[subject] = {}
            if action == 'lose':
                amount *= -1
            happy_map[subject][other] = amount
        else:
            print 'No match for line: %s' % line
            


print happy_map
print find_happiness(happy_map)

add_me(happy_map)

print happy_map
print find_happiness(happy_map)