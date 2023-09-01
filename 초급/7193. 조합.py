# 팩토리얼 계산 함수
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 조합 계산 함수
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# 입력 받기
A, B = map(int, input().split())

# 조합 계산 및 출력
result = combination(A, B)
print(result)
