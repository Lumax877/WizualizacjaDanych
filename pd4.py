# zad 1
# rand = [a for a in range(0,33) if a % 4 == 0]
# a = open('zad1.txt', 'w')
# for e in rand:
#     a.write(str(e) + ' ')
# a.close()

# zad 2
# with open('zad1.txt', 'r') as a:
#     l = a.readlines()
#     l = [e[:-1] for e in l]
#     print(l)

# zad 3
# with open('zad3.txt', 'a') as a:
#     for e in 'linijka':
#         a.write(e + '\n')
#
# with open('zad3.txt', 'r') as b:
#    for e in b:
#          print(e[:-1])

# zad 4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         return ("Produkt to {}".format(self.nazwa_produktu))
#
#     def ile_produktu(self):
#         return ("{} {}".format(self.ilosc, self.jednostka_miary))
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# cl = NaZakupy('mąka', 2, 'kg', 3)
#
# print(cl.wyswietl_produkt())
# print(cl.ile_produktu())
# print(cl.ile_kosztuje())

# zad 5
#
# class Arytmetyczne:
#     ciag = []
#     ilosc = 0
#     pe = 0
#     r = 0
#
#     def wyswietl_dane(self):
#         return f'Lista elementów: {self.ciag}'
#
#     def pobierz_elementy(self):
#         self.ilosc = int(input('Podaj ilosc elementow w ciagu: '))
#         print('Teraz podawaj kolejno wartosci elementow tego ciagu: ')
#         for i in range(self.ilosc):
#             self.ciag.append(int(input()))
#
#         print(self.ciag)
#
#     def pobierz_parametry(self):
#         self.pe = int(input("Podaj pierwszy element ciągu: "))
#         self.r = int(input("Podaj różnicę ciągu: "))
#         self.ilosc = int(input("Podaj ilość elementów ciągu do wygenerowania: "))
#
#     def policz_sume(self):
#         return f'Suma elementów: {sum(self.ciag)}'
#
#     def policz_elementy(self):
#         self.ciag.append(self.pe)
#         for x in range(1, self.ilosc):
#             self.ciag.append(self.ciag[x - 1] + self.r)
#
#
# kl = Arytmetyczne()
#
# kl.pobierz_parametry()
# kl.policz_elementy()
# print(kl.wyswietl_dane())
# print(kl.policz_sume())
#
# kl.pobierz_elementy()

# zad 6
# class Robaczek:
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += ile_krokow * self.krok
#
#     def idz_w_dol(self, ile_krokow):
#         self.y -= ile_krokow * self.krok
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= ile_krokow * self.krok
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x += ile_krokow * self.krok
#
#     def gdzie(self):
#         return f'({self.x}, {self.y})'
#
#
# robak = Robaczek(0, 0, 1)
#
# robak.idz_w_lewo(10)
# robak.idz_w_prawo(10)
# robak.idz_w_gore(1)
# robak.idz_w_dol(100)
# print(robak.gdzie())
