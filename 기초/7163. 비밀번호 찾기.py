input_string = input().split()  # 알파벳들을 공백을 기준으로 분리하여 리스트에 저장합니다.

password = []  # 비밀번호를 저장할 리스트를 초기화합니다.

# 입력된 알파벳들을 순회하면서 비밀번호를 추출합니다.
for char in input_string:
    password.append(char)  # 현재 알파벳을 비밀번호 리스트에 추가합니다.
    if char == 'c':  # 알파벳 'c'가 입력되면 비밀번호의 마지막 글자임을 의미합니다.
        break  # 반복문을 종료합니다.

# 추출된 비밀번호를 공백을 기준으로 문자열로 변환하여 출력합니다.
print(' '.join(password))
