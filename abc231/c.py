import bisect

n, q = map(int, input().split())
a_list = list(map(int, input().split()))

q_list = []
for i in range(q):
    input_q = int(input())
    q_list.append(input_q)

a_sorted = sorted(a_list)

for value in q_list:
    ans = bisect.bisect_left(a_sorted, value)
    print(len(a_sorted) - ans)
