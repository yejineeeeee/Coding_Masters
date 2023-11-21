N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0] * (K+1)
distinct = 0
answer = N
left = 0

for right in range(N):
    if cnt[A[right]] == 0:
        distinct += 1
    cnt[A[right]] += 1
    
    while distinct == K:
        answer = min(answer, right - left + 1)
        cnt[A[left]] -= 1
        if cnt[A[left]] == 0:
            distinct -= 1
        left += 1

print(answer)
