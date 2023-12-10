from itertools import cycle

def p1(f):
    res = 0
    dirs, points = f.read().split("\n\n")
    points = [x.split(" = ") for x in points.splitlines()]
    points = {x: y[1:-1].split(", ") for x, y in points}

    current = "AAA"
    count = 0
    for i in cycle(dirs):
        current = points[current][i == "R"]
        count += 1
        if (current == "ZZZ"):
            return count

def p2(f):
    return 0
