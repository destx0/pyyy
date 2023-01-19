for _ in range(int(input())):
    s = input()
    l, r = 1, 1
    if s[:l] <= s[l:r] and s[l:r] <= s[:r]:
        print(s[:l], s[l:r], s[:r])
