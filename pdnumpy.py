import numpy as np

# zad 1

# a = np.arange(3,48,3)
# print(a)

# zad 2

# a = np.arange(4,20)
# b = a.astype('float')
# print(b)
# c = a.astype('int')
# print(c)

# zad 3

# def funkcja(n):
#     a = np.arange(1,n*n+1)
#     b = a.reshape(n,n)
#     print(b)
#
# funkcja(5)

# zad 4

# def ciaggeo(n, an):
#     a = np.logspace(1, an, num=an,endpoint=True,base=n,dtype="int64")
#     print(a)
#
# ciaggeo(3,4)

# zad 5

# def co(n):
#     xd = np.diag([a for a in range(n, 0, -1)])
#     print(xd)
#
# co(3)

# zad 7

# def uhuhu(n):
#     tak = np.zeros((n,n), dtype='int')
#     for a in range(n):
#          for b in range(n):
#              for c in range(n):
#                 if (a == b-c or a == b+c):
#                  tak[a,b] = 2 * (c+1)
#
#     print(tak)
#
# uhuhu(4)

# zad 9

# fibo = [1,1]
# for x in range(23):
#     fibo.append(fibo[x] + fibo[x+1])
# a = np.array(list(fibo))
# b = a.reshape(5,5)
# print(b)

