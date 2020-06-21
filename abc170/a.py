x = list(map(int, input().split()))

for i,value in enumerate(x):
    if value == 0:
        print(i+1)
        exit()