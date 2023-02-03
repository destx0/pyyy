for _ in range(int(input())):
    n = int(input())
    str = input()
    ls, rs = [0] * 26, [0] * 26
    lc, rc = 0, 0
    res = 0
    for ch in str:
        rs[ord(ch) - ord('a')] += 1
    # print(rs)
    for num in rs:
        if num > 0:
            rc += 1
    # print("rc", rc)
    for ch in str:
        rs[ord(ch) - ord('a')] -= 1
        ls[ord(ch) - ord('a')] += 1
        if rs[ord(ch) - ord('a')] == 0:
            rc -= 1
        if ls[ord(ch) - ord('a')] == 1:
            lc += 1
        res = max(res, lc + rc)
    print(res)
