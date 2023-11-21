N = int(input())
profits = list(map(int, input().split()))

max_current = max_global = profits[0]

for i in range(1, N):
    max_current = max(profits[i], max_current + profits[i])
    max_global = max(max_global, max_current)

print(max_global)
