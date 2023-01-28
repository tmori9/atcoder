n, m = map(int, input().split())
ab_list = [list(map(int, input().split())) for i in range(m)]

city_list = [set() for i in range(100005)]

for a, b in ab_list:
    city_list[a].add(b)
    city_list[b].add(a)


for i, route in enumerate(city_list):
    if i == 0:
        continue
    print(len(route), end="")
    if not len(route) == 0:
        print(" ", end="")
        print(*sorted(route))
    else:
        print("")
    if i == n:
        break
