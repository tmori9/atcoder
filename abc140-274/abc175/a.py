x = input()

if x == "RRR":
    print(3)
elif x == "RRS" or x == "SRR":
    print(2)
elif x == "RSR" or x == "RSS" or x== "SSR" or x=="SRS":
    print(1)
else:
    print(0)