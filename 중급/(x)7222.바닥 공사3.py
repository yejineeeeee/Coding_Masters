def count_ways_to_fill_floor(n):
    dp = [0] * (n + 1)  
    
    dp[1] = 1
    dp[2] = 3
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 796796
    
    return dp[n]

n = int(input())  
result = count_ways_to_fill_floor(n)
print(result)
