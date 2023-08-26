# 소의 무게를 입력받습니다.
weight = int(input())

# 등급을 결정하여 출력합니다.
if weight >= 200:
    print("A")
elif weight >= 180:
    print("B")
elif weight >= 150:
    print("C")
else:
    print("D")
