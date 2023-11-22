def rps_game(N, M, bot1, bot2):
    round = 0
    offensive = 0
    while True:
        if round >= N * M * 10:  # 영원히 승부를 계속하게 되는 경우
            return 0
        turn1 = bot1[round % N]
        turn2 = bot2[round % M]
        if turn1 == turn2:  # 같은 손 모양을 낸 경우
            if offensive != 0:  # 선공이 정해진 상태라면
                return offensive  # 선공 승리
        elif (turn1 == 1 and turn2 == 3) or (turn1 == 2 and turn2 == 1) or (turn1 == 3 and turn2 == 2):  # 첫 번째 묵찌빠봇이 이긴 경우
            offensive = 1
        else:  # 두 번째 묵찌빠봇이 이긴 경우
            offensive = 2
        round += 1

# 입력값 받기
N, M = map(int, input().split())
bot1 = list(map(int, input().split()))
bot2 = list(map(int, input().split()))

# 묵찌빠 진행
print(rps_game(N, M, bot1, bot2))
