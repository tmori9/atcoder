X, K, D = map(int, input().split())

hu = False
if X < 0:
    X = abs(X)

idou_kaisu = X//D # 移動回数
amari = X%D # あまり

if idou_kaisu >= K: # すべて一方方向
    print(X - (K*D))
    exit()
else:
    X = amari
    K = K - idou_kaisu

three_list = []

for i in range(K):
    three_list.append(X)
    
    if len(three_list) >= 4:
        three_list.pop(0)
    if len(three_list) >= 3:
        if three_list[0] == three_list[2]: # 繰り返し
            if (K-i) % 2 == 0: # 偶数
                print(abs(three_list[0]))
            else:
                print(abs(three_list[1]))
            exit()
    if X >= 0:
        X -= D
    else:
        X +=D
print(abs(X))
    