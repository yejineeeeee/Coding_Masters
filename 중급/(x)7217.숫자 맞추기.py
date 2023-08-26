from collections import deque

def min_operations_to_reach_target(N, K):
    visited = [False] * (N + 1)  # 방문 여부
    queue = deque([(K, 0)])  # 시작 숫자와 횟수
    
    while queue:
        current_number, count = queue.popleft()
        
        if current_number == N:  # 목표 숫자에 도달한 경우
            return count
        
        # 1을 더한 숫자를 검사
        if current_number + 1 <= N and not visited[current_number + 1]:
            queue.append((current_number + 1, count + 1))
            visited[current_number + 1] = True
        
        # 1을 뺀 숫자를 검사
        if current_number - 1 >= 0 and not visited[current_number - 1]:
            queue.append((current_number - 1, count + 1))
            visited[current_number - 1] = True
        
        # 2를 곱한 숫자를 검사
        if current_number * 2 <= N and not visited[current_number * 2]:
            queue.append((current_number * 2, count + 1))
            visited[current_number * 2] = True
    
    return -1  # 목표 숫자에 도달할 수 없는 경우

N, K = map(int, input().split())

result = min_operations_to_reach_target(N, K)
print(result)
