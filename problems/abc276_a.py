s = input()

s = s[::-1]

idx = s.find("a")

if idx == -1:
    print(-1)
else:
    print(len(s) - idx)
