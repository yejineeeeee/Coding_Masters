def count_moles(board):
    count = 0
    for row in board:
        for cell in row:
            if cell == 'T':  # 'T'인 경우만 카운트 증가
                count += 1
    return count


input_board = []
for _ in range(8):
    row = input().strip()
    input_board.append(row)

result = count_moles(input_board)

print(result)
