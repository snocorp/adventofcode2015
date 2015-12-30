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
                'rest_time': int(m.group(4))
            }
        else:
            print 'No match for line: %s' % line

max_distance = 0
max_reindeer = '?'
for r in G:
    t = 0
    d = 0
    while t < race_time:
        # flight phase
        t_flight = min(race_time - t, G[r]['flight_time'])
        d += t_flight * G[r]['flight_speed']
        
        t += t_flight + G[r]['rest_time']
        
    if d > max_distance:
        max_distance = d
        max_reindeer = r
        
print max_reindeer, max_distance