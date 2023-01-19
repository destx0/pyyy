from collections import Counter


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = dict(Counter(nums))
    cols = {}
    f = l = 0
    if sum(cnt.values()) != n:
        print(-1)
        continue
    for key in cnt:
        if not (cnt[key] and cnt[key] % key == 0):
            print(-1)
            f = 1
            break
    if f:
        continue

    for c in nums:
        if c not in cols:
            cols[c] = l+1
            l += 1

        cnt[c] -= 1
        print(cols[c], end=" ")
        if cnt[c] and (cnt[c] % c == 0):
            del cols[c]
    print()
