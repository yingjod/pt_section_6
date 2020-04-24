def num_(score_lst, order_lst):
    """

    get students score from user

    """
    for i in range(3):
        print("the %s student : " % order_lst[i])
        score_lst.append([])
        for j in range(5):
            score_lst[i].append(eval(input()))


def print_(score_lst, order_lst):
    """
    
    print out all info

    """
    for i in range(3):
        print("student %d" % (i + 1))
        print("#sum %d" % (sum(score_lst[i])))
        print("#average %.2f" % (sum(score_lst[i]) / 5))


if __name__ == "__main__":
    score_lst = []
    order_lst = ["1st", "2nd", "3ed"]
    num_(score_lst, order_lst)
    print_(score_lst, order_lst)
