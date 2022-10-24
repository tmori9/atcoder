n = int(input())

n_list = [0]*50000
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x+y+z >= 150:
                break
            index = x*x + y*y + z*z + x*y + y*z + z*x
            n_list[index] = n_list[index]+1

for i in range(1,n+1):
    print(n_list[i])