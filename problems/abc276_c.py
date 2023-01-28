n = int(input())
target = list(map(int, input().split()))

target = target[::-1]
pre_t = 20
for i, t in enumerate(target):
    if t < pre_t:
        pass
    else:
        mae_list = target[::-1][: len(target) - i - 1]
        ato_list = target[::-1][len(target) - i :]
        pop_i = -1
        for search_a in sorted(ato_list, reverse=True):
            if search_a < t:
                pop_idx = ato_list.index(search_a)
                pop_i = ato_list.pop(pop_idx)
                ato_list.append(t)
                break
        break

    pre_t = t

if mae_list:
    print(*mae_list, end=" ")
print(pop_i, end=" ")
if ato_list:
    print(*sorted(ato_list, reverse=True))
