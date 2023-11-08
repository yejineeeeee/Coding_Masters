def count_passed_students(scores, P, K):
    passed = [1 if score >= P else 0 for score in scores]
    for i in range(1, len(scores)):
        passed[i] += passed[i - 1]
    
    max_passed = 0
    for i in range(K - 1, len(scores)):
        max_passed = max(max_passed, passed[i] - (passed[i - K] if i >= K else 0))
    
    return max_passed

def find_maximum_P(scores, K):
    left, right = 0, max(scores) + 1
    while left < right:
        mid = (left + right) // 2
        if count_passed_students(scores, mid, K) >= K:
            left = mid + 1
        else:
            right = mid
    return left - 1

# 학생 수 N과 합격 학생 수의 최댓값 K 입력 받기
N, K = map(int, input().split())

# 학생들의 점수 입력 받기
scores = list(map(int, input().split()))

# P의 최댓값 찾기
result = find_maximum_P(scores, K)

print(result)
