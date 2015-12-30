import re

race_time = 2503

dist_pattern = r'(.*?) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.'
dist_re = re.compile(dist_pattern)

G = {}
with open('input.txt', 'r') as f:
    for line in f:
        m = dist_re.match(line)
        
        if m:
            reindeer = m.group(1)
            
            G[reindeer] = {
                'flight_speed': int(m.group(2)),
                'flight_time': int(m.group(3)),
                'rest_time': int(m.group(4)),
                'state': 'start',
                'since': 0,
                'distance': 0,
                'points': 0
            }
        else:
            print 'No match for line: %s' % line

t = 1
while t <= race_time + 1:
    max_r = None
    for r in G:
        if G[r]['state'] == 'start':
            G[r]['state'] = 'flight'
            G[r]['since'] = t
            G[r]['distance'] += G[r]['flight_speed']
        elif G[r]['state'] == 'flight':
            if t - G[r]['flight_time'] == G[r]['since']:
                G[r]['state'] = 'rest'
                G[r]['since'] = t
            else:
                G[r]['distance'] += G[r]['flight_speed']
        elif G[r]['state'] == 'rest':
            if t - G[r]['rest_time'] == G[r]['since']:
                G[r]['state'] = 'flight'
                G[r]['since'] = t
                G[r]['distance'] += G[r]['flight_speed']
    
        print t, r, G[r]['state'], G[r]['points']
        
        if max_r is None or G[r]['distance'] > G[max_r]['distance']:
            max_r = r

    for r in G:
        if G[r]['distance'] == G[max_r]['distance']:
            G[r]['points'] += 1
    
    t += 1

max_r = None
for r in G:
    if max_r is None or G[r]['points'] > G[max_r]['points']:
        max_r = r
        
print 'Winner:'
print t, max_r, G[max_r]['points']