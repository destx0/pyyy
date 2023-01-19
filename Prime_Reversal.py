from collections import Counter


for _ in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    if Counter(s1) == Counter(s2):
        print("YES")
    else:
        print("NO")
