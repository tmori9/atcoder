h, w = map(int, input().split())
s_list = [[str(j) for j in input()] for i in range(h)]

result_num = 0

left_target = False
# i = 列, j = 幅
for i, h_list in enumerate(s_list):
    left_target = False
    for j, mark in enumerate(h_list):
        if mark == ".":
            if left_target == True:
                result_num += 1
            left_target = True
        else:
            left_target = False

left_target = False

s_list = list(zip(*s_list))
for i, h_list in enumerate(s_list):
    left_target = False
    for j, mark in enumerate(h_list):
        if mark == ".":
            if left_target == True:
                result_num += 1
            left_target = True
        else:
            left_target = False
        
print(result_num)
