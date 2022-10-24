a,b=map(float,input().split())
a_tax = a*100//8
b_tax = b*100//10
min_tax = 0

if a_tax <= b_tax:
    min_tax = int(a_tax)
else:
    min_tax = int(b_tax)

r_a_tax = int(min_tax*0.08)
r_b_tax = int(min_tax*0.1)

flag = True
while(flag):
    if r_a_tax == a and r_b_tax == b:
        flag = False
    elif r_a_tax > a or r_b_tax > b:
        print(-1)
        exit()
    else:
        min_tax += 1
        r_a_tax = int(min_tax*0.08)
        r_b_tax = int(min_tax*0.1)

print(min_tax)
