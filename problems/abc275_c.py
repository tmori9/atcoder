s_list = []
pawn_list = []
for i in range(9):
    s = list(input())
    for j, value in enumerate(s):
        if value == "#":
            pawn_list.append([i, j])
    s_list.append(s)

# print(s_list)
# print(pawn_list)


count = 0
for first_pawn in pawn_list:
    for second_pawn in pawn_list:
        if first_pawn == second_pawn:
            continue
        x_move = second_pawn[0] - first_pawn[0]
        y_move = second_pawn[1] - first_pawn[1]
        third_pawn = [second_pawn[0] - y_move, second_pawn[1] + x_move]
        forth_pawn = [third_pawn[0] - x_move, third_pawn[1] - y_move]

        if third_pawn in pawn_list and forth_pawn in pawn_list:
            count += 1

print(count // 4)
