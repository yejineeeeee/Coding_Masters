from itertools import permutations

def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(seq) - 1
    while seq[j] <= seq[i-1]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]
    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    return True

N, K = map(int, input().split())
seq = list(map(int, input().split()))

for _ in range(K):
    if not next_permutation(seq):
        seq.sort()

print(" ".join(map(str, seq)))
