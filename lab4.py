import math
import random


def zadanie1():
    a = round((math.e ** 4 - math.log2(34)) ** (1/3), 2)
    print(a)
    b = (math.log(20) + math.cos(45) + math.e) ** (1/3)
    b = round(b, 2)
    print(b)
    c = (math.log(20, 3) + math.sin(45) * 5/8) ** (1/4)
    c = round(c)
    print(c, 2)
    d = math.log(23, 3) + (math.sin(34)+5) ** (1/3)
    d = round(d)
    print(d)
    e = round((math.log2(32) + math.pi + math.sin(56)) ** (1/4), 2)
    print(e)


def zadanie2():
    n = 11
    while n > 10:
        n = int(input("podaj liczbe wierszy piramidy z A, ale liczba nie moze byc wieksza od 10"))
    for i in range(1, n+1):
        for j in range(i):
            print("A",end="")
        print()

def piramida(n):
    if n < 10 | n < 1:
        print('zla wartosc n')
    else:
        a = 2*n
        for i in range(n):
            for j in range(a):
                if j == a/2:
                    print("A", end="")
                elif (j >= a/2 - i) & (j < a/2):
                    print("A", end='')
                elif (j > a/2) & (j <= a/2 + i):
                    print("A", end="")
                else:
                    print(" ", end="")
            print('')


def zadanie5():
    n = int(input("podaj n"))
    a = []
    suma = 0
    suma_wszystkich = []
    for i in range(n):
        x = [random.randrange(1, 10000) for m in range(n)]
        a.append(x)
    for i in range(n):
        print(a[i], end="")
        for j in range(n):
            suma += a[i][j]
            suma_wszystkich.append(suma)
        print(f" = {suma}")
        suma = 0
    return suma_wszystkich


def main():
    # zadanie1()
    # zadanie2()
    # piramida(10)
    zadanie5()


if __name__ == '__main__':
    main()
