input_data = input().split()

# 연차, 군별, 동원지정여부, 신분
year = int(input_data[0])
branch = input_data[1]
call_up = input_data[2]
rank = input_data[3]

# 연간 훈련 시간 계산
training_hours = 0

if rank == "Private":
    if year == 0:
        training_hours = 0
    elif 1 <= year <= 4:
        if branch == "ROKA" or branch == "ROKN":
            training_hours = 32
        if call_up == "Y" or branch == "ROKAF":
            training_hours = 28
    elif 5 <= year <= 6:
        training_hours = 20
elif rank == "Officer":
    if year == 0:
        training_hours = 0
    elif 1 <= year <= 6:
        training_hours = 28

print(training_hours)
