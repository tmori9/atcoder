# import copy

N, K = map(int, input().split())
S = input()

def calc(LR_str):
    re_sum = 0
    for i, s in enumerate(LR_str):
        if s == 'L' and not i==0:
            if LR_str[i-1] == 'L':
                re_sum += 1
        if s == 'R' and not i==N-1:
            if LR_str[i+1] == 'R':
                re_sum += 1
    return re_sum

result_list = []
str_list = []
str_list_copy = []
select_str = ""

def add_str(select_str):
    for start in range(N):
        end = N-1
        while start < end:
            S_copy = select_str # select str
            S_copy = list(S_copy)
            S_slice = S_copy[start:end+1]
            S_slice = S_slice[::-1]
            for ii, S_moji in enumerate(S_slice):
                if S_moji == 'L':
                    S_slice[ii] = 'R'
                else:
                    S_slice[ii] = 'L'
            S_copy[start:end+1] = S_slice
            S_copy = "".join(S_copy)
            str_list.append(S_copy)
            end -= 1

for i in range(K):
    if i ==0:
        select_str = S
        add_str(select_str)
    else:
        str_list_copy = str_list.copy()
        for single_str in str_list_copy:
            add_str(single_str)

for n in str_list:
    calc_int = calc(n)
    result_list.append(calc_int)

print(max(result_list))
