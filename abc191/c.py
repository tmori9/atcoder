h, w = map(int, input().split())

s_list = []
for line in range(h):
    one_list = list(input())
    s_list.append(one_list)

result_sum = 0
first_flag = False
save_line = []
save_line_num = 0
save_fist_line_num = 0
for i, line in enumerate(s_list):
    if not('#' in line):  # すべて白
        continue
    if first_flag == False:
        past_pt = '.'
        for pt in line:
            if not(past_pt == pt) and pt == '#':
                result_sum += 1
            past_pt = pt
        first_flag = True  # 次から2回目
        save_fist_line_num = i
        save_line = s_list[i]
    else:  # 中間
        a_flag = False
        for j in range(len(s_list[0])):
            if a_flag == False and s_list[i-1][j] != s_list[i][j]:
                result_sum += 1
                a_flag = True
            else:
                a_flag = False
        save_line = s_list[i]
        save_line_num = i  # 行数
# 最終行
past_pt = '.'
for pt in save_line:
    if not(past_pt == pt) and pt == '#':
        result_sum += 1
    past_pt = pt


# 列にも適用
s_list = [list(x) for x in zip(*s_list)]

first_flag = False
save_line = []
save_line_num = 0
save_fist_line_num = 0
for i, line in enumerate(s_list):
    if not('#' in line):  # すべて白
        continue
    if first_flag == False:
        past_pt = '.'
        for pt in line:
            if not(past_pt == pt) and pt == '#':
                result_sum += 1
            past_pt = pt
        first_flag = True  # 次から2回目
        save_fist_line_num = i
        save_line = s_list[i]
    else:  # 中間
        a_flag = False
        for j in range(len(s_list[0])):
            if a_flag == False and s_list[i-1][j] != s_list[i][j]:
                result_sum += 1
                a_flag = True
            else:
                a_flag = False
        save_line = s_list[i]
        save_line_num = i  # 行数
# 最終行
past_pt = '.'
for pt in save_line:
    if not(past_pt == pt) and pt == '#':
        result_sum += 1
    past_pt = pt


print(result_sum)
