from collections import Counter


t = int(input())
while t:
    t -= 1
    n = int(input())
    nums = list(map(int, input().split()))
    cn = Counter(nums)
    print("NO" if cn[0] % 2 else "YES")
