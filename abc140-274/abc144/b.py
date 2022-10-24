N=int(input())
flag = False
for i in range(1,10):
    for j in range(1,10):
        if i*j == N:
            flag = True

print("Yes") if flag else print("No")