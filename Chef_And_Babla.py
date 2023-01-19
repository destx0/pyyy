t = int(input())
while t:
    n = int(input())
    nums = list(map(lambda x: abs(int(x)),  input().split()))
    small = min(nums)
    if small == 1:
        small = 0
    print(small-1)
    t -= 1
