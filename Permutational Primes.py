from collections import defaultdict
from math import isqrt

MAX = 10 ** 5
sieve = [1] * (MAX + 1)
for i in range(2, isqrt(MAX) + 1):
    if sieve[i]:
        for j in range(i * i, MAX + 1, i): sieve[j] = 0
MEMO = defaultdict(list)
for i in range(3, MAX + 1, 2):
    if sieve[i]: MEMO[tuple(sorted(str(i)))].append(i)

def permutational_primes(n: int, k: int) -> list:
    res = [perms[0] for perms in MEMO.values() if sum(p <= n for p in perms) == k + 1]
    return [len(res), res[0], res[-1]] if res else [0, 0, 0]