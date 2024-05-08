import pandas as pd
# import numpy as np

df = pd.read_excel('imiona.xlsx', sheet_name=0)
df2 = pd.read_csv("zamowienia.csv", sep=";", decimal=".")

def kropka1():
    print(df[df["Liczba"]>1000])


def kropka2():
    print(df[df["Imie"]=="DAWID"])


def kropka3():
    print("suma urodzonych: ")
    print(sum(df["Liczba"]))
    # print(df.groupby(["Rok", "Plec"]).agg({"Liczba": "sum"}))


def kropka4():
    print(sum(df["Liczba"].where(df["Rok"].isin([2000,2001,2002,2003,2004,2005]), 0)))


def kropka5():
    print(df.groupby(["Plec"]).agg({"Liczba":"sum"}))
    # print("suma chłopców: ")
    # print(sum(df["Liczba"].where(df["Plec"]=="M",0)))
    # print()
    # print("suma dziewczynek:")
    # print(sum(df["Liczba"].where(df["Plec"]=="K",0)))


def kropka6():
    print(df.groupby(["Rok","Plec"]).agg({"Liczba":"max"}))


def kropka7():
    print(df.groupby(["Plec"]).get_group("M").agg({"Liczba": "max"}))
    # print(df["Imie"].where())


def zad31():
    print(df2["Sprzedawca"].unique())


def zad32():
    posortowane=df2.sort_values(by="Utarg",ascending=False)
    posortowane=posortowane["Utarg"]
    print(posortowane[0:5])


def zad33():
    # df2.groupby(["Sprzedawca"]).agg()
    pass


def main():
    # kropka1()
    # kropka2()
    # kropka3()
    # kropka4()
    # kropka5()
    # kropka6()
    # kropka7()
    # zad31()
    zad32()



if __name__ == "__main__":
    main()