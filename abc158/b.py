N,B,R=map(int,input().split())
process_n = N//(B+R)
amari = N%(B+R)
result = process_n*B

if amari <= B:
    result += amari
else:
    result += B
print(result)