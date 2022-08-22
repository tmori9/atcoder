x, y, n = map(int, input().split())

x_n = n
y_n = 0
result_sum = 999999999999

while True:
    calc_sum = x * x_n + y * y_n
    result_sum = min(result_sum, calc_sum)

    x_n -= 3
    y_n += 1
    if x_n < 0:
        break

print(result_sum)
