n = int(input())
keta_num = len(str(n))
result_str = '0'

if not keta_num % 2 == 0:  # 奇数
    for i in range(keta_num // 2):
        result_str += '9'
    print(int(result_str))
    exit()
else:  # 偶数
    for i in range(keta_num // 2 - 1):
        result_str += '9'
    str2int = int(result_str)
    n_int = str(n)
    temp_num = keta_num // 2
    check_num_mae = n_int[:temp_num]
    check_num_ato = n_int[temp_num:]

    if check_num_ato[0] == '0' and keta_num == 2:
        count_num = int(check_num_mae) - ((temp_num-1)*10)
        if check_num_ato[0] == '0':
            count_num -= 1
        print(count_num)
    else:
        if int(check_num_mae) <= int(check_num_ato):  # 前と同じかそれ以上
            count_num = int(check_num_mae) - (10**(temp_num-1)) + 1
        else:
            count_num = int(check_num_mae) - (10**(temp_num-1))
        print(str2int+count_num)
