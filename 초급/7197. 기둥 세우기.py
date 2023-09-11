# 입력값 받기
N, M = map(int, input().split())
castle = []
for _ in range(N):
    row = list(map(int, input().split()))
    castle.append(row)

# 가로 방향에서 필요한 기둥 개수 세기
horizontal_pillars = sum(1 for row in castle if 0 not in row)

# 세로 방향에서 필요한 기둥 개수 세기
vertical_pillars = sum(1 for j in range(M) if all(castle[i][j] == 1 for i in range(N)))

# 필요한 기둥의 최솟값 출력
min_pillars = max(horizontal_pillars, vertical_pillars)
print(min_pillars)
