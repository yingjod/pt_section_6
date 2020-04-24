# import random
#
# lotto=[]
#
# for i in range (1,7):
#     randnum = random.randint(1,49)
#     lotto.append(randnum)
#
# print('the lottery numbers are :')
# for i in lotto:
#     print('%4d'%i,end='  ')


# import random
#
# lotto=[]
# checknum=[]
#
# for i in range(0,50):
#     checknum.append(0)
#
# count=1
# while count <= 6:
#     randnum = random.randint(1,49)
#     if checknum[randnum] == 0
#         lotto.append(randnum)
#         count+=1
#     checknum[randnum] = 1
#
# print('the lottery numbers are : \n',end = '' )
# for i in lotto:
#     print(i , end = ' ')
# print()

# import random
# lotto=[]
# n=1
# while n <= 6 :
#     randnum = random.randint(1,49)
#     if randnum not in lotto:
#         lotto.append(randnum)
#         n += 1
#
# print('the lottery numbers are : \n',end=' ')
# for i in lotto:
#     print('%4d'%i,end=' ')
# print()
#
# lotto.sort()
# print('after sorting : ')
# for i in lotto :
#     print('%4d '% i ,end= ' ')
# print()

# lst2=[[1,2,3],[4,5,6]]
# print(lst2)
# print(lst2[0])
# print(len(lst2))
# print(len(lst2[0]))

import random
rows = eval (input('enter the number of row : '))
columns=eval(input('enter the number od columns : '))

lst2=[]
for i in range (rows):
    lst2.append([])
    for j in range(columns):
        lst2[i].append(random.randint(1,50))

print(lst2)

print()
for i in range (len(lst2)):
    for j in range (len(lst2[0])):
        print('lst2[%d][%d] = %5d'%(i , j , lst2[i][j]))
    print()


for row in lst2:
    for value in row:
        print('%5d'%(value),end='')
    print()

for i in range(len(lst2)):
    for j in range (len(lst2[0])):
        print('%5d'%(lst2[i][j]),end = '')
    print()