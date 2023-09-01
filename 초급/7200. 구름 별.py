# 양의 정수 N 입력 받기
N = int(input())

# 크기가 N인 구름 별 출력
for i in range(N):
    # 각 줄에 별표 출력 (2개씩)
    for j in range(2):
        print("*", end="")
    
    print()  # 줄 바꿈
