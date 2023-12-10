from collections import Counter

def get_rank(hand):
    counts = [x for _,x in Counter(hand).most_common()]
    if (counts[0] == 5):
        return 1
    elif (counts[0] == 4):
        return 2
    elif (counts[0] == 3 and counts[1] == 2):
        return 3
    elif (counts[0] == 3):
        return 4
    elif (counts[0] == 2 and counts[1] == 2):
        return 5
    elif (counts[0] == 2):
        return 6
    else:
        return 7

def is_hand_better(hand1, hand2):
    ranking = "AKQJT98765432"
    hand1_rank = get_rank(hand1)
    hand2_rank = get_rank(hand2)

    if (hand1_rank < hand2_rank):
        return True
    elif (hand1_rank > hand2_rank):
        return False

    for i in range(0, len(hand1)):
        if (ranking.index(hand1[i]) < ranking.index(hand2[i])):
            return True
        elif (ranking.index(hand1[i]) > ranking.index(hand2[i])):
            return False
    return False

def p1(f):
    hands = [[x for x in l.split()] for l in f.readlines() ]
    scored = [(hands[0][0], int(hands[0][1]))]
    for i in range(1, len(hands)):
        hand = hands[i][0]
        bid = int(hands[i][1])
        for j, s in enumerate(scored):
            if (is_hand_better(hand, s[0])):
                scored.insert(j, (hand, bid))
                break
        else:
            scored.append((hand, bid))
    return sum((len(scored)-i)*s[1] for i, s in enumerate(scored))

def get_rank2(hand_count):
    counts = [x for _,x in hand_count]
    if (counts[0] == 5):
        return 1
    elif (counts[0] == 4):
        return 2
    elif (counts[0] == 3 and counts[1] == 2):
        return 3
    elif (counts[0] == 3):
        return 4
    elif (counts[0] == 2 and counts[1] == 2):
        return 5
    elif (counts[0] == 2):
        return 6
    else:
        return 7

def op_jokers(hand):
    hand_counter = Counter(hand).most_common()
    hand_counter = [list(e) for e in hand_counter]
    j_count = hand.count("J")
    if (j_count > 0 and len(hand_counter) > 1):
        hand = hand.replace("J", "")
        hand_counter = Counter(hand).most_common()
        hand_counter = [list(e) for e in hand_counter]
        hand_counter[0][1] = hand_counter[0][1] +  j_count

    return hand_counter

def is_hand_better2(hand1, hand2):
    ranking = "AKQT98765432J"
    hand1_rank = get_rank2(op_jokers(hand1))
    hand2_rank = get_rank2(op_jokers(hand2))

    if (hand1_rank < hand2_rank):
        return True
    elif (hand1_rank > hand2_rank):
        return False

    for i in range(0, len(hand1)):
        if (ranking.index(hand1[i]) < ranking.index(hand2[i])):
            return True
        elif (ranking.index(hand1[i]) > ranking.index(hand2[i])):
            return False
    return False

def p2(f):
    hands = [[x for x in l.split()] for l in f.readlines() ]
    scored = [(hands[0][0], int(hands[0][1]))]
    for i in range(1, len(hands)):
        hand = hands[i][0]
        bid = int(hands[i][1])
        for j, s in enumerate(scored):
            if (is_hand_better2(hand, s[0])):
                scored.insert(j, (hand, bid))
                break
        else:
            scored.append((hand, bid))
    return sum((len(scored)-i)*s[1] for i, s in enumerate(scored))
