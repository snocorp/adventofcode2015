import re

vowel_pattern = r'.*[aeiou].*[aeiou].*[aeiou].*'
vowel_re = re.compile(vowel_pattern)

pair_pattern = r'.*([a-z])\1.*'
pair_re = re.compile(pair_pattern)

excl = ['ab', 'cd', 'pq', 'xy']

count = 0
with open('input.txt', 'r') as f:
    for line in f:
        nice = True
        nice = nice and vowel_re.match(line)
        nice = nice and pair_re.match(line)
        if nice:
            for e in excl:
                if line.find(e) > -1:
                    nice = False
                    break
        
        if nice:
            count = count + 1
            
print str(count)