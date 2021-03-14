import random
# zad 1
# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# A = []
# for i in liczby:
#     A.append(1 - i)
# print(A)
#
# B = []
# for a in range(8):
#     B.append(4**a)
# print(B)
#
# C = []
# for m in range(8):
#     if m % 2 == 0:
#         C.append(4**m)
# print(C)

# zad 2

# lista1 = [random.randint(1, 27) for x in range(10)]
# lista2 = [x for x in lista1 if x % 2 == 0]
# print(lista1)
# print(lista2)

# zad 3

# towary = {'bułki' : 'sztuk', 'mleko' : 'l', 'mąka' : 'kg'}
# ilosc = {}
# for key, a in towary.items():
#     if a == 'sztuk':
#         ilosc[a] = key
# print(ilosc)

# zad 4

# def pitagoras(a, b, c):
#     if a > b and a > c:
#         if a ** 2 == b ** 2 + c ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif b > a and b > c:
#         if b ** 2 == a ** 2 + c ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'
#     elif c > a and c > b:
#         if c ** 2 == a ** 2 + b ** 2:
#             return 'Trójkąt jest prostokątny'
#         else:
#             return 'Trójkąt nie jest prostokątny'

# zad 5

# def poletrapezu(a = 1, b = 2, h = 3):
#     return ((a + b) * h / 2)

# zad 6

# def ciong(a = 1, b = 4, ile = 10):
#     print(a)
#     for x in range(a, ile):
#         print(x * b)
# ciong()

# zad 7

# def cionk(*liczby):
#     if len(liczby) != 3:
#         print('Podaj trzy liczby!')
#         return -1
#     print(liczby[0])
#     for x in range(liczby[0], liczby[2]):
#         print(x * liczby[1])
#
# cionk(1, 2, 3)

# zad 8
# def licz(**a):
#     return len(a.items()), sum(x for x in a.values())


