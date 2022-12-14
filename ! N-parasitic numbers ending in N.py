def calc_special(d, b):
    rep = {10:'d', 8:'o', 16:'x'}[b]
    n = format(d, rep)
    while True:
        prod = format(d * int(n, b), rep)
        if n[-1:]+n[:-1] == prod: return n
        n = prod[-len(n):]+n[-1:]