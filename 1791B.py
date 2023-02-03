for _ in range(int(input())):
    n = int(input())
    st = input()
    x, y = 0, 0
    f = 1

    for char in st:
        if char == "U":
            x += 1
        elif char == "D":
            x -= 1
        elif char == "L":
            y -= 1
        else:
            y += 1
        if x == 1 and y == 1:
            print("YES")
            f = 0
            break
    # print(x, y)
    if f:
        print("NO")
