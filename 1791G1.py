for _ in range(int(input())):
    n, budget = map(int, input().split())
    nums = list(map(int, input().split()))
    print(nums)
    for i in range(len(nums)):
        nums[i] += i+1
    print(nums)
    snum = sorted(nums)
    print(snum)
    cnt = 0
    for num in snum:
        budget -= num
        if budget < 0:
            break
        cnt += 1
    print(cnt)
