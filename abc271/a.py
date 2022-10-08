n = int(input())
res = hex(n)[2:].upper()

if len(res) == 0:
    print("00")
elif len(res) == 1:
    print(f"0{res}")
else:
    print(res)
