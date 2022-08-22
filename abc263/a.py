a, b, c, d, e = map(int, input().split())

card_list = [a, b, c, d, e]
sort_list = sorted(card_list)

if (sort_list[0] == sort_list[1] and sort_list[1] == sort_list[2]) and (
    sort_list[3] == sort_list[4]
):
    print("Yes")
    exit()

if (sort_list[0] == sort_list[1]) and (
    sort_list[2] == sort_list[3] and sort_list[3] == sort_list[4]
):
    print("Yes")
    exit()

print("No")
