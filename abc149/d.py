n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = list(input())

r_point = t.count('s') * r
s_point = t.count('p') * s
p_point = t.count('r') * p

sum_point = r_point+s_point+p_point

for i, moji in enumerate(t):
    if i+k >= len(t):
        break
    if t[i] == 'r' and t[i+k] == 'r':
        sum_point -= p
        t[i+k] = 'x'
    if t[i] == 's' and t[i+k] == 's':
        sum_point -= r
        t[i+k] = 'x'
    if t[i] == 'p' and t[i+k] == 'p':
        sum_point -= s
        t[i+k] = 'x'

print(sum_point)
