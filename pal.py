s = input()
count = [0]*26
res = ['_']*len(s)
for c in s:
    count[ord(c)-ord('A')] += 1
j, f = 0, 0
for i in range(26):
    if count[i] % 2 == 1:
        f += 1
if f > 1:
    print("NO SOLUTION")
else:
    for i, val in enumerate(count):
        if count[i] % 2 == 1:
            res[len(s)//2] = chr(i+ord('A'))
        while val > 1:
            res[j] = res[-j-1] = chr(i+ord('A'))
            j -= 1
            val -= 2
    print(res)
