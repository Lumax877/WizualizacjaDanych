import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zad 1

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot(xticks = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017], figsize = (10,10))
# plt.legend(loc='lower right')
# plt.title('Liczba narodzin dzieci w danym roku')
# plt.show()

# zad 2

# xlsx = pd.ExcelFile(r'datasets\imiona.xlsx')
# data = pd.read_excel(xlsx, header=0)
# df = pd.DataFrame(data)
#
# grupa = df.groupby(['Plec']).agg({'Liczba': {'sum'}})
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# plt.show()

# zad 3

# xlsx = pd.ExcelFile(r'datasets\imiona.xlsx')
# data = pd.read_excel(xlsx, header=0)
# df = pd.DataFrame(data)
#
# grupa = df.where(df['Rok'] > 2012).groupby(['Plec']).agg({'Liczba': {'sum'}})
# wykres = grupa.plot.pie(subplots=True, fontsize=20)
# plt.show()

# zad 4

# df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=",")
# a = df['Sprzedawca'].value_counts()
# wykres = a.plot.bar(figsize = (8,8))
# plt.show()