def prime_factorization(x):
    factors = []
    for i in range(2, x + 1):
        if x % i == 0:
            count = 0
            while x % i == 0:
                x //= i
                count += 1
            factors.append((i, count))
    return factors

def count_factor(x, factor):
    count = 0
    while x:
        x //= factor
        count += x
    return count

p, n = map(int, input().split())
factors = prime_factorization(p)
min_zeros = float('inf')

for factor, count in factors:
    min_zeros = min(min_zeros, count_factor(n, factor) // count)

print(min_zeros)
