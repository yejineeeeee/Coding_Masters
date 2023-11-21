def find_optimal_start_day(N, K, visitors):
    max_average = 0
    current_sum = sum(visitors[:K])
    start_day = 0

    for i in range(K, N):
        current_sum += visitors[i] - visitors[i - K]
        current_average = current_sum / K

        if current_average > max_average:
            max_average = current_average
            start_day = i - K + 1

    return start_day + 1

N, K = map(int, input().split())
visitors = list(map(int, input().split()))

result = find_optimal_start_day(N, K, visitors)
print(result)

def solution(n, accounts, transfers):
    answer = []
    return answer