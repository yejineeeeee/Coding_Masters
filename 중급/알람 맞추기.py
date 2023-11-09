# 주어진 알람 시각을 입력으로 받습니다.
alarm_time = input().split(":")
HH, MM = int(alarm_time[0]), int(alarm_time[1])

# N번째 알람을 입력으로 받습니다.
N = int(input())

# 누적 분을 계산합니다. (등차수열의 합)
total_minutes = (N * (N - 1)) // 2

# 최종 알람 시각을 계산합니다.
final_HH = HH
final_MM = MM + total_minutes

# 분 단위가 60을 넘어갈 경우 시간을 업데이트합니다.
final_HH += final_MM // 60
final_MM %= 60

# 시간이 24를 넘어갈 경우 24로 나머지를 계산합니다.
final_HH %= 24

# 결과를 "HH:MM" 형태로 출력합니다.
print(f"{final_HH:02d}:{final_MM:02d}")
