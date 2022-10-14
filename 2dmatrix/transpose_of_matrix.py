def matrix(n):
    ob = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        ob.append(row)
    # transpose
    for i, val in enumerate(ob):

        # if 'i' dont use here  then we don't get the transpose of
        # matrix we repeat again it self so we have to take
        # upper triangle to swap the value
        for j in range(i, len(ob[0])):
            # here we get the swap row with column to get transepose
            val[j], ob[j][i] = ob[j][i], val[j]

    print("\n".join(map(str, ob)))


n = int(input())
matrix(n)


# skipcq
"""
input

11	12	13	14

21	22	23	24

31	32	33	34

41	42	43	44


output


[11, 21, 31, 41]
[12, 22, 32, 42]
[13, 23, 33, 43]
[14, 24, 34, 44]
"""
