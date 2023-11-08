def is_good_array(N, a):
    first_occurrence = {}  # 각 숫자의 첫 번째 등장 인덱스를 기록할 딕셔너리
    second_occurrence = {}  # 각 숫자의 두 번째 등장 인덱스를 기록할 딕셔너리

    for i in range(2 * N):
        if a[i] not in first_occurrence:
            # 처음 보는 숫자라면, 첫 번째 등장 인덱스를 저장
            first_occurrence[a[i]] = i
        else:
            if a[i] not in second_occurrence:
                # 이미 한 번 등장한 숫자이지만, 아직 두 번째 등장 인덱스가 없다면, 두 번째 등장 인덱스를 저장
                second_occurrence[a[i]] = i
            else:
                # 이미 두 번 이상 등장한 숫자가 또 등장하면 조건을 만족하지 않으므로 "NO" 반환
                return "NO"

    for num, first_index in first_occurrence.items():
        if num in second_occurrence:
            second_index = second_occurrence[num]
            # 같은 숫자가 두 번 이상 등장한 경우, 두 번째 등장 인덱스와 첫 번째 등장 인덱스의 홀/짝 여부를 비교하여 조건을 확인
            if first_index % 2 == second_index % 2:
                return "NO"

    # 모든 조건을 통과하면 "YES" 반환
    return "YES"

N = int(input())
a = list(map(int, input().split()))

result = is_good_array(N, a)
print(result)
