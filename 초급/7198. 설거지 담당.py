# 요일 번호 입력 받기
N = int(input())

# 요일 번호에 따라 설거지를 해야 하는지 판단하여 출력
if N in [1, 3, 5, 7]:
    print("RUN")
else:
    print("STAY")
