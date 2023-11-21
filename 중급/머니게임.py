def money_game(N, M):
    while N >= 2 * M or M >= 2 * N:
        if N >= 2 * M:
            N %= 2 * M
        elif M >= 2 * N:
            M %= 2 * N
        if N == 0 or M == 0:
            break
    return N, M

N, M = map(int, input().split())
N, M = money_game(N, M)
print(N, M)
