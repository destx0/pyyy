for _ in range(int(input())):
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))
    nl, nv = -1, int(1e9)
    for i, num in enumerate(nums):

        if (nums[i] + i+1) < nv + min(nl+1, n-nl):
            nl = i
            nv = nums[i]
        nums[i] += min(i+1, n-i)
    nums[nl] = int(1e9)
    print(nums)
    snum = sorted(nums)
    print(snum)
    nv += nl+1
    if t < nv:
        print(0)
        continue
    t -= nv
    cnt = 1
    for num in snum:
        t -= num
        if t < 0:
            break
        cnt += 1
    print(cnt)
