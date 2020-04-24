import random


def lotto():
    lottolst = []
    count = 0
    while count < 6:
        lottonum = random.randint(1, 49)
        if lottonum not in lottolst:
            lottolst.append(lottonum)
            count += 1
    lottolst.sort()
    print(lottolst)


def main():
    for i in range(1, 6):
        lotto()


main()
