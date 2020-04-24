import random

randlist = []
count = 1
while count <= 100:
    randnum = random.randint(1, 1000)
    if randnum not in randlist:
        randlist.append(randnum)
        count += 1

randlist.sort()
for j in range(1, 101):
    if j % 10 == 0:
        print("%4d" % (randlist[j - 1]))
    else:
        print("%4d" % (randlist[j - 1]), end="")

print()
print(randlist[1])
print(randlist[len(randlist) - 2])
