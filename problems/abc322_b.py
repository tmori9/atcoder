n, m = map(int, input().split())
s = list(input())
t = list(input())

# print(s)
s_len = len(s)
# print(t[:s_len])

settou = False
setubi = False

if s == t[:s_len]:
    settou = True
if s == t[-s_len:]:
    setubi = True

if settou and setubi:
    print(0)
elif settou and not (setubi):
    print(1)
elif not (settou) and setubi:
    print(2)
else:
    print(3)
