N = int(input())
Cook = list(map(int, input().split()))
Manzoku = list(map(int, input().split()))
addManzoku = list(map(int, input().split()))

result_sum = 0
past_c = 55

for i, c in enumerate(Cook):
    result_sum += Manzoku[c-1]

    if c - past_c == 1:
        result_sum += addManzoku[c-2]
    past_c = c

print(result_sum)