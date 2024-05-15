import numpy as np
import pandas as pd
import matplotlib.pyplot as plt





'''
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()
'''
'''
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],'Stolica':['Bruksela', 'New Delhi', 'Brasilia','Warszawa'],'Kontynent': ['Europa','Azja', 'Ameryka Południowa','Europa'], 'Populacja':[11190846,1303171035,207847528,38675467]}

df = pd.DataFrame(data)
print(df)

grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
print(grupa)

wykres = grupa.plot.bar()
wykres.set_ylabel("Mld")
wykres.set_xlabel("Kontynent")
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title("Populacja z podziałem na kontynenty")
plt.show()
'''
def zadanie1():
    df = pd.read_excel('imiona.xlsx', sheet_name=0)
    # df2 = pd.read_csv("zamowienia.csv", sep=";", decimal=".")

    sumaUrodzen = df.groupby(["Rok"]).agg({"Liczba": "sum"})
    df2 = pd.DataFrame(sumaUrodzen, columns=['Rok','Liczba'])
    df2.plot()
    lata = df["Rok"].unique()
    plt.xticks(lata)
    plt.xticks(rotation=90)
    plt.show()


def zadanie2():
    df = pd.read_excel('imiona.xlsx', sheet_name=0)

    sumaUrodzen = df.groupby(["Plec"]).agg({"Liczba": "sum"})
    wykres = sumaUrodzen.plot.bar()
    wykres.set_ylabel("Liczba")
    wykres.set_xlabel('Płeć')
    wykres.tick_params(axis='x', labelrotation=0)
    wykres.legend()
    wykres.set_title("urodzenia wedlug plci")
    plt.show()


def zadanie3():
    df = pd.read_excel('imiona.xlsx', sheet_name=0)
    df = df.groupby(["Rok","Plec"]).agg({"Liczba": "sum"}).tail(5)
    sumaUrodzen = df.groupby(["Plec"]).agg({"Liczba": "sum"})
    # print(sumaUrodzen)
    sumaUrodzen.plot(kind='pie',subplots=True, autopct='%.2f%%', fontsize=20,figsize=(6,6), colors=['red','blue'])
    plt.title("Ilość urodzeń chłopców i dziewczynek w ostatnich 5 latach")
    plt.show()


def zadanie4():
    df2 = pd.read_csv("zamowienia.csv", sep=";", decimal=".")
    grupa = df2.groupby(["Sprzedawca"]).agg({"idZamowienia": "count"})
    wykres = grupa.plot.bar()
    wykres.set_ylabel("Ilosc zamowien")
    wykres.set_xlabel("Sprzedawca")
    wykres.tick_params(axis="x",labelrotation=0)
    wykres.legend()
    wykres.set_title("Zamowienia zrobione przez Sprzedawców")
    plt.show()



if __name__ == '__main__':
    # zadanie1()
    # zadanie2()
    zadanie3()
    # zadanie4()
    # pass
