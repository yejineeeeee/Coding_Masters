N = int(input())  # 10진수 정수 N을 입력받아 정수로 변환합니다.

# N을 8진수와 16진수로 변환하여 출력합니다.
octal_representation = oct(N)[2:]  # 8진수로 변환한 값을 가져옵니다. [2:]는 "0o" 접두사를 제외하기 위해 슬라이싱합니다.
hexadecimal_representation = hex(N)[2:].upper()  # 16진수로 변환한 값을 가져옵니다. [2:]는 "0x" 접두사를 제외하기 위해 슬라이싱합니다. .upper()는 대문자로 변환합니다.

print(octal_representation, hexadecimal_representation)
