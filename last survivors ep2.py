from collections import Counter

def shift(c):
    return chr( (ord(c) - 96) % 26 + 97 )

def last_survivors(string):
    c = Counter(string)
    while True:
        for k,v in c.items():
            if v > 1:
                c[k] = v % 2
                c[shift(k)] += v // 2
                break
        else:
            return "".join(c.elements())