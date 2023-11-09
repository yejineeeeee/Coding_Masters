def solve(n):
    ans = 0
    while n > 1:
        ans += n // 2
        n = (n + 1) // 2
    return ans

n = int(input())
print(solve(n))

