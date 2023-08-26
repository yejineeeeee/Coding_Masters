def min_moves_to_reach(dest, start):
    moves = 0
    
    while start != dest:
        if start < dest:
            start += 3
        else:
            start -= 1
        moves += 1
    
    return moves

N, J = map(int, input().split())

moves = min_moves_to_reach(J, N)
print(moves)