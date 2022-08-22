n, p, q, r = map(int, input().split())
a_list = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    a_list[i] += a_list[i - 1]

a_set = set(a_list)

for a in a_list:
    if a + p in a_set and a + p + q in a_set and a + p + q + r in a_set:
        print("Yes")
        exit()
print("No")
