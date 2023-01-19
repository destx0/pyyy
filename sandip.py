table = [['a', 'b', 'c', 'd', ], [0, 1, 2, 3], [0, 5, 6, 7], [0, 9, 10, 11], [
    'e', 'f', 'g', 'h', ], [0, 1, 2, 3], [0, 0, 6, 7], [0, 9, 10, 11]]
prev = 0
# for idx in range(len(table)):
#     row = table[idx] row = [0, 1, 2, 3]
for idx, row in enumerate(table):
    # print("row", row, "idx", idx)
    if row[0]:
        prev = idx
        # print()
        # continue
    else:
        for jdx, item in enumerate(row):

            if item:

                print(table[prev][jdx], item, end=' ')
            elif jdx == 0:
                print()
                print(table[prev][jdx], end=' ')
# 1. iterate all rows
# if the first element is not null then its a header row and we store the index
# else  its a data row
#       if its in first column then print header first element
#       else its a not null value then print header element and data element
#       if item is null skip it
