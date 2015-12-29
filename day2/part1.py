L = 0
W = 1
H = 2

total_area = 0
with open('input.txt', 'r') as f:
    for line in f:
        dim = line.split('x')
        dim[L] = int(dim[L])
        dim[W] = int(dim[W])
        dim[H] = int(dim[H])
        
        area = (dim[L]*dim[W] + dim[W]*dim[H] + dim[H]*dim[L]) * 2
        smallest = dim[L]*dim[W]*dim[H] / max(dim)
        total_area += area + smallest
        
print total_area