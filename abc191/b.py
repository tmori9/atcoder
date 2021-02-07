n, x = map(int, input().split())
A_list = list(map(int, input().split()))

result_list = [n for n in A_list if n != x]
if result_list == []:
    print()
else:
    L = [str(a) for a in result_list]
    L = " ".join(L)
    print(L)
