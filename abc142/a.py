N = int(input())
count = 0
for i in range(N+1):
    if i % 2 == 1:
        count += 1

print(count/N)