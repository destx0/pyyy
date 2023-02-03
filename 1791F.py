for _ in range(int(input())):
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))
    res = ""
    for _ in range(t):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            for i in range(inp[1]-1, inp[2]):
                if (nums[i]) > 9:
                    tmp = 0
                    # print("ni", nums[i])
                    while nums[i] > 0:
                        tmp += nums[i] % 10
                        nums[i] //= 10
                    nums[i] = tmp
                    # print("n", nums[i])
        else:
            res += str(nums[inp[1]-1]) + "\n"
    print(res, end="")
