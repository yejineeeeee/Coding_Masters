R = int(input())  # 원의 반지름 입력
PI = 3.14  # 원주율 값

area = R * R * PI  # 원의 넓이 계산

if area.is_integer():
    print(int(area))  # 넓이가 정수인 경우 정수로 출력
else:
    print(format(area, ".1f")) 
