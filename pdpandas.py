import pandas as pd
import numpy as np
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# print(df[df['Liczba']>1000])

# print(df[df["Imie"]=='BARTOSZ'])

# nie rozumiem o jaki okres chodzi

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
# print(df)
# a = df.drop_duplicates(subset="Sprzedawca")
# sprzedawcy = a['Sprzedawca']
# print(sprzedawcy)

