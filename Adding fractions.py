from fractions import Fraction

def add_fracs(*fracs): 
    if fracs: 
        s = str(sum(Fraction(frac) for frac in fracs))
        return s
    return ''