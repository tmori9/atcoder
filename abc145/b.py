N = int(input())
S = input()
N_half = N//2
if S == S[:N_half]+S[:N_half]:
    print("Yes")
else:
    print("No")
