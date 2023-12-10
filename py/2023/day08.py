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

def gcd(a, b):
    # Greatest common divisor using Euclid's Algorithm.
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def p2(f):
    res = 0
    dirs, points = f.read().split("\n\n")
    points = [x.split(" = ") for x in points.splitlines()]
    points = {x: y[1:-1].split(", ") for x, y in points}

    current = [x for x in points.keys() if x[2] == "A"]
    count = 0
    first_find = {}
    for i in cycle(dirs):
        for j in range(0, len(current)):
            current[j] = points[current[j]][i == "R"]
            if (current[j][2] == "Z" and j not in first_find):
                first_find[j] = count+1
            if (len(first_find.keys()) == len(current)):
                val = first_find[0]
                for k in range(1, len(first_find)):
                    val = lcm(val, first_find[k])
                return val
        count += 1
