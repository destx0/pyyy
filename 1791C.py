for _ in range(int(input())):
    n = int(input())
    st = input()
    l, r = 0, len(st) - 1
    while l < r:
        if st[l] != st[r]:
            l += 1
            r -= 1
        else:
            break
    print(r-l+1)
