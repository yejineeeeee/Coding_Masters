id_str = input()

# 아이디의 길이가 20을 넘거나 영어 소문자, 대문자 이외의 문자가 포함되어 있다면 "I" 출력
# 그렇지 않다면 "P" 출력
if len(id_str) > 20 or not id_str.isalpha():
    print("I")
else:
    print("P")
