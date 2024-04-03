import math
import random
import sys

def zadanie1():
    for x in range(13,30):
        print(x, round((math.exp(x)+math.cos(x))**(1/4),2))


def zadanie2(Min, Max, ile):
    try:
        lista = [random.randint(Min, Max) for _ in range(ile)]
        # print(lista)
        slownik = {}
        for i in lista:
            counter = 0
            for j in lista:
                if i==j:
                    counter += 1
            slownik[i]=counter
        return slownik
    except ValueError:
        print("wystapil blad")


def zadanie3():
    f=open("liczby1.txt","r")
    tekst = f.readlines()
    f.close()

    suma_w = 0
    suma_k = 0

    # print(tekst)
    for i in range(len(tekst)):
        tekst[i]=tekst[i].strip()
        tekst[i]=tekst[i].split()
    # print(tekst)

    for i in range(len(tekst)):
        for j in range(len(tekst)):
            tekst[i][j] = int(tekst[i][j])
    # print(tekst)

    for i in range(len(tekst)):
        for j in range(len(tekst)):
            suma_w += tekst[i][j]
            suma_k += tekst[j][i]

    wynik = suma_w + suma_k
    return wynik


def zadanie4():
    print("podaj a: ")
    a = abs(int(sys.stdin.readline()))
    # print(a)
    print("podaj h: ")
    h = abs(int(sys.stdin.readline()))
    if a == 0 or h == 0:
        print("wymiary nie moga wynosic 0")
        return 0
    else:
        return (a**2)*h*1/3


def main():
    print("zadanie 1")
    zadanie1()

    print()
    print("zadanie 2")
    print(zadanie2(1,10,10))

    print()
    print("zadanie 3")
    print(f"suma z wartości z wierszy i kolumn to: {zadanie3()}")

    print()
    print("zadanie 4")
    print(zadanie4())


if __name__ == '__main__':
    main()
