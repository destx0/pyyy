import math


def helper(a, b):
    if a**b * b + b**a*a == num:
        return True


for _ in range(int(input())):
    num = int(input())
    f = 0
    t = math.ceil(num/2)


# for _ in range(int(input())):
#     f = 0
#     num = int(input())
#     t = num//2
    for i in range(1, t):
        for j in range(i, t):
            if helper(i, j):
                f = 1
                print(i, j)
                break
        else:
            continue
        if f:
            # print("break")
            break
    if not f:
        print(-1)
