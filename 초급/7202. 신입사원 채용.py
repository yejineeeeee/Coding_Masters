import sys

N = int(sys.stdin.readline())
candidates = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    candidates.append((x, y))

ranks = [1] * N

for i in range(N):
    for j in range(N):
        if i != j:
            if candidates[i][0] < candidates[j][0] and candidates[i][1] < candidates[j][1]:
                ranks[i] += 1
            elif candidates[i][0] == candidates[j][0] and candidates[i][1] < candidates[j][1]:
                ranks[i] += 1
            elif candidates[i][0] < candidates[j][0] and candidates[i][1] == candidates[j][1]:
                ranks[i] += 1
                
for i in range(N):
    temp = ranks[i]
    flag = 0
    for j in range(N):
        if i != j and temp > ranks[j]:
            if candidates[i][0] > candidates[j][0] or candidates[i][1] > candidates[j][1]:
                temp = ranks[j]
                flag = 1
    if flag == 1:
        for j in range(N):
            if i != j and temp < ranks[j] and ranks[j] <= ranks[i]:
                ranks[j] = temp
        ranks[i] = temp
            
print(' '.join(map(str,ranks)))