N = int(input())  # 피자 조각의 개수 입력

# 각 사람이 먹는 조각의 개수를 구하고 합산
pieces_per_person = N // 3
total_leftover = N - (pieces_per_person * 3)

# 냉장고에 넣어둘 조각의 최소 개수 출력
print(total_leftover)
