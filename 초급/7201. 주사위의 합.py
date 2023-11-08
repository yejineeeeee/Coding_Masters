# 정수 N 입력 받기
N = int(input())

# 주사위 2개를 굴려 합이 N이 되는 경우 출력
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == N:
            print(f"{i} {j}")
