r, c = map(int, input().split())
board = [list(input()) for i in range(c)]
print(board)

for i in range(c):
    for j in range(r):
        for i_ in range(c):
            for j_ in range(r):
                if board[i_][j_].isdigit():
                    if abs(i_ - i) + abs(j_ - j) <= int(board[i_][j_]):
                        board[i][j] = "."
