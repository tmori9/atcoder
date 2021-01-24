n, x = map(int, input().split())
alco_list = [list(map(int, input().split())) for i in range(n)]

drinked = 0.0
for j, value in enumerate(alco_list):
    alco_value = value[0] * value[1] / 100.0
    drinked += alco_value
    drinked = round(drinked, 2)
    if x < drinked:
        print(j+1)
        exit()
print(-1)
