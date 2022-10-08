n, m = map(int, input().split())

move_next = []
for i in range(400):
    for j in range(400):
        # print(f"i={i}, j={j}, sum={i**2 + j**2}")
        check_one = [i**2 + j**2, i, j]
        if m == i**2 + j**2:
            move_next = [i, j]
            break
    if len(move_next) == 2:
        break

print(move_next)
move_all = []
move_all.append(move_next)

if not move_next[0] == move_next[1]:
    move_all.append([move_next[1], move_next[0]])


reachable = [[-1] * 400 for i in range(400)]  # TODO 400

print(reachable)

reachable[0][0] = 0
