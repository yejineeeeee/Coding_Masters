from collections import deque
from collections import defaultdict
import numpy as np

N, M, K = map(int, input().split())
weights = [0] + [int(input()) for _ in range(N)]
graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

start = np.argmax(weights)
que = deque()
que.append(start)

ans = 0
changed = True

while que and changed:
    changed = False
    que_len = len(que)

    for _ in range(que_len):
        node = que.popleft()

        for adj in graph[node]:
            diff = abs(weights[node] - weights[adj])
            if diff > K:
                if weights[node] > weights[adj]:
                    weights[adj] += (diff - K)
                else:
                    weights[node] += (diff - K)
                ans += (diff - K)
                changed = True

            que.append(adj)

print(ans)
