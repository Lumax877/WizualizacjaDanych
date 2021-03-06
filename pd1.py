# zad 1
# a = str("Hello World")
#
# b = 37
# c = 40.2
# d = 2 + 3j
#
# e = list(("tytus", "romek", "atomek"))
# f = tuple(("maslo", "majonez", "cukier"))
# g = range(7)
#
# h = dict(name="John", age=36)
#
# i = set(("apple", "banana", "cherry"))
# j = frozenset(("apple", "banana", "cherry"))
#
# k = bool(5)
#
# l = bytes(5)
# m = bytearray(5)
# n = memoryview(bytes(5))
#
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# print(c)
# print(type(c))
# print(d)
# print(type(d))
# print(e)
# print(type(e))
# print(f)
# print(type(f))
# print(g)
# print(type(g))
# print(h)
# print(type(h))
# print(i)
# print(type(i))
# print(j)
# print(type(j))
# print(k)
# print(type(k))
# print(l)
# print(type(l))
# print(m)
# print(type(m))
# print(n)
# print(type(n))

# zad 2

# def dod(x, y):
#     return x + y
#
# def odej(x, y):
#     return x - y
#
# def mnoz(x, y):
#     return x * y
#
# def dziel(x, y):
#     return x / y
#
# print("Wybierz operacje:")
# print("1.dodawanie")
# print("2.odejmowanie")
# print("3.mnozenie")
# print("4.dzielenie")
#
# while True:
#
#     choice = input("Wybierz(1/2/3/4): ")
#
#
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Pierwsza liczba: "))
#         num2 = float(input("Druga liczba: "))
#
#         if choice == '1':
#             print(num1, "+", num2, "=", dod(num1, num2))
#
#         elif choice == '2':
#             print(num1, "-", num2, "=", odej(num1, num2))
#
#         elif choice == '3':
#             print(num1, "*", num2, "=", mnoz(num1, num2))
#
#         elif choice == '4':
#             print(num1, "/", num2, "=", dziel(num1, num2))
#         break
#     else:
#         print("co")

# zad 3

# a = 3
# a += 1
# print (a)
# a -= 2
# print(a)
# a /= 2
# print (a)
# a *= 42
# print(a)
# a %= 7
# print(a)

# zad 4

# a = exp(10)
# print(a)

# b = (log(5 + (sin(8) ** 2)) ** 1/6)
# print(b)


# c = floor(3.55)
# d = ceil(4.80)
# print(c)
# print(d)

# zad 5

# imie = "BARTOSZ"
# nazwisko = "OCHTABINSKI"
# a = imie.capitalize()
# b = nazwisko.capitalize()
# print(a + " " + b)

# zad 6

# piosenka = "la la la kaczynski la la la morawiecki la la la"
# a = piosenka.count("la")
# print(a)

# zad 7

# imie = "bartosz"
#
# tak = (imie[0], imie[-1])
# print(tak)

# zad 8

# txt = "piec plus dwa to siedem"
#
# a = txt.split()
#
# print(a)

# zad 9

# a = "mleko"
# b = 4.27
# c = 45
# d = hex(c)
# print(a)
# print(b)
# print(d)