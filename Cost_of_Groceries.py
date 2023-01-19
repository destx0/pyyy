for _ in range(int(input())):
    n, f = map(int, input().split())
    fresh = list(map(int, input().split()))
    price = list(map(int, input().split()))
    res = 0
    for i, fr in enumerate(fresh):
        if fr >= f:
            res += price[i]
    print(res)
