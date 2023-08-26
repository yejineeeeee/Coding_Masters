def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

N = int(input())  # 자연수 N 입력

count = 0  # 소수 개수를 세는 변수 초기화
for i in range(1, N + 1):
    if is_prime(i):
        count += 1

print(count)  # 소수 개수 출력
