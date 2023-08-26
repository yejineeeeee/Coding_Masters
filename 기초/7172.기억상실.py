A, B, N = map(int, input().split())

# A - B: 하루에 외울 수 있는 단어의 차이
# N - B: 목표 단어를 모두 외운 후에 B개의 단어를 잊게 됨
# ceil((N - B) / (A - B)): 목표 단어를 모두 외우는 데 필요한 날 수
import math
days = math.ceil((N - B) / (A - B))
print(days)
