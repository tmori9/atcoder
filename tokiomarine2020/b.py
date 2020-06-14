A, V = map(int, input().split()) # 鬼
B, W = map(int, input().split())
T = int(input())

if A <= B: # 鬼が左側
    A += V*T
    B += W*T
    if A >= B:
        print("YES")
    else:
        print("NO")
else:
    A -= V*T
    B -= W*T
    if A <= B:
        print("YES")
    else:
        print("NO")
