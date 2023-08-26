def max_collected_coins(triangle, n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]  
    
    # 아래에서부터 시작
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1]) # 현재 위치의 동전 개수와 아래쪽에서 더 많이 주울 수 있는 위치의 최대 동전 개수를 더한 값
    
    return dp[1][1]  # 산 정상에서 시작해서 주울 수 있는 최대 동전 개수를 반환합니다.

n = int(input())  # 산의 높이

# 산에 떨어진 동전의 개수
triangle = []
for _ in range(n):
    row = list(map(int, input().split()))
    triangle.append([0] + row)  # 산의 모양을 맞추기 위해 첫 번째 열에 0을 추가합니다.

result = max_collected_coins(triangle, n)
print(result)
