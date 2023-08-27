N, H, X = map(int, input().split())
p_list = list(map(int, input().split()))

for i, p in enumerate(p_list):
    if H + p >= X:
        print(i + 1)
        exit()
