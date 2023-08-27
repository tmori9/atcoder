n = int(input())
a_list = list(map(int, input().split()))
a_set = set(a_list)

for i in range(min(a_set), max(a_set)):
    if not i in a_set:
        print(i)
        exit()
