x1, y1 = input()
x2, y2 = input()
if x1 == "#" and y1 == "#":
    print("Yes")
elif x1 == "#" and x2 == "#":
    print("Yes")
elif x2 == "#" and y2 == "#":
    print("Yes")
elif y1 == "#" and y2 == "#":
    print("Yes")
else:
    print("No")