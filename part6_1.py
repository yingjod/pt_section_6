def enter(size, sum_of_even_index, count, alist):
    """
    sum of the all the even
    """
    for i in range(size):
        alist.append(eval(input()))

    for i in range(size):
        count += 1
        print(" %3d" % alist[i], end=" \n " if count % 3 == 0 else " ")

        if i % 2 == 0:
            sum_of_even_index += alist[i]

    print(sum_of_even_index)


if __name__ == "__main__":

    size = 12
    sum_of_even_index = 0
    count = 0
    alist = []
    enter(size, sum_of_even_index, count, alist)
