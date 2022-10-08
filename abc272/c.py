n = int(input())
a_list = list(map(int, input().split()))

a_list_sorted = sorted(a_list, reverse=True)

# print(a_list_sorted)

gu_count = 0
gu_list = []

ki_count = 0
ki_list = []


for i in a_list_sorted:
    if i % 2 == 0:
        gu_count += 1
        gu_list.append(i)
    else:
        ki_count += 1
        ki_list.append(i)

    if 2 <= gu_count and 2 <= ki_count:
        print(max(gu_list[0] + gu_list[1], ki_list[0] + ki_list[1]))
        exit()
if 2 <= gu_count and ki_count < 2:
    print(gu_list[0] + gu_list[1])
elif gu_count < 2 and 2 <= ki_count:
    print(ki_list[0] + ki_list[1])
else:
    print(-1)
