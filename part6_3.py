def creat(lst):
    """
    
    get a new list

    """
    for i in range(10):
        lst.append(eval(input()))


if __name__ == "__main__":
    lst = []
    creat(lst)
    lst.sort()
    print(lst[-1], lst[-2], lst[-3])
