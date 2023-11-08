def is_good_array(N, a):
    first_occurrence = {}  # 각 숫자의 첫 번째 등장 인덱스를 기록할 딕셔너리
    second_occurrence = {}  # 각 숫자의 두 번째 등장 인덱스를 기록할 딕셔너리

    for i in range(2 * N):
        if a[i] not in first_occurrence:
            first_occurrence[a[i]] = i
        else:
            if a[i] not in second_occurrence:
                second_occurrence[a[i]] = i
            else:
                return "NO"

    for num, first_index in first_occurrence.items():
        if num in second_occurrence:
            second_index = second_occurrence[num]
            if first_index % 2 == second_index % 2:
                return "NO"

    return "YES"

N = int(input())
a = list(map(int, input().split()))

result = is_good_array(N, a)
print(result)
