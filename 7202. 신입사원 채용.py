# 지원자의 수 N 입력 받기
N = int(input())

# 지원자 정보 (서류 점수, 면접 점수)를 입력 받아 리스트에 저장
applicants = []
for i in range(N):
    x, y = map(int, input().split())
    applicants.append((x, y))

# 등수 계산
ranks = [1] * N  # 모든 지원자의 등수를 1로 초기화

for i in range(N):
    for j in range(N):
        if i != j:
            if applicants[i][0] < applicants[j][0] and applicants[i][1] < applicants[j][1]:
                ranks[i] += 1

# 결과 출력
print(*ranks)
