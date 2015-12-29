L = 0
W = 1
H = 2

total_length = 0
with open('input.txt', 'r') as f:
    for line in f:
        dim = line.split('x')
        dim[L] = int(dim[L])
        dim[W] = int(dim[W])
        dim[H] = int(dim[H])
        
        smallest_perimeter = (dim[L]+dim[W]+dim[H] - max(dim)) * 2
        volume = dim[L]*dim[W]*dim[H]
        total_length += smallest_perimeter + volume
        
        #print (smallest_perimeter + volume)
        
print total_length