# 세 각의 크기를 입력받습니다.
angle1, angle2, angle3 = map(int, input().split())

# 세 각의 합이 180도이고 각각의 각이 0도보다 크다면 버뮤다 삼각형이 될 수 있습니다.
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("P")
else:
    print("F")
