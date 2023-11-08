def count_placement_cases(N):
    # dp[i][0]: i열에 학생이 배치되지 않은 경우의 수
    # dp[i][1]: i열에 학생이 배치된 경우의 수
    dp = [[0, 0] for _ in range(N + 1)]
    
    # 초기
    dp[0][0] = 1
    dp[1][0] = 1  # 1열에 학생이 배치되지 않은 경우의 수
    dp[1][1] = 1  # 1열에 학생이 배치된 경우의 수
    
    for _ in range(a-1):
        n_xx : xx + xo + ox
        
    
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]  # i열에 학생이 배치되지 않은 경우의 수
        dp[i][1] = dp[i - 1][0]  # i열에 학생이 배치된 경우의 수
    
    total_cases = dp[N][0] + dp[N][1]
    return total_cases

N = int(input())
result = count_placement_cases(N)
print(result)
