S = list(input())
K = int(input())

x_count = 0
p_count = 0
odd_flag = False

count_list = []
for i in S:
    if i == "X":
        x_count += 1
        if p_count <= -1:
            count_list.append(p_count)
            p_count = 0
    else:
        p_count -= 1
        if x_count >= 1:
            count_list.append(x_count)
            x_count = 0
count_list.append(x_count + p_count)

print(count_list)
"""
cost_list = []  # マイナスを集める
if count_list[0] >= 0:
    cost_list = count_list[1::2]
else:
    cost_list = count_list[0::2]

range_list = []
weight = 0
print(cost_list)

for i, value in enumerate(cost_list):
    weight -= value  # 足す
"""