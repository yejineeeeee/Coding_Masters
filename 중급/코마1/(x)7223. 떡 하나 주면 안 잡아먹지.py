# dynamic programing으로 함

N = int(input())
grid = []

for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# dp[i][j]: (1, 1)에서 출발하여 (i, j)까지 도달하는 데 필요한 최소 떡의 개수
dp = [[0] * N for _ in range(N)]
dp[0][0] = grid[0][0]

# 첫 번째 행 초기화
for i in range(1, N):
    dp[0][i] = dp[0][i - 1] + grid[0][i]

# 첫 번째 열 초기화
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + grid[i][0]

# 다이나믹 프로그래밍 수행
for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

# 결과 출력
print(dp[N - 1][N - 1])
