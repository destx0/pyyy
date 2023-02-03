for _ in range(int(input())):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))
    oc, ec = 0, 0
    for num in nums:
        if num % 2 == 0:
            ec += 1
        else:
            oc += 1

    if x % 2 == 0:
        print(ec) if oc else print(-1)
    else:
        print((ec+1)//2)
