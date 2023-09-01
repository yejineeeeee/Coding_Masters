# 림보 게임을 통과할 수 있는지 판단하는 함수
def pass_limbo(N, heights):
    for i in range(N):
        if heights[i] == 160:
            return 'I ' + str(heights[i])
        elif heights[i] < 160:
            return 'I ' + str(heights[i])
    return 'P'

# 입력값 받기
N = int(input())
heights = list(map(int, input().split()))

# 결과 계산
result = pass_limbo(N, heights)

# 결과 출력
print(result)
