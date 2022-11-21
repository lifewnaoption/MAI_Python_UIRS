def solve_sequence(ys):
    """Lagrange polynomial interpolation"""
    xs = range(len(ys))  # Or any array if all xi aren't evenly spaced
    def eval(n, i):
        num = den = 1
        for j in range(len(xs)):
            if i != j:
                num *= n - xs[j]
                den *= xs[i] - xs[j]
        return ys[i] * num // den
    return lambda n: sum(eval(n, i) for i in range(len(xs)))