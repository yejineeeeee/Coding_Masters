N = int(input()) 

# 하루 동안 숫자 N을 볼 수 있는 시간을 세기 위한 변수 초기화
count = 0

# 시간 범위 순회 (00:00:00부터 23:59:59까지)
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            # 시, 분, 초를 문자열로 변환하여 숫자 N이 포함되어 있는지 확인
            time_str = f"{hour:02d}{minute:02d}{second:02d}"
            if str(N) in time_str:
                count += 1

print(count)
