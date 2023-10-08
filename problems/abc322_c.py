n, m = map(int, input().split())
x_list = list(map(int, input().split()))

for i, x in enumerate(x_list):
    if i == 0:
        res = list(range(x))
        print(*res[::-1], sep="\n")
    else:
        res = list(range(x - x_list[i - 1]))
        print(*res[::-1], sep="\n")
