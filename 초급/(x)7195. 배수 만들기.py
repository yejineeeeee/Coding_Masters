import itertools

def find_largest_multiple(N, numbers):
    # 가능한 모든 순열을 생성합니다.
    permutations = itertools.permutations(numbers)
    
    largest_multiple = -1  # 가장 큰 300의 배수를 저장할 변수
    
    for perm in permutations:
        # 순열을 이어붙여서 숫자를 만듭니다.
        concatenated_number = ''.join(map(str, perm))
        
        # 만든 숫자가 0이 아니고, 0으로 시작하지 않는 경우에만 300의 배수인지 확인합니다.
        if concatenated_number != '0' and int(concatenated_number) % 300 == 0:
            largest_multiple = max(largest_multiple, int(concatenated_number))
    
    # 가능한 모든 조합 중 300의 배수가 없는 경우 -1을 반환합니다.
    if largest_multiple == -1:
        return '-1'
    
    return str(largest_multiple)

# 입력값을 받습니다.
N = int(input())
numbers = list(map(int, input().split()))

# 결과를 출력합니다.
print(find_largest_multiple(N, numbers))
