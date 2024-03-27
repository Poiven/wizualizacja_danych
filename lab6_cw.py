import numpy as np

def zadanie1():
    a = np.arange(3,46,3)
    print(a)


def zadanie2():
    a = np.arange(15,dtype='float')
    print(a)
    b = a.astype('int64')
    print(b)
    print(f'tablica posiada dane typu {b.dtype}.')


def zadanie3(n):
    tab = np.arange(1, n ** 2 + 1)
    tab = tab.reshape((n,n))
    print(tab)


def zadanie4(liczba, ilosc):
    # tablica = np.arang
    result = np.logspace(start=1,stop=ilosc, num=ilosc, base=liczba, dtype='int')
    return result


def zadanie5(n):
    a = np.arange(n)
    a = a[::-1]
    macierz = np.diag(a)
    print(macierz)


def zadanie6():
    pass


def zadanie7(n):
    # tab = np.zeros((n,n))
    # for i in range(1, 2*n):
    #     tab += np.diag([2*],+)
    # print(tab)
    #
    # print(np.array([[2,4,6,8],[4,2,4,6]]))
    pass





def main():
    # zadanie1()
    # zadanie2()
    # zadanie3(6)
    # print(zadanie4(2,4))
    zadanie5(4)
    zadanie7(4)



if __name__ == '__main__':
    main()
