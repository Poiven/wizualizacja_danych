import numpy as np


def zadanie1():
    a = np.arange(3, 46, 3) # zamiast 46 mozna 3*15+1
    print(a)


def zadanie2():
    a = np.arange(15, dtype='float')
    print(a)
    b = a.astype('int64')
    print(b)
    print(f'tablica posiada dane typu {b.dtype}.')


def zadanie3(n):
    tab = np.arange(1, n ** 2 + 1)
    tab = tab.reshape((n, n))
    print(tab)


def zadanie4(liczba, ilosc):
    # tablica = np.arang
    result = np.logspace(start=1, stop=ilosc, num=ilosc, base=liczba, dtype='int')
    return result


def zadanie5(n):
    a = np.arange(n)
    a = a[::-1]
    macierz = np.diag(a)
    print(macierz)


def zadanie6():
    tablica = np.array([["t", "o", "k", "b"], ["k", "a", "o", "l"], ["o", "j", "m", "n"],  ["c", "g", "d", "a"]])
    print(tablica)
# wykreslanka = np.zeros((6,6),dtype='str')
#wykreslanka = np.diag(mrowka)
#wykreslanka[:,0]=malina
#wykreslanka[5,::-1]=armata

def zadanie7(n):
    tab = np.zeros((n, n))
    var1 = 0
    for i in range(1, len(tab)+1):
        if i != 1:
            tab += np.diag([2 * i for a in range(n - var1)], var1)
            tab += np.diag([2 * i for a in range(n - var1)], -var1)
        else:
            tab += np.diag([2 * i for a in range(n)])
        var1 += 1
    print(tab)
    # tab+= np.diag([2* for _ in range()])


def zadanie8(n, kierunek=0):
    wiersz = n.shape[0]
    kolumna = n.shape[1]
    print(kolumna)
    kierunek = int(kierunek)
    if kierunek == 0:
        if wiersz % 2 == 0:
            return n[:(wiersz//2)]
        else:
            print("nie mozna podzielic tej tablicy wzgledem wierszy")
    elif kierunek == 1:
        if kolumna % 2 == 0:
            return n[:, 0:(kolumna//2)]
        else:
            print("nie mozna wyswietlic")


def zadanie9():
    # fibonacii
    fib = [0, 1]
    for i in range(2, 25):
        fib.append(fib[i - 1] + fib[i - 2])
    tablica_fib = np.array(fib).reshape(5, 5)
    print(tablica_fib)
    # print(fib)
    # print(len(fib))


def main():
    tab_wielowymiarowa = np.array([[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]])
    # print(tab_wielowymiarowa.shape)

    # zadanie1()
    # zadanie2()
    # zadanie3(6)
    # print(zadanie4(2,4))
    # zadanie6()
    # zadanie5(4)
    # zadanie7(5)
    # print(zadanie8(tab_wielowymiarowa, 0))
    # zadanie9()


if __name__ == '__main__':
    main()
