n, m = map(int, input().split())
a_list = [int(i) for i in input().split()]

sort_a_list = sorted(a_list)[::-1]

for i, num in enumerate(range(m)):
    if sort_a_list[i] < sum(sort_a_list)/(4*m):
        print("No")
        exit()

print("Yes")
