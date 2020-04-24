def compute(alist):
    for i in range(len(alist)):
        alist[i] = eval(input())
    return alist


def max(alist):
    max_num = alist[0]
    for i in range(len(alist)):
        if alist[i] > max_num:
            max_num = alist[i]
    return max_num


def min(alist):
    min_num = alist[0]
    for i in range(len(alist)):
        if alist[i] < min_num:
            min_num = alist[i]
    return min_num


def main():
    lst = [0] * 5
    print(compute(lst))
    print("max=", max(lst))
    print("min=", min(lst))


main()
