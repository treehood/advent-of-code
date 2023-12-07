import math

def p1(f):
    times, distances = list(map(str.split, [l.split(":")[1] for l in f.readlines()]))
    res = 1
    for i, time in enumerate(times):
        time = int(time)
        dist = int(distances[i])
        # Since values form a parabola, we can use quadratic formula to compute ranges.
        x1 = (-time + math.sqrt((time**2) - (4*-1*-dist )))/-2
        x2 = (-time - math.sqrt((time**2) - (4*-1*-dist )))/-2
        res *= (math.ceil(x2) - math.floor(x1+1))
    return res
def p2(f):
    time, dist = [int(l.split(":")[1].replace(" ", "")) for l in f.readlines()]
    x1 = (-time + math.sqrt((time**2) - (4*-1*-dist )))/-2
    x2 = (-time - math.sqrt((time**2) - (4*-1*-dist )))/-2
    return (math.ceil(x2) - math.floor(x1+1))
