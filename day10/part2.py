input = '1113122113'

def lookandsay(s):
    output = ''
    count = 0
    prev = ''
    for c in s:
        if prev == '' or c == prev:
            count += 1
        else:
            output += str(count) + prev
            count = 1
        prev = c
    return output + str(count) + prev

for i in range(50):
    input = lookandsay(input)

print len(input)