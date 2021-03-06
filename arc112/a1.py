t = int(input())
case_list = [list(map(int, input().split())) for i in range(t)]

for l, r in case_list:
    output_num = 0
    sum_num = r+1 - (l*2)
    if sum_num <= 0:
        print(0)
    else:
        print(int(sum_num*(sum_num+1)/2))
