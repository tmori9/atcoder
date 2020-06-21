x, y = map(int, input().split())

tori = 2
kame = 4 # 全部
legs = 4*x
while True:
    if legs == y:
        print("Yes")
        exit()
    legs -= 2
    if legs < 2*x: # 全部鳥
        print("No")
        exit()

