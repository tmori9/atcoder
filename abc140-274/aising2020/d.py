import copy
n = int(input())
x = list(input())

def count_ones_by_bin(num):
    bin_num = bin(num)[2:]
    count = 0
    for i in bin_num:
            count += int(i)
    return count

def waru(nn):
    one_count = count_ones_by_bin(nn)
    if nn % one_count == 0:
        return -1
    return nn % one_count

for i in range(1, n+1):
    x_copy = copy.copy(x)
    if x_copy[i-1] == '0':
        x_copy[i-1] = '1'
    else:
        x_copy[i-1] = '0'
    str_x = "".join(x_copy)
    num_x = int(str_x,2)

    if num_x == 0:
        print(0)
        break
    result_count = 0
    while True:
        if num_x == -1:
            break
        result_count += 1
        num_x = waru(num_x)
    print(result_count)