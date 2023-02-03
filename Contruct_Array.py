arr = [1, 3, 5, 7]
cnt = 1
res = []
for num in arr:
    tmp = []
    for i in range(num):
        tmp.append(cnt)
        cnt += 1
    res.append(tmp)
print(res)
str = input()
