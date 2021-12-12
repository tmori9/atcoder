import collections

n = int(input())

n_list = []
for i in range(n):
    x = input()
    n_list.append(x)


c = collections.Counter(n_list)
a = c.most_common()[0]
print(a[0])