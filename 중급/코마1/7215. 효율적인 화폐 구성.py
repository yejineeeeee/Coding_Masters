def min_coin_count(N, M, coins):
    # 최소 동전 개수 저장
    dp = [10001] * (M + 1)
    dp[0] = 0  # 0원->동전 0개
    
    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[M] == 10001:
        return -1  # 만들 수 없는 경우
    else:
        return dp[M]

N, M = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

result = min_coin_count(N, M, coins)
print(result)
