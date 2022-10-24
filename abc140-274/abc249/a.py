a, b, c, d, e, f, x = map(int, input().split())

takahashi_distance = x // (a + c)
takahashi_amari = x % (a + c)


if takahashi_amari >= a:
    takahashi_amari = 0
    takahashi_distance += 1

t_distance = (takahashi_distance * a + takahashi_amari) * b


aoki_distance = x // (d + f)
aoki_amari = x % (d + f)

if aoki_amari >= d:
    aoki_amari = 0
    aoki_distance += 1
a_distance = (aoki_distance * d + aoki_amari) * e


if t_distance < a_distance:
    print("Aoki")
elif t_distance == a_distance:
    print("Draw")
else:
    print("Takahashi")
