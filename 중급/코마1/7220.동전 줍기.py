# 입력 받기
N = int(input())
coins = []  # 동전 정보를 저장할 리스트

for i in range(N):
    coins.append(list(map(int, input().split())))

# 다이나믹 프로그래밍을 위한 2차원 리스트 초기화
dp = [[0] * (i + 1) for i in range(N)]

# 초기값 설정
dp[0][0] = coins[0][0]

# 다이나믹 프로그래밍 수행
for i in range(1, N):
    for j in range(i + 1):
        if j == 0:  # 가장 왼쪽 위치에서는 오른쪽으로만 이동 가능
            dp[i][j] = dp[i - 1][j] + coins[i][j]
        elif j == i:  # 가장 오른쪽 위치에서는 왼쪽으로만 이동 가능
            dp[i][j] = dp[i - 1][j - 1] + coins[i][j]
        else:  # 중간 위치에서는 왼쪽이나 오른쪽 중 큰 값 선택
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + coins[i][j]

# 최대값 찾기
max_coins = max(dp[N - 1])

# 결과 출력
print(max_coins)
