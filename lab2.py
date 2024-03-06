import sys as system


def zadanie1():
    n = input("podaj dowolną liczbę słów: ")
    n = n.strip()
    counter = 0
    for _ in n:
        if _ == " ":
            counter += 1
    print(f"jest/są {counter + 1} wyrazow")


def zadanie2():
    system.stdout.write("podaj liczbę: ")
    a = system.stdin.readline()
    b = system.stdin.readline()
    c = int(system.stdin.readline())
    a = int(a)
    b = int(b)
    wynik = a ** b + c
    system.stdout.write(f"wynik działania to {wynik}")


def zadanie3():
    n = input("podaj jakies zdanie do policzenia ilosci znakow")
    # n=n.strip()
    # print(n)
    if n == n[::-1]:
        print("sa rowne")


def zadanie4():
    n = int(input("podaj liczbę"))
    for i in range(2, (n//2)+1):
        if n % i == 0:
            print("nie jest liczbą pierwszą")
            return False
        else:
            print("jest liczbą pierwszą")
            return True


def zadanie5():
    counter = 0
    for j in range(1, 1000):
        suma = 0
        for i in range(1, j):
            if j % i == 0:
                suma += i
        if suma == j:
            # print("liczba doskonala")
            counter += 1
    print(f"doskonalych licz w zakresie do 1000 jest {counter}")


def zadanie6():
    lista = [12, 45.7, 16, 10, 1.5]
    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    print(lista)


def zadanie7():
    lista = []
    i = 0
    while i < 10:
        n = int(input("podaj liczbę: "))
        if (n % 2) == 0:
            lista.append(n)
        i += 1
    print(lista)


def zadanie8():
    slownik = {}
    do_usuniecia = []
    lista = ["kot", 15, 2.5, "nic", 15, "kot"]
    for i in lista:
        # print(i)
        counter = lista.count(i)
        slownik[i] = counter
    # print(slownik)

    for k in slownik:
        # print(k)
        if not (isinstance(k, int) or isinstance(k, float)):
            do_usuniecia.append(k)

    for n in do_usuniecia:
        del slownik[n]
    print(slownik)


def main():
    zadanie1()
    zadanie2()
    zadanie3()
    zadanie4()
    zadanie5()
    zadanie6()
    zadanie7()
    zadanie8()


if __name__ == '__main__':
    main()
