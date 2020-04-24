def compute(lst):
    """

    print it

    """
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print("%4d" % lst[i][j], end=" ")
            print()


def list_(row, column, lst):
    """

    to make  the list

    """
    for i in range(row):
        lst.append([])
        for j in range(column):
            lst[i].append(j - i)

    compute(lst)


if __name__ == "__main__":
    row = eval(input())
    column = eval(input())
    lst = []
    list_(row, column, lst)
