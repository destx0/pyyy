t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    na = list(map(int, input().split()))
    ma = list(map(int, input().split()))
    final = 0

    def bsearch(idx):
        res = 0
        for ni in na:
            res += (ni//(idx+1))*ma[idx]
        return res

    l, r = 0, m-1
    while l <= r:
        mid = (l+r)//2
        if mid+1 <= r and bsearch(mid) >= bsearch(mid+1):
            final = max(final, bsearch(mid))
            r = mid-1
        else:
            final = max(final, bsearch(mid+1))
            l = mid+1
    print(final)
