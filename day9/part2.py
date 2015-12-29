import re

def routes(graph, chain, dist):
    if len(chain) == len(graph):
        return dist
        
    # print chain

    options = graph[chain[len(chain)-1]]
    
    # print options
    
    max_dist = -1
    for o in options:
        if o not in chain:
            d = routes(graph, chain + [o], dist + options[o])
            if d > max_dist:
                max_dist = d
    return max_dist


dist_pattern = r'(.*?) to (.*?) = (\d+)'
dist_re = re.compile(dist_pattern)

G = {}
with open('input.txt', 'r') as f:
    for line in f:
        m = dist_re.match(line)
        
        if m:
            from_place = m.group(1)
            to_place = m.group(2)
            dist = int(m.group(3))
            
            if from_place not in G:
                G[from_place] = {}
            if to_place not in G:
                G[to_place] = {}
            
            G[from_place][to_place] = dist
            G[to_place][from_place] = dist
        else:
            print 'No match for line: %s' % line

print len(G)
max_dist = -1
for start in G:
    dist = routes(G, [start], 0)
    if dist > max_dist:
        max_dist = dist
print max_dist