from collections import deque


target = 7
blocks = 6
out = [[i] for i in range(1, target-blocks+2)]
# [[1],[2],[3],[4],[5],[6],[7]]
output = deque(out)
# print(output)

while len(output[0]) < blocks:
    curr = output.popleft()
    t = curr[:]
    if len(t) < blocks - 1:
        for i in range(1, target-sum(curr)+1):
            t.append(i)
# [1] -> [1,1]
            output.append(t)
            t = curr[:]
            # [1] -> [1,2]
    elif len(t) == blocks-1 and target-sum(t) > 0:
        t.append(target-sum(t))

        output.append(t)
        t = curr[:]
print(output)
# target 0
# [[1] , [2] , [3]]
# [[1,1],[1,2],[1,3] , [2,1],[2,2],[2,3] , [3,1],[3,2],[3,3]
#
