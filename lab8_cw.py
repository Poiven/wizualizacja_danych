import numpy as np


def zadanie1():
    a = np.array([1,3,4])
    b = np.array([5,6,7])
    c = a.dot(b)
    print(a)
    print(b)
    print()
    print(c)
    # print(np.dot(a,b))


def zadanie2():
    a = np.arange(9).reshape((3,3))
    b = np.arange(2,18).reshape((4,4))

    aMinRow = a.min(axis=1)
    aMinCol = a.min(axis=0)
    print(f"a min rzedu: {aMinRow}, kolumy: {aMinCol}")

    bMinRow = b.min(axis=1)
    bMinCol = b.min(axis=0)
    print(f"b min rzedu: {bMinRow}, kolumny: {bMinCol}")


def zadanie3():
    a = np.array([1, 3, 4])
    b = np.array([5, 6, 7])
    # a = a*2
    # b = b*2
    c = a*b
    print(a)
    print(b)
    print(c)


def zadanie4():
    pass



def main():
    # zadanie1()
    # zadanie2()
    zadanie3()



if __name__ == '__main__':
    main()