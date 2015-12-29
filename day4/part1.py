import md5
import string
import sys

input = 'ckczppom'
found = False

prefix = '00000'
max = sys.maxint

n = 0
while n <= max:
    hash = md5.new(input + str(n))

    hex = hash.hexdigest()
    if string.find(hex, prefix) == 0:
        found = True
        break
    
    n = n + 1

if found:
    print "%d: %s" % (n, hex)
else:
    print 'no result'