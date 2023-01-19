import math


t = int(input())
while t:
    a, b = map(int, input().split())
    c = math.gcd(a, b)
    print(math.lcm(a, c) - math.gcd(b, c))
    t -= 1
