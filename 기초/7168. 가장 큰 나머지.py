N = int(input())

# N을 5로 나눈 나머지와 7로 나눈 나머지 중 더 큰 값을 출력합니다.
# 나머지가 같은 경우에도 하나의 값만 출력합니다.
remainder_5 = N % 5
remainder_7 = N % 7

if remainder_5 > remainder_7:
    print(remainder_5)
else:
    print(remainder_7)
