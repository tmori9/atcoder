t = int(input())

x_list = [list(map(int, input().split())) for i in range(t)]

for i in x_list:
    red_num = (i[0] - i[1] + 1)**2
    blue_num = (i[0] - i[2] + 1)**2
    