def p1(f):
    lines = f.readlines()
    res = 0
    for line in lines:
        first_int = 0
        last_int = 0
        for char in line:
            if char.isdigit():
                if first_int == 0:
                    first_int = char
                last_int = char
        res += int("{}{}".format(first_int, last_int))
    return res

def p2(f):
    letters = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    lines = f.readlines()
    res = 0
    for line in lines:
        first_int = 0
        last_int = 0
        for i in range(0, len(line)):
            char = line[i]
            if char.isdigit():
                if first_int == 0:
                    first_int = char
                last_int = char
            else:
                for k in letters:
                    if line[i:i+len(k)] == k:
                        if first_int == 0:
                            first_int = '{}'.format(letters[k])
                        last_int = '{}'.format(letters[k])
                        i+=len(k)-1

        res += int("{}{}".format(first_int, last_int))
    return res
