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

def zadanie3():
    n = 11
    while n > 10:
        n = int(input("podaj liczbe wierszy piramidy z A, ale liczba nie moze byc wieksza od 10"))

    for i in range(1, n+1):

        for j in range(1, i+2):
            # if i == 0:
            #     print("A")
            #     continue
            print("A", end="")
        print()


def piramida():
    n = int(input("liczba wierszy: "))

    for i in range(1, n + 1):
        for space in range(0, (n - i)):
            print(end="  ")

        for j in range(1,2*i):
            print("A", end="")

        print()


def zadanie5():
    n = int(input("podaj n"))
    a = []
    suma = 0
    suma_wszystkich = []
    for i in range(n):
        x = [random.randrange(1, 10000) for m in range(n)]
        a.append(x)
    for i in range(n):
        print(a[i],end="")
        for j in range(n):
            suma += a[i][j]
            suma_wszystkich.append(suma)
        print(f" = {suma}")
    return suma_wszystkich


def main():
    # zadanie1()
    # zadanie2()
    # zadanie3()
    # piramida()
    # zadanie5()
    piramida()
    print(3//2)

if __name__ == '__main__':
    main()
