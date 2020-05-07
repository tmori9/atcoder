import copy

H, W = map(int,input().split())
root_list = []
for _ in range(H):
    root_list.append(list(str(input())))


change_list = copy.deepcopy(root_list)
DP_list = []

for i, line in enumerate(root_list):
    DP_line = []
    str_pt = root_list[i][0]
    if i == 0:
        DP_line.append(0) # 初期値
    else:
        if root_list[i-1][0] == line[0]: # 1文字目が上下一致
            DP_line.append(DP_list[i-1][0])
        else:
            DP_line.append(DP_list[i-1][0] + 1)

    for j, pt in enumerate(line[1:], 1): # 先頭は抜かす
        if i == 0: # 1行目
            if str_pt == pt: # 前の文字と一致
                DP_line.append(DP_line[j-1]) # 前の値を入れる
            else:
                DP_line.append(DP_line[j-1] + 1) # 違ったら1足す
                str_pt = pt
        else: # 2行目以降（上下左右比較）
            # 横比較
            if str_pt == pt:
                yoko_pt = DP_line[j-1]
            else:
                yoko_pt = DP_line[j-1] + 1
            
            # 縦比較
            if pt == root_list[i-1][j]:
                tate_pt = DP_list[i-1][j]
            else:
                tate_pt = DP_list[i-1][j] + 1
            
            DP_line.append(min(yoko_pt, tate_pt))
            str_pt = pt

    DP_list.append(DP_line)

result = DP_list[H-1][W-1] // 2

if root_list[0][0] == "#":
    result += 1
if root_list[H-1][W-1] == "#":
    result += 1
if  root_list[0][0] == "#" and root_list[H-1][W-1] == "#":
    if result == 2 or (H == 1 and W == 1):
        result = 1
    else:
        result -= 1

print(result)
