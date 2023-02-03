from collections import Counter


for _ in range(int(input())):
    n = int(input())
    nums = input()
    # nums.append(0)
    # nums.append(1)
    # print("nums", nums)
    cnt = Counter(nums)
    # print("cnt0",  cnt['0'])
    # print("cnt1", cnt['1'])
    if cnt['0'] >= cnt['1']:
        print(cnt['1'])
    else:
        print(cnt['0']+1)
