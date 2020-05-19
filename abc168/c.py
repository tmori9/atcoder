import math
A, B, H, M = map(int, input().split())

tyousin = M*6
tansin = H*30 + M*0.5

kakudosa = abs(tyousin - tansin)
if kakudosa >= 180:
    kakudosa = 360 - kakudosa

result_root = A**2 + B**2 - 2*A*B*math.cos(math.radians(kakudosa))

print(math.sqrt(result_root))