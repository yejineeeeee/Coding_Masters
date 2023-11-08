def calculate_additional_hits(x, y):
    target_average = y / x  
    
    # 만약 현재 타율이 1일 경우
    if target_average == 1:
        return -1
    
    # 앞으로 더 나가야 할 횟수
    additional_hits = int((target_average * (x + 1)) - y)
    
    if additional_hits > 1000000000:
        return -1
    
    return additional_hits

x, y = map(int, input().split())  # 지금까지 타석에 들어선 횟수와 안타를 친 횟수

result = calculate_additional_hits(x, y)
print(result)
