n = int(input())
a_list = list(map(int, input().split()))

pt = 0
jiko = 0

for i in range(n):
    print(i)
    value = a_list[i]  # 5

    if a_list[value - 1] == value:
        jiko += 1
        continue
    if a_list[value - 1] == i + 1:
        # print(f"i = {i}, value= {value}")
        # print(f"a_list[value - 1] = {a_list[value - 1]}")
        if i < value:
            pt += 1

pt += (jiko * (jiko - 1)) // 2
print(pt)
