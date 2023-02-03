for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == min(a, b, c):
        print("ALICE")
    elif b == min(a, b, c):
        print("BOB")
    else:
        print("CHARLIE")
