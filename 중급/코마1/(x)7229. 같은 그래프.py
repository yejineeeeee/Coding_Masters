def are_graphs_equal(graph1, graph2):
    # 그래프의 정점 집합과 간선 집합이 서로 같은지 확인
    if len(graph1) != len(graph2):
        return False

    for u in graph1:
        if u not in graph2:
            return False

        # 정점 u의 인접한 정점들을 정렬하여 비교
        if sorted(graph1[u]) != sorted(graph2[u]):
            return False

    return True

# 입력 받기
n1, m1 = map(int, input().split())  # 첫 번째 그래프의 정점 수와 간선 수
graph1 = {}  # 첫 번째 그래프의 정점과 인접한 정점을 저장할 딕셔너리
for _ in range(m1):
    u, v = map(int, input().split())  # 첫 번째 그래프의 간선 정보
    if u not in graph1:
        graph1[u] = []
    if v not in graph1:
        graph1[v] = []
    graph1[u].append(v)
    graph1[v].append(u)

n2, m2 = map(int, input().split())  # 두 번째 그래프의 정점 수와 간선 수
graph2 = {}  # 두 번째 그래프의 정점과 인접한 정점을 저장할 딕셔너리
for _ in range(m2):
    u, v = map(int, input().split())  # 두 번째 그래프의 간선 정보
    if u not in graph2:
        graph2[u] = []
    if v not in graph2:
        graph2[v] = []
    graph2[u].append(v)
    graph2[v].append(u)

# 두 그래프가 같은지 확인
if are_graphs_equal(graph1, graph2):
    print("YES")
else:
    print("NO")
