# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    #low_pt = [s.start for s in segments]
    high_pt = [s.end for s in segments]
    index = high_pt.index(min(high_pt))
    p = high_pt[index]
    points.append(p)
    del segments[index]
    seg = segments[:]

    for s in seg:
        if p >= s.start and p<= s.end:
            #print(s)
            segments.remove(s)

    if segments!=[]:
        extra = optimal_points(segments)
        set1 = set(extra)
        set2 = set(points)
        if set1 - set2 == []:
            points += extra
        else:
            points = points + list(set1 - set2)

    return points




    #for s in segments:
        #points.append(s.start)
        #points.append(s.end)
    #return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
