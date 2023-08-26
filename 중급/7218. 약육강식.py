def max_continuous_eating_sharks(shark_sizes):
    n = len(shark_sizes)
    dp = [1] * n  #  dp[i]는 i번째 상어를 마지막으로 하는 최대 연속 먹이 개수를 나타냅니다.
    
    for i in range(n):  # 모든 상어에 대해서 반복합니다.
        for j in range(i): 
            if shark_sizes[i] > shark_sizes[j]:  # 뒤에 있는 상어가 앞에 있는 상어를 먹을 수 있는 경우
                dp[i] = max(dp[i], dp[j] + 1)  # dp[j]에 1을 더한 값과 dp[i] 중 큰 값을 선택합니다.
    
    return max(dp)  # 최대 연속 먹이 개수를 나타냅니다.

n = int(input())  # 상어의 마리 수
shark_sizes = list(map(int, input().split())) 

result = max_continuous_eating_sharks(shark_sizes)
print(result)
