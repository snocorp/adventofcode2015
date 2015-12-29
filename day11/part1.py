input = 'hepxxyzz'

def inc(s):
    i = len(s) - 1
    while True:
        if i < 0:
            break

        if s[i] < 'z':
            s[i] = chr(ord(s[i]) + 1)
            break
            
        s[i] = 'a'
        i -= 1
        
    return s
    
def test(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    
    seq = False
    i = 2
    while i < len(s):
        if ord(s[i-2]) + 1 == ord(s[i-1]) and ord(s[i-1]) + 1 == ord(s[i]):
            seq = True
            break
        
        i += 1
    
    if not seq:
        return False
        
    pairs = False
    pair_char = ''
    i = 2
    while i < len(s):
        if s[i] != pair_char and s[i-1] == s[i]:
            if pair_char == '':
                pair_char = s[i]
                i += 1
            else:
                pairs = True
                break
        
        i += 1
    
    return pairs

passwd = inc(list(input))
iterations = 1
while True:
    # print iterations, passwd
    if passwd == input:
        #looped
        print 'No valid password found'
        break
    if test(passwd):
        break
    passwd = inc(passwd)
    iterations += 1

print ''.join(passwd)