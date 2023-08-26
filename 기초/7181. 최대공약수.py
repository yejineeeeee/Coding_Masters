def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N, M = map(int, input().split())  # 두 자연수 입력

result = gcd(N, M)  # 두 수의 최대공약수 계산

print(result)  # 최대공약수 출력
