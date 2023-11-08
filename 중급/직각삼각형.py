solutions = {}  # 가능한 직각삼각형의 둘레와 개수를 저장할 딕셔너리

p = int(input())  # 입력으로 둘레를 받음

# 가능한 둘레 범위 내에서 세 변의 길이를 조사
for a in range(1, p // 2):
    for b in range(a, p // 2):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c > p:
            break
        if c.is_integer():
            perimeter = a + b + int(c)
            if perimeter in solutions:
                solutions[perimeter] += 1
            else:
                solutions[perimeter] = 1

max_triangles = max(solutions.values())  # 가장 많이 발견된 직각삼각형의 개수
min_perimeter = min([perimeter for perimeter, count in solutions.items() if count == max_triangles])  # 최소 둘레

print(min_perimeter, max_triangles)
