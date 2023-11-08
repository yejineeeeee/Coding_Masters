def min_flipped_white(dots, n):
    min_white_count = float('inf')  
    
    for row in range(n):
        white_count = dots[row].count('W')  # 해당 행의 흰색 바둑돌 개수를 세기
        min_white_count = min(min_white_count, white_count)
    
    for col in range(n):
        white_count = sum(1 for row in dots if row[col] == 'W')  # 해당 열의 흰색 바둑돌 개수를 세기
        min_white_count = min(min_white_count, white_count)
    
    return min_white_count

n = int(input())  # 바둑판의 크기 N을 입력받습니다.

# 바둑돌의 상태
dots = []
for _ in range(n):
    row = input()
    dots.append(row)

result = min_flipped_white(dots, n)
print(result)
