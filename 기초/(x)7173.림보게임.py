N = int(input())  # 림보의 개수 입력

pass_through = True  # 초기에는 무사히 통과 가능하다고 가정
hit_height = 0  # 부딪힌 림보의 높이 초기화

for _ in range(N):
    height = int(input())  # 각 림보의 높이 입력
    
    if height == 160:  # 림보의 높이와 허리 높이가 같다면 통과할 수 없음
        pass_through = False
        hit_height = height
        break
    
    if height < 160:  # 허리를 젖혀 걸었을 때의 키보다 작은 높이의 림보에 부딪힘
        pass_through = False
        hit_height = height
        break

if pass_through:
    print("P")
else:
    print("I", hit_height)
