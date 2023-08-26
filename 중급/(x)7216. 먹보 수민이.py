import heapq

def min_convenience_store_visits(N, stores, L, P):
    stores.sort()  # 편의점을 위치 기준으로 오름차순 정렬
    
    heap = []  # 힙을 사용하여 포만감을 최대화하도록 편의점 정보를 저장
    refuel_count = 0  # 편의점 방문 횟수
    current_position = 0  # 수민의 현재 위치
    
    for distance, appetite in stores:
        diff = distance - current_position
        
        while P < diff:
            if not heap:
                print("-1")
                return
            P += -heapq.heappop(heap)
            refuel_count += 1
        
        P -= diff
        current_position = distance
        heapq.heappush(heap, -appetite)
    
    while P < L - current_position:
        if not heap:
            print("-1")
            return
        P += -heapq.heappop(heap)
        refuel_count += 1
    
    print(refuel_count)

# 입력 받기
N = int(input())
stores = []
for _ in range(N):
    a, b = map(int, input().split())
    stores.append((a, b))
L, P = map(int, input().split())

# 최소 편의점 방문 횟수 계산
min_convenience_store_visits(N, stores, L, P)
