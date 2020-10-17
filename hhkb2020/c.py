n = int(input())
p_list = list(map(int, input().split()))

temp_list = {-1}
result_num = 0

for i in p_list:
    temp_list.add(i)
    if result_num == i:
        while True:
            if result_num+1 in temp_list:
                result_num += 1
            else:
                result_num += 1
                break
    print(result_num)