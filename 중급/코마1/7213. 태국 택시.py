# 크루스칼 알고리즘을 위한 유니온 파인드(Union-Find) 구현
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())

# 모든 택시 정보를 저장할 리스트 생성
taxis = []

# 택시 정보 입력 및 정렬
for _ in range(M):
    a, b, c = map(int, input().split())
    taxis.append((c, a, b))

taxis.sort()

# 부모 노드 초기화
parent = [i for i in range(N + 1)]

# 최소 비용 초기화
total_cost = 0

# 크루스칼 알고리즘 수행
for cost, a, b in taxis:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

# 출력
print(total_cost)
