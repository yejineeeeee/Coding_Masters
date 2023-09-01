# 크루스칼 알고리즘

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x: # 루트 찾기
            self.parent[x] = self.find(self.parent[x]) # 부모 바꾸기
        return self.parent[x] # 루트 반환

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return  # 같은 그룹이면 안함

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x #y의 루트 -> x루트
        else:
            self.parent[root_x] = root_y # x의 루트 -> y루트
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1

        return True

def find_minimum_reservation_cost(N, taxi_info):
    taxi_info.sort(key=lambda x: x[2])  # 택시 예약 비용

    uf = UnionFind(N + 1)
    min_cost = 0
    for a, b, c in taxi_info:
        if uf.union(a, b):
            min_cost += c # 두 도시 간선을 최소 스패닝 트리에 추가
    
    return min_cost


N, M = map(int, input().split())
taxi_info = []
for _ in range(M):
    a, b, c = map(int, input().split())
    taxi_info.append((a, b, c))

# 최소 예약 비용 계산
result = find_minimum_reservation_cost(N, taxi_info)

print(result)
