from statistics import mean

n = int(input())
x_point = list(map(int, input().split()))

x_point = sorted(x_point)

accurary_point = x_point[n:-n]
print(mean(accurary_point))
