import re

def p1(f):
    lines = f.readlines()
    res = 0
    for line in lines:
        numbers = line.split(":")[1]
        winning, have = numbers.split("|")
        winning = re.split(" +", winning.strip())
        have = re.split(" +", have.strip())
        won = []
        for n in have:
            if n in winning:
                won.append(n)
        if (len(won) > 0):
            res += 2**(len(won)-1)
    return res

def p2(f):
    lines = f.read().splitlines()
    card_count = [1 for i in range(len(lines))]
    res = 0
    for i, line in enumerate(lines):
        numbers = line.split(":")[1]
        winning, have = numbers.split("|")
        winning = re.split(" +", winning.strip())
        have = re.split(" +", have.strip())
        won = []
        for n in have:
            if n in winning:
                won.append(n)
        for j in range(i+1, min(len(lines), i+len(won)+1)):
            card_count[j] += card_count[i]
        res += card_count[i]
    return res
