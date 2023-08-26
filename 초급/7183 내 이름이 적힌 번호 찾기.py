def find_yeongdeok(name_list, yeongdeok):
    for i, name in enumerate(name_list, start=1):
        if name == yeongdeok:
            return i
    return -1  # 만약 영덕의 이름을 못 찾으면 -1을 반환

# N명의 이름이 적힌 목록과 영덕의 영어 이름을 입력받습니다.
N, yeongdeok = input().split()
N = int(N)
name_list = input().split()

# 영덕의 영어 이름이 몇 번째인지 찾습니다.
position = find_yeongdeok(name_list, yeongdeok)

if position != -1:
    print(position)
else:
    print("영덕의 이름을 목록에서 찾을 수 없습니다.")
