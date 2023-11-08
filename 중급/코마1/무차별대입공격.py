from itertools import product

N, K = map(int, input().split())

characters = input()

combinations = product(sorted(characters), repeat=K)
for combination in combinations:
    print(''.join(combination))
