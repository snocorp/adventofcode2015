

out = open('output2.py', 'w')

out.write("""
total = 0
"""
)

def encode(s):
    return s.replace("\\", "\\\\").replace("\"", "\\\"")

try:
    with open('input.txt', 'r') as f:
        for line in f:
            s = line.strip()
            out.write('total = total + len("\\"%s\\"") - %d\n' % (encode(encode(s)), len(s)))
            
    out.write("""
print total
"""
)
finally:
    out.close()