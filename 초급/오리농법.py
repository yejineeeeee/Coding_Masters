def min_grass_to_remove(field):
    n = len(field)
    row_grass = [0] * n
    col_grass = [0] * n

    # 각 행과 열에 작물과 잡초가 얼마나 있는지 계산
    for i in range(n):
        for j in range(n):
            if field[i][j] == 1:
                row_grass[i] += 1
                col_grass[j] += 1

    # 잡초만 있는 땅의 수 초기화
    grass_count = 0

    # 행과 열을 선택하면서 잡초를 먹어서 없앰
    while True:
        min_row_grass = min(row_grass)
        min_col_grass = min(col_grass)
        
        # 더 이상 선택할 행 또는 열이 없으면 종료
        if min_row_grass == n and min_col_grass == n:
            break
        
        # 행과 열 중에서 작물이 더 적은 쪽을 선택
        if min_row_grass <= min_col_grass:
            min_grass_idx = row_grass.index(min_row_grass)
            for j in range(n):
                if field[min_grass_idx][j] == 2:
                    field[min_grass_idx][j] = 0
                    grass_count += 1
            row_grass[min_grass_idx] = n
        else:
            min_grass_idx = col_grass.index(min_col_grass)
            for i in range(n):
                if field[i][min_grass_idx] == 2:
                    field[i][min_grass_idx] = 0
                    grass_count += 1
            col_grass[min_grass_idx] = n

    return grass_count

n = int(input())
field = []
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

# 남아있는 잡초만 있는 땅의 수 계산
result = min_grass_to_remove(field)

print(result)
