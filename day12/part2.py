import json

def sum_dict(d):
    if 'red' in d.values():
        return 0
    sum = 0
    for i in d:
        if type(d[i]) is dict:
            sum += sum_dict(d[i])
        elif type(d[i]) is list:
            sum += sum_list(d[i])
        elif type(d[i]) is int:
            sum += d[i]
    return sum
    
def sum_list(a):
    sum = 0
    for i in a:
        if type(i) is dict:
            sum += sum_dict(i)
        elif type(i) is list:
            sum += sum_list(i)
        elif type(i) is int:
            sum += i
    return sum

with open('input.txt', 'r') as f:
    input = f.read()
    
j = json.loads(input)
sum = 0
if type(j) is dict:
    sum += sum_dict(j)
elif type(j) is list:
    sum += sum_list(j)
elif type(j) is int:
    sum += i
print sum