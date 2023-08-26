N = int(input())  # 학생 수 입력
students = []  # 학생 정보를 저장할 리스트

for _ in range(N):
    name, iq = input().split()  # 이름과 IQ 입력
    students.append((name, int(iq)))  # 튜플 형태로 리스트에 추가

# 정렬 기준을 IQ 내림차순, 이름 오름차순으로 설정
students.sort(key=lambda x: (-x[1], x[0]))

# 상위 3명의 이름 출력
for i in range(3):
    print(students[i][0])
