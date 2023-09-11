# 입력값 파싱
year, branch, mobilization, status = input().split()

# 연차를 정수로 변환
year = int(year)

# 훈련 시간 계산 함수
def calculate_training_time(year, branch, mobilization, status):
    if status == "Private":
        if year == 0 and mobilization == "N":
            return 0
        elif 1 <= year <= 4 and mobilization == "N":
            if branch == "ROKA" or branch == "ROKN":
                return 32
            else:
                return 28
        elif 5 <= year <= 6 and mobilization == "N":
            return 20
    elif status == "Officer":
        if year == 0 and mobilization == "N":
            return 0
        elif 1 <= year <= 6 and mobilization == "N":
            return 28

    # 조건에 해당하지 않는 경우
    return -1

# 훈련 시간 계산
training_time = calculate_training_time(year, branch, mobilization, status)

# 결과 출력
print(training_time)
