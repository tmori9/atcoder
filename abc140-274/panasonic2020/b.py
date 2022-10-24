H,W=map(int,input().split())
if H == 1 or W == 1:
    print(1)
    exit()
one_line = (H+1)//2
two_line = H//2
print((W//2)*(one_line+two_line) + W%2 * one_line)
