import string
import copy

n = int(input())

n_list = []

n -= 1
for i in range(11, -1, -1):
    proc_value = n // 26**i
    proc_value = proc_value % 26
    n_list.append(proc_value)

counter = len(n_list)
while counter >= 0:
    if n_list[0] == 0:
        n_list = n_list[1:]
    counter -= 1
    
print(n_list)