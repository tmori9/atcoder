N, K = map(int, input().split())

over_n = N - (N//K) * K
under_n = abs(over_n-K)
print(min(over_n, under_n))
