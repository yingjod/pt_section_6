def count_():

    """
    
    to print out the number showed most time in list and how many time.

    """
    size = 10
    sample = []
    count = [0] * size

    for i in range(size):
        num = int(input())

        sample.append(num)
        count[sample.index(num)] += 1
    num_occu = max(count)

    print(sample[count.index(num_occu)])
    print(num_occu)


if __name__ == "__main__":
    count_()
