n, m, t = map(int, input().split())
a = list(map(int, input().split()))
x_list = [list(map(int, input().split())) for i in range(m)]


sort_x_list = sorted(x_list, reverse=False, key=lambda x: x[0])

bornus_index = 0
for i, value in enumerate(a):
    t -= value
    if t <= 0:
        print("No")
        exit()
    if bornus_index < len(sort_x_list):
        if i + 2 == sort_x_list[bornus_index][0]:
            t += sort_x_list[bornus_index][1]
            bornus_index += 1

print("Yes")
