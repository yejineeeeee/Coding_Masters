def find_element_position(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid + 1  # 인덱스는 0부터 시작하지만 문제에서는 1부터 시작
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # 원소를 찾지 못했을 경우

# N과 특정 원소를 입력받습니다.
N, target = map(int, input().split())

# 정렬된 정수 리스트를 입력받습니다.
sorted_list = list(map(int, input().split()))

# 원소의 위치를 찾고 출력합니다.
position = find_element_position(sorted_list, target)
print(position)
