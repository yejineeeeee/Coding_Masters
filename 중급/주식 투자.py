N, K = map(int, input().split())
dp = [[0]*2001 for _ in range(N+1)]
dp[0][1000] = 1
for i in range(N):
    for j in range(2000):
        if dp[i][j] > 0:
            dp[i+1][j+100] += dp[i][j]
            dp[i+1][j-100] += dp[i][j]
print(dp[N][1000+K])
