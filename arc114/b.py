n = int(input())
f_list = list(map(int, input().split()))

all_set = []
for i, value in enumerate(f_list):
    init_set = set()
    init_set.add(i+1)
    while True:
        if f_list[i] in init_set:
            break
        else:
            init_set.add(f_list[i])
    all_set.append(list(init_set))

result = []
for line in all_set:
    if line not in result:
        result.append(line)

print(len(result))
