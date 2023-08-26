# 정점의 개수 N과 간선의 개수 M을 입력받음
N, M = map(int, input().split())

# 행렬을 2차원 리스트로 초기화
adj_matrix = [[0] * N for _ in range(N)]

# M개의 간선 정보 입력받아 인접 행렬에 표시
for _ in range(M):
    a, b = map(int, input().split())
    # 무향 그래프이므로 양쪽 1로 표시
    adj_matrix[a - 1][b - 1] = 1
    adj_matrix[b - 1][a - 1] = 1

for row in adj_matrix:
    print(*row)
