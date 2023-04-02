s_board = [list(input()) for i in range(8)]

# print(s_board)
for i in range(8):
    for j in range(8):
        if s_board[i][j] == "*":
            moji = chr(97 + j)  # chr(97) = a, chr(98) = b
            print(f"{str(moji)}{8-i}")
