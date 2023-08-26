# 아버지와 어머니의 키를 입력받습니다.
father_height, mother_height = map(int, input().split())

# 자녀의 예상 키를 계산하여 출력합니다.
child_height = (father_height + mother_height) // 2
print(child_height)
