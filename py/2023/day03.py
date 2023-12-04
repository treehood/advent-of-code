import re

def p1(f):
    res = 0
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            # Clamp box around digits to grid size.
            start = max(0, match.start()-1)
            end = min(len(line)-1, match.end()+1)
            i_up = max(0, i-1)
            i_down = min(len(line)-1, i+1)
            chars = ""
            chars += lines[i_up][start:end]
            chars += lines[i][start:end]
            chars += lines[i_down][start:end]
            symbols = re.findall(r"[^\d.]", chars)
            if (len(symbols) > 0):
                res += int(match.group())
    return res

def p2(f):
    res = 0
    found = {}
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            adj = [(i, match.start()-1), (i, match.end())]
            adj += [(i-1, j) for j in range(match.start()-1, match.end()+1)]
            adj += [(i+1, j) for j in range(match.start()-1, match.end()+1)]
            for x, y in adj:
                if (x >= 0) and (x < len(lines)) and (y >= 0) and (y < len(lines[x])) and lines[x][y] == "*":
                    if (x,y) not in found.keys():
                        found[(x,y)] = []
                    found[(x,y)].append(match.group())
    for v in found.values():
        if len(v) == 2:
            res += int(v[0]) * int(v[1])
    return res
