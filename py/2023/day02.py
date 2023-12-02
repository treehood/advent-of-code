import re

def p1(f):
    lines = f.readlines()
    maxs = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    res = 0
    for line in lines:
        game_values = line.split(': ')
        game_num = game_values[0].split(' ')[1]

        is_valid = True
        num_color = re.split(', |; ', game_values[1].strip())
        for pair in num_color:
            values = pair.split(' ')
            if (int(values[0]) > maxs[values[1]]):
                is_valid = False
                break
        if is_valid:
            res += int(game_num)
    return res
def p2(f):
    lines = f.readlines()
    res = 0
    for line in lines:
        mins = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        game_values = line.split(': ')
        game_num = game_values[0].split(' ')[1]

        is_valid = True
        num_color = re.split(', |; ', game_values[1].strip())
        for pair in num_color:
            values = pair.split(' ')
            current_min = mins[values[1]]
            if (int(values[0]) > current_min):
                mins[values[1]] = int(values[0])
        res += mins['red'] * mins['green'] * mins['blue']

    return res
