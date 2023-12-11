
def p1(f):
    res = 0
    for l in f.readlines():
        vals = [int(x) for x in l.split()]
        all_zeros = False
        orig_pass_len = len(vals)
        start = 0
        end = orig_pass_len
        length = 0
        all_zero = False
        while (not all_zero):
            all_zero = True
            for i in range(start, end-1):
                if (vals[i] != 0):
                    all_zero = False
                val = vals[i+1] - vals[i]
                vals.append(val)
            length = end-start-1
            start = end
            end = start + length
        offset = 1
        val = vals[-offset]
        while (length != orig_pass_len):
            offset += length
            length += 1
            val += vals[-offset]
        res += val
    return res

def p2(f):
    res = 0
    for l in f.readlines():
        vals = [int(x) for x in l.split()]
        vals.reverse()
        all_zeros = False
        orig_pass_len = len(vals)
        start = 0
        end = orig_pass_len
        length = 0
        all_zero = False
        while (not all_zero):
            all_zero = True
            for i in range(start, end-1):
                if (vals[i] != 0):
                    all_zero = False
                val = vals[i+1] - vals[i]
                vals.append(val)
            length = end-start-1
            start = end
            end = start + length
        offset = 1
        val = vals[-offset]
        while (length != orig_pass_len):
            offset += length
            length += 1
            val += vals[-offset]
        res += val
    return res
