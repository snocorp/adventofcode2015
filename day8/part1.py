

out = open('output1.py', 'w')

out.write("""
total = 0
"""
)

try:
    with open('input.txt', 'r') as f:
        for line in f:
            s = line.strip()
            out.write('total = total + %d - len(%s)\n' % (len(s), s))
            
    out.write("""
print total
"""
)
finally:
    out.close()