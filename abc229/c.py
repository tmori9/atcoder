N, weight = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(N)]
cheese.sort(key=lambda x: x[0], reverse=True)

result_num = 0
for value, w in cheese:
    weight -= w
    result_num += w * value
    if weight <= 0:
        result_num -= abs(weight) * value
        break
print(result_num)
