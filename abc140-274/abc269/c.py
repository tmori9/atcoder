N = int(input())

N_2 = list(format(N, "b"))


cut_list = []
count_list = []

first_flag = False
for i, v in enumerate(N_2[::-1]):
    if v == "1":
        if not first_flag:
            start = 0
            end = 2**i
            first_flag = True
            count_list.append(start)
            count_list.append(end)
        else:
            base_number = 2**i
            new_list = [n + base_number for n in count_list]
            count_list.extend(new_list)
    # print(f"{i}: {count_list}")
if len(count_list) == 0:
    print(0)
else:
    print(*count_list, sep="\n")
