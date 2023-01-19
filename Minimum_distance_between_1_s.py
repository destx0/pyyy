for _ in range(int(input())):
    n = int(input())
    str = list(input())
    l = -1
    dis = set()
    dis.add(2)
    d = 2
    for i,c in enumerate(str):
        if c== '1' and l == -1:
            l = i
        elif c== '1':
            d = 2 - (i-l)%2
            dis.add(d)
        if d == 1:
            break

    print((min(dis)))

    