import re

pair_pattern = r'.*([a-z][a-z]).*\1.*'
pair_re = re.compile(pair_pattern)

split_pattern = r'.*([a-z])[a-z]\1.*'
split_re = re.compile(split_pattern)

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        nice = True
        nice = nice and pair_re.match(line)
        nice = nice and split_re.match(line)
        
        if nice:
            count = count + 1
            
print str(count)