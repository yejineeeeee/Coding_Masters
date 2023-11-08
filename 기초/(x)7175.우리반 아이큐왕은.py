# 학생 수 입력
N = int(input())

# 학생 정보를 저장할 리스트 생성
students = []

# 학생 정보 입력 및 저장
for _ in range(N):
    name, iq = input().split()
    students.append((name, int(iq)))

# IQ 기준으로 내림차순 정렬하되, 같은 IQ일 경우 이름을 기준으로 정렬
students.sort(key=lambda x: (-x[1], x[0]))

# 상위 3명 출력
for i in range(3):
    print(students[i][0])
