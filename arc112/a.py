t = int(input())
case_list = [list(map(int, input().split())) for i in range(t)]

for l, r in case_list:
    output_num = 0
    for i in range(r, -1, -1):
        sum_num = i+1 - (l*2)
        if sum_num > 0:
            output_num += sum_num
        else:
            break
    print(output_num)
