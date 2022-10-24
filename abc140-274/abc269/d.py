N = int(input())
xy_set = set()
for _ in range(N):
    x, y = map(int, input().split())
    xy_set.add(x * 10000 + y)


def dfs(target_int, target_set):
    if target_int - 10001 in target_set:
        target_set.remove(target_int - 10001)
        dfs(target_int - 10001, target_set)
    elif target_int - 10000 in target_set:
        target_set.remove(target_int - 10000)
        dfs(target_int - 10000, target_set)
    elif target_int - 1 in target_set:
        target_set.remove(target_int - 1)
        dfs(target_int - 1, target_set)
    elif target_int + 1 in target_set:
        target_set.remove(target_int + 1)
        dfs(target_int + 1, target_set)
    elif target_int + 10000 in target_set:
        target_set.remove(target_int + 10000)
        dfs(target_int + 10000, target_set)
    elif target_int + 10001 in target_set:
        target_set.remove(target_int + 10001)
        dfs(target_int + 10001, target_set)
    return target_set


cnt = 0
while xy_set:
    cnt += 1
    root_target = xy_set.pop()
    xy_set = dfs(root_target, xy_set)

print(cnt)
