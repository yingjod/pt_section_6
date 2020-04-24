import random

randlist = []
for i in range(100):
    randnum = random.randint(1, 1000)
    randlist.append(randnum)

randlist.sort()
for j in range(1, 101):
    if j % 10 == 0:
        print("%4d" % (randlist[j - 1]))
    else:
        print("%4d" % (randlist[j - 1]), end="")

print()
print(randlist[1])
print(randlist[-2])
