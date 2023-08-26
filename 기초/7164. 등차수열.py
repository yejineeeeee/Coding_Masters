A, B, N = map(int, input().split())  # A, B, N을 공백을 기준으로 입력받아 정수로 변환합니다.

# N번째 항을 계산합니다.
result = A + (N - 1) * B  # 등차수열의 N번째 항 공식을 이용하여 계산합니다.

# 결과를 출력합니다.
print(result)
