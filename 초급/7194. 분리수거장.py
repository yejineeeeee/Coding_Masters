# 입력 받기
N = int(input())  # 아파트 단지의 수

# 아파트 단지의 위치와 주민 수 저장
apartments = []
for i in range(N):
    D, A = map(int, input().split())
    apartments.append((D, A, i + 1))  # (아파트 단지 위치, 주민 수, 아파트 단지 번호) 저장

# 아파트 단지를 위치(D)를 기준으로 정렬
apartments.sort(key=lambda x: x[0])

# 최소 거리 합을 초기화
min_distance_sum = float('inf')
selected_apartment = -1

# 각 아파트 단지를 분리수거장으로 선택해보면서 최소 거리 합 계산
for i in range(N):
    distance_sum = 0
    for j in range(N):
        distance_sum += abs(apartments[i][0] - apartments[j][0]) * apartments[j][1]
    
    # 최소 거리 합인 경우 업데이트
    if distance_sum < min_distance_sum:
        min_distance_sum = distance_sum
        selected_apartment = apartments[i][2]

# 결과 출력
print(selected_apartment)
