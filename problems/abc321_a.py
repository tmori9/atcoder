n = int(input())
# print(n)

# nを1文字ずつ分割してリストに格納する
n_list = list(str(n))

n_max = 199999
for i in n_list:
    i = int(i)
    if n_max <= i:
        print("No")
        exit()
    else:
        n_max = i

print("Yes")
