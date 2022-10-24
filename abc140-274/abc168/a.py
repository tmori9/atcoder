N = input()

target_n = int(N[-1])
if target_n == 2 or target_n == 4 or target_n == 5 or target_n == 7 or target_n == 9:
    print("hon")
elif target_n == 0 or target_n == 1 or target_n == 6 or target_n == 8:
    print("pon")
else:
    print("bon")
