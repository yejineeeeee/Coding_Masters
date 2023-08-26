def count_ways_to_fill_floor(N):
    # N이 1일 경우
    if N == 1:
        return 1
    # N이 2일 경우
    if N == 2:
        return 2
    
    # N이 3 이상인 경우
    dp = [0] * (N + 1)
    dp[1] = 1  # 1번째 칸을 채우는 방법의 수
    dp[2] = 2  # 2번째 칸을 채우는 방법의 수
    
    # 3번째부터 N번째까지의 칸을 채우는 방법의 수 계산
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 796796
    
    # N번째 칸을 채우는 방법의 수 반환
    return dp[N]

# 가로 길이
N = int(input())

ways = count_ways_to_fill_floor(N)

print(ways)
