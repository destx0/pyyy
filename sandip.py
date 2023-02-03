table = [['a', 'b', 'c', 'd', ], [0, 1, 2, 3], [0, 5, 6, 7], [0, 9, 10, 11], [
    'e', 'b', 'c', 'h', ], [0, 1, 2, 3], [0, 4, 6, 7], [0, 9, 10, 11]]
prev = 0
mincolumn = 0
maxcolumn = 0
hasminmax = False
lastmax = 1
idx = 0
while (table[idx]):
    row = table[idx]
    if table[idx][0]:
        hasminmax = False
        prev = idx
        for j, item in enumerate(row):
            if item == 'b':
                mincolumn = j
                # print("mincolumn", mincolumn)
                hasminmax = True
            if item == 'c':
                maxcolumn = j
                # print("maxcolumn", maxcolumn)

    else:

        if not hasminmax:
            for jdx, item in enumerate(row):
                if item:

                    print(table[prev][jdx], item, end=' ')
                elif jdx == 0:
                    print()
                    print(table[prev][jdx], end=' ')
        else:
            for jdx, item in enumerate(row):
                if jdx == mincolumn:
                    continue
                if item:

                    print(table[prev][jdx], item, end=' ')
                elif jdx == 0:
                    print()
                    print(table[prev][jdx], end=' ')
            for jdx, item in enumerate(row):
                if jdx == maxcolumn:
                    continue
                if item:

                    print(table[prev][jdx], item, end=' ')
                elif jdx == 0:
                    print()
                    print(table[prev][jdx], end=' ')
    idx += 1

# # for idx in range(len(table)):
# #     row = table[idx] row = [0, 1, 2, 3]
# for idx, row in enumerate(table):
#     # print("row", row, "idx", idx)

#     if row[0]:
#         hasminmax = False
#         prev = idx
#         for j, item in enumerate(row):
#             if item == 'b':
#                 mincolumn = j
#                 hasminmax = True
#             if item == 'c':
#                 maxcolumn = j
#         # print()
#         # continue
#     else:
#         for jdx, item in enumerate(row):

#             if item:
#                 if hasminmax:

#                     if jdx == mincolumn and lastmax == 0:

#                         continue
#                     elif jdx == maxcolumn and lastmax == 1:

#                         continue
#                     if jdx == mincolumn or jdx == maxcolumn:
#                         lastmax = 1 - lastmax

#                     print(table[prev][jdx], item, end=' ')
#             elif jdx == 0:
#                 print()
#                 print(table[prev][jdx], end=' ')
# # 1. iterate all rows
# # if the first element is not null then its a header row and we store the index
# # else  its a data row
# #       if its in first column then print header first element
# #       else its a not null value then print header element and data element
# #       if item is null skip it
