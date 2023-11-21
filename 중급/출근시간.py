import heapq
import sys

def dijkstra(graph, start, end):
    # 최단 거리 테이블 초기화
    distance = {node: sys.maxsize for node in graph}
    distance[start] = 0

    # 우선순위 큐 초기화
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # 현재 노드까지의 거리가 이미 갱신된 경우 무시
        if current_distance > distance[current_node]:
            continue

        # 현재 노드와 연결된 인접 노드들을 확인
        for neighbor, weight in graph[current_node]:
            total_distance = current_distance + weight

            # 더 짧은 경로를 찾은 경우 업데이트
            if total_distance < distance[neighbor]:
                distance[neighbor] = total_distance
                heapq.heappush(queue, (total_distance, neighbor))

    return distance[end]

def find_min_time(N, M, K, roads):
    # 그래프 초기화
    graph = {i: [] for i in range(1, N + 1)}

    # 도로 정보 입력
    for road in roads:
        u, v, w = road
        graph[u].append((v, w))

    # 철수의 집에서 자녀의 학교로 가는 최단 거리
    home_to_school = dijkstra(graph, 1, K)

    # 자녀의 학교에서 철수의 회사로 가는 최단 거리
    school_to_office = dijkstra(graph, K, N)

    # 집에서 학교를 들러 회사로 가는 최소 시간
    min_time = home_to_school + school_to_office

    return min_time

# 입력 받기
N, M, K = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

# 함수 호출 및 결과 출력
result = find_min_time(N, M, K, roads)
print(result)
