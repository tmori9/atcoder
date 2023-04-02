n, x = map(int, input().split())
a_list = set(map(int, input().split()))

for pt in a_list:
    if pt + x in a_list:
        print("Yes")
        exit()
print("No")
