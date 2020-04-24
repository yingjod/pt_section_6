def compute(lst, a=3):
    lst.sort()
    ans = []
    for i in range(-1, -1 * a - 1, -1):
        ans.append(lst[i])
    return ans


def main():
    lst = []
    for i in range(10):
        num = eval(input())
        lst.append(num)
    print(lst)
    print(compute(lst))


main()
