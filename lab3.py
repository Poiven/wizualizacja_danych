import math
import random


def zadanie1():
    A = [1 - x for x in range(1, 11)]
    print(A)
    B = [4 ** x for x in range(8)]
    print(B)
    C = [x for x in B if x % 2 == 0]
    print(C)


def zadanie2():
    # losowa liczba bez powtorzen z danej listy itp
    lista1 = random.sample(range(1000000), 10)
    lista2 = [x for x in lista1 if x % 2 == 0]
    # print(lista1)
    print(lista2)


def zadanie3():
    lista_zakupow = {'jajka': 'sztuki', 'butelki wody': 'sztuki', 'cukier': 'kg', 'szynka': 'dag'}
    nowa_lista = [x for x in lista_zakupow if lista_zakupow[x] == 'sztuki']
    print(nowa_lista)


# zadanie4
def trojkat():

    # n = [int(input("podaj liczbę do sprawdzenia: ")) for x in range(3)]
    a = int(input("podaj 'a' do sprawdzenia: "))
    b = int(input("podaj b do sprawdzenia: "))
    c = int(input("podaj c do sprawdzenia: "))
    tak = 'jest to trojkat prostokatny'
    nie = 'nie jest to trojkat prostokatny'

    if a > b:
        if a > c:
            if (b ** 2) + (c ** 2) == a ** 2:
                print(tak)
                return True
            else:
                print(nie)
                return False
        else:
            if (b ** 2) + (a ** 2) == c ** 2:
                print(tak)
                return True
            else:
                print(nie)
                return False
    else:
        if b > c:
            if (c ** 2) + (a ** 2) == b ** 2:
                print(tak)
                return True
            else:
                print(nie)
                return False
        else:
            if (b ** 2) + (a ** 2) == c ** 2:
                print(tak)
                return True
            else:
                print(nie)
                return False


# zadanie 5
def trapez(a=2, b=4, h=1):
    return ((a + b) * h) / 2


# zadanie 6
def iloczyn_ciagu(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile):
        a *= b
        iloczyn *= a
    return iloczyn


# wersja alternatywna
'''
def iloczyn_ciagu2(a=1, b=4, ile=10):
    # iloczyn = a
    ciag = []
    for i in range(ile):
        ciag.append(a)
        a *= b
    print(ciag)'''


def zadanie7():
    try:
        liczba = float(input("Podaj liczbę: "))
        if liczba < 0:
            raise Exception
        pierwiastek = math.sqrt(liczba)
        print(f"Pierwiastek z {liczba} wynosi {pierwiastek}.")
    except Exception:
        print("Nie można policzyć pierwiastka z liczby ujemnej.")


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    trojkat()
    print(trapez())
    # print(trapez(10, 10, 2))
    print(iloczyn_ciagu(1, 2, 4))
    # iloczyn_ciagu2(1, 2, 11)
    zadanie7()


if __name__ == '__main__':
    main()
