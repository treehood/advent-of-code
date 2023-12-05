import re

def p1(f):
    dests = []
    blob = f.read()
    seeds = list(map(int, re.match(r"seeds:[? \d]+", blob).group().split(": ")[1].split()))
    sand_filter = []
    rules_blob = re.finditer(r"[a-z]+-to-[a-z]+ map:\n([\d ]+\n)+", blob)
    for i, rule_blob in enumerate(rules_blob):
        rules = map(str.split, rule_blob.group().strip().split(":\n")[1].split("\n"))
        sand_filter.append({})
        for rule in rules:
            dst,src,rng = list(map(int, rule))
            sand_filter[i][range(src, src+rng)] = range(dst, dst+rng)
    for seed in seeds:
        current_src = seed
        for layer in sand_filter:
            for src in layer.keys():
                if (current_src in src):
                    current_src = layer[src][0] + (current_src - src[0])
                    break
        dests.append(current_src)


    return min(dests)

def p2(f):
    batch, *etc = f.read().split("\n\n")
    batch = batch.split(": ")[1].split()
    batch = [int(x) for x in batch]
    batch = [range(batch[i], batch[i] + batch[i+1]) for i in range(0, len(batch), 2)]

    new_batch = []
    for mapping in etc:
        ranges = mapping.split(":\n")[1].splitlines()
        ranges = [[int(i) for i in r.split()] for r in ranges]
        ranges = [(range(y,y+z), range(x,x+z)) for x,y,z in ranges]

        for b in batch:
            for x,y in ranges:
                overlap = range(max(b.start,x.start), min(b.stop,x.stop))
                if (len(overlap) == 0):
                    continue
                underflow = range(b.start, overlap.start)
                if underflow:
                    batch.append(underflow)
                overflow = range(overlap.stop, b.stop)
                if overflow:
                    batch.append(overflow)
                offset = y.start - x.start
                new_batch.append(range(overlap.start+offset, overlap.stop+offset))
                break
            else:
                # Passthrough if no mapping.
                new_batch.append(b)
        batch = new_batch
        new_batch = []
    return min([x.start for x in batch])
