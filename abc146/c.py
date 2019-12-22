A,B,X=map(int,input().split())

if X < A + B :
    print("0")
    exit()

result = 0
keta = 10
flag = 0
while True:
    result = (X - (keta*B)) // A
    price = A*result + B*len(str(result))
    if result >= 1000000000:
        print('1000000000')
        exit()
    if len(str(result)) < keta or result <0:
        keta -= 1
    else:
        while True:
            price = A*result + B*len(str(result))
            if price > X:
                result -= 1
            else:
                print(result)
                exit()
