import copy
N, M, B =map(int,input().split())
g_y, g_x =map(int,input().split()) # ゴールの座標

robot_list = []
for i in range(M):
    ry, rx, c = input().split()
    one_line = [int(ry), int(rx) ,c]
    robot_list.append(one_line)

same_row = [] # ゴールの縦軸と同じブロックのリスト
same_line = [] # ゴールの横軸と同じブロックのリスト

block_list = []
for i in range(B):
    by, bx = map(int,input().split())
    one_line = [by, bx]

    if g_x == bx:
        same_row.append(one_line)
    if g_y == by:
        same_line.append(one_line)

    block_list.append(one_line)
# print(same_row) # 後で消す
# print(same_line) # 後で消す

result_list = []


# 縦軸の計算
ij = 0
while(True):
    if [g_y + ij, g_x] in same_row: # ブロックがある
        # print("ue")
        # print(g_y + ij, g_x)
        break
    else:
        if ij != 0:
            result_list.append([g_y+ij, g_x, "D"])
    ij -= 1
    # 最下層の判定
    if g_y + ij == -1:
        ij = N - g_y -1

ij = 0
while(True):
    if [g_y + ij, g_x] in same_row:
        # print("sita")
        # print(g_y + ij, g_x)
        # if ij != 1:
        #     result_list.append([g_y + ij-1, g_x, "U"]) # ブロックの上に置く # TODO ブロックが一番上の場合、矢印は一番下
        break
    else:
        if ij != 0:
            result_list.append([g_y+ij, g_x, "U"])
    ij += 1
    # 最下層の判定
    if g_y + ij == 40:
        ij = - g_x

# 横軸の判定
available_line = [] # 設置した横列のリスト

ij = 0
while(True):
    if [g_y, g_x + ij] in same_line:
        # print("hidari")
        # print(g_y, g_x + ij)
        # if ij != 1:
        #     result_list.append([g_y, g_x + ij +1, "R"]) # TODO
        break
    else:
        if ij != 0:
            result_list.append([g_y, g_x + ij, "R"])
            available_line.append(g_x + ij)
    ij -= 1
    # 最左端の判定
    if g_x + ij == -1:
        ij = N - g_x -1

ij = 0
while(True):
    if [g_y, g_x + ij] in same_line:
        # print("migi")
        # print(g_y, g_x + ij)
        # if ij != 1:
        #     result_list.append([g_y, g_x + ij -1, "L"]) # TODO
        break
    else:
        if ij != 0:
            result_list.append([g_y, g_x + ij, "L"])
            available_line.append(g_x + ij)
    ij += 1
    # print(ij)
    # print(g_x + ij -1)
    # 最右端の判定
    if g_x + ij == 40:
        ij = -g_x

# available_line の上に↓を作成
ij = -1
while len(available_line) != 0:
    for avai_x in available_line:
        if [g_y+ij, avai_x] in block_list:
            available_line.remove(avai_x)
            continue
        if [g_y+ij, avai_x] in result_list:
            available_line.remove(avai_x)
            continue
        result_list.append([g_y+ij, avai_x, "D"])
    ij -= 1
    # 最下層の判定
    if g_y + ij == 40:
        ij = -g_x

# print("av: ", available_line)
print(len(result_list))
for line in result_list:
    print(line[0], line[1], line[2])
