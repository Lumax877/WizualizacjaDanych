import pandas as pd
import numpy as np
import xlrd
import openpyxl

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# print(df[df['Liczba']>1000])

# print(df[df["Imie"]=='BARTOSZ'])

# a = df.agg({'Liczba':['sum']})
# print(a)

# new_df = df[((df["Rok"] >= 2000) & (df["Rok"]<=2005))]
# index = new_df.index
# print(len(index))

# ko = df[df["Plec"] == "K"]
# licz = ko.index
# print(len(licz))
# me = df[df["Plec"] == "M"]
# licz2 = me.index
# print(len(licz2))

# print(ko['Imie']. value_counts(). idxmax())
# print(me['Imie']. value_counts(). idxmax())

# zad 3

df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=",")

# a = df.drop_duplicates(subset="Sprzedawca")
# sprzedawcy = a['Sprzedawca']
# print(sprzedawcy)

# top 5

# a = df['Sprzedawca'].value_counts()
# print(a)

# a = df['Kraj'].value_counts()
# print(a)


# a = df[(df["Kraj"] == "Polska")]# nie mam pomyslu na znalezienie roku 2005, bo kolumna nie jest napisana w datetime type
# b = a['Kraj'].value_counts()
# print(b)



