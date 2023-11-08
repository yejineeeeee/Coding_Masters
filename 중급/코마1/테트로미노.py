grid = [list(input()) for _ in range(5)]

# 5x5 격자를 시계 방향으로 90도 회전하는 함수
def rotate(grid):
    rotated = [['.' for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            rotated[i][j] = grid[4 - j][i]
    return rotated

# 도형이 동일한지 확인하는 함수
def is_identical(grid1, grid2):
    for i in range(5):
        for j in range(5):
            if grid1[i][j] != grid2[i][j]:
                return False
    return True

# 테트로미노가 되는지를 판별하는 함수
def is_tetromino():
    for i in range(4):
        for j in range(4):
            # '#'을 찾으면 연결된 정사각형을 확인하기 시작
            if grid[i][j] == '#':
                count = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 4 and 0 <= nj < 4 and grid[ni][nj] == '#':
                        count += 1
                # 연결된 정사각형이 1개가 아니면 테트로미노 아님
                if count != 1:
                    return False
    # 4x4 격자에서 '#'의 개수가 4개여야 테트로미노
    if sum(row.count('#') for row in grid) != 4:
        return False

    # 원본 도형을 모든 회전 상태와 비교하여 동일한 도형인지 확인
    original = grid[:]
    for _ in range(3):
        original = rotate(original)
        if is_identical(grid, original):
            return True
    return False

if is_tetromino():
    print("YES")
else:
    print("NO")
