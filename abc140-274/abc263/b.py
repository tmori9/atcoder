n = int(input())
p_list = list(map(int, input().split()))

parent = p_list[-1]
result = 0
while True:
    result += 1
    parent_pt = parent
    if parent == 1:
        print(result)
        exit()
    parent = p_list[parent_pt - 2]
