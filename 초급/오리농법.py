def count_weeds_removed(field):
    n = len(field)
    weeds_removed = 0
    
    # 가로줄을 선택하여 잡초 제거
    for i in range(n):
        row = field[i]
        if 2 in row:
            continue  # 잡초가 이미 없는 행은 건너뜁니다.
        count_weeds = row.count(2)
        weeds_removed += count_weeds
        for j in range(n):
            if row[j] == 2:
                row[j] = 0  # 잡초를 제거합니다.
    
    # 세로줄을 선택하여 잡초 제거
    for j in range(n):
        col = [field[i][j] for i in range(n)]
        if 2 in col:
            continue  # 잡초가 이미 없는 열은 건너뜁니다.
        count_weeds = col.count(2)
        weeds_removed += count_weeds
        for i in range(n):
            if field[i][j] == 2:
                field[i][j] = 0  # 잡초를 제거합니다.
    
    return weeds_removed

def main():
    n = int(input())
    field = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        field.append(row)
    
    max_weeds_removed = 0
    
    # 모든 가능한 가로줄과 세로줄 조합에 대해 최대 잡초 제거 개수를 구합니다.
    for i in range(n):
        for j in range(n):
            # 가로줄과 세로줄을 하나씩 선택하여 잡초 제거
            temp_field = [row[:] for row in field]
            temp_field[i] = [0] * n
            for k in range(n):
                temp_field[k][j] = 0
            max_weeds_removed = max(max_weeds_removed, count_weeds_removed(temp_field))
    
    print(max_weeds_removed)

if __name__ == "__main__":
    main()
