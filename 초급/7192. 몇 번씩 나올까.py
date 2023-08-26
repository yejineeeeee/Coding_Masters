def count_digits(n):
    digit_count = [0] * 10

    for i in range(1, n + 1):
        number = i
        while number > 0:
            digit = number % 10
            digit_count[digit] += 1
            number //= 10
    
    return digit_count

N = int(input())

result = count_digits(N)

# 결과 출력
print(*result)
