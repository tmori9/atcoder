n = int(input())
x = [input() for i in range(n)]
d = dict()

for name in x:
    # 辞書にない場合
    if not name in d:
        d[name] = 0
        print(name)
    else:
        d[name] += 1
        print("{}({})".format(name, d[name]))
