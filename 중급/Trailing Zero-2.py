def count_five(x):
    count = 0
    while x:
        x //= 5
        count += x
    return count

n = int(input())
left, right = 0, n * 5

while left <= right:
    mid = (left + right) // 2
    if count_five(mid) >= n:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
