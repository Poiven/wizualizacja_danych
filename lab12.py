import matplotlib.pyplot as plt
import numpy as np
# do listingu 4
from PIL import Image


'''
plt.plot([1,2,3,4])
plt.ylabel('jakies liczby')
plt.show()
'''

'''
plt.plot([1,2,3,4],[1,4,9,16], 'ro-')
plt.axis([0,6,0,20])
plt.show()

plt.plot([1,2,3,4],[1,4,9,16], 'r')
plt.plot([1,2,3,4],[1,4,9,16], 'o')
plt.axis([0,6,0,21])
plt.show()
'''

'''
# listing 3
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.legend(labels=['liniowa','kwadratowa','szescienna'])
plt.show()
'''

'''
x=np.linspace(0,2,100)

plt.plot(x,x, label="liniowa")
plt.plot(x,x**2, label="kwadratowa")
plt.plot(x,x**3, label="szescienna")

# etykiety osi
plt.xlabel("etykiety x")
plt.ylabel("etykiety y")

# tytul wykresu
plt.title('prosty wykres')
# włączamy pokazanie legendy
plt.legend()
plt.savefig('wykres_matplot.png')

plt.show()
im1=Image.open('wykres_matplot.png')
im1=im1.convert('RGB')
im1.save('nowy.jpg')
'''
'''
# listing5
x = np.arange(0,10,0.1)
s = np.sin(x)
plt.plot(x,s, label="sin(x)")
# etykiety osi
plt.xlabel('x')
plt.ylabel('sin(x)')
# tytul wykresu
plt.title('wykres sin(x)')
# legenda
plt.legend()

plt.show()
'''
'''
# listing 6
# daen w postaci slownika ale moze byc to pandas dataFrame
data = {"a": np.arange(50),
        "c": np.random.randint(0,50,50),
        "d": np.random.randn(50)}
data["b"] = data["a"] + 10 * np.random.randn(50)
data["d"] = np.abs(data["d"]) * 100
print(f"a={data['a'][0]},b={data['b'][0]},c={data['c'][0]},d={data['d'][0]}")
plt.scatter('a','b', c='c', s='d', data=data)
plt.xlabel('wartosc a')
plt.ylabel('wartosc b')
plt.show()

'''
# plt.xlim i .ylim moze zastapic axis a jak sie nie wyswietlaja ticki co chcemy
# to mozna uzyc plt.xticks([0,2,...]) zeby dodac wlasna podzialke

# wiecej na pdfie

# zadania

# zadanie 1

def zadanie1():
    x = np.arange(1,20)
    y = 1/x
    plt.plot(x,y, label="f(x)=1/x")
    plt.legend()
    plt.axis([1,20, 0, 1])
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("wykres funkcji f(x) dla x[1,20]")
    plt.show()


# zadanie 2

def zadanie2():
    x = np.arange(1, 20)
    y = 1 / x
    plt.plot(x, y, "g>:", label="f(x)=1/x")
    plt.legend()
    plt.axis([0, 20, 0, 1])
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("wykres funkcji f(x) dla x[1,20]")
    plt.show()


def zadanie3():
    x = np.arange(0, 31, 0.1)
    ysin = np.sin(x)
    ycos = np.cos(x)

    plt.plot(x, ysin, 'c',label="sin(x)")
    plt.plot(x, ycos, 'm',label="cos(x)")
    plt.legend()
    plt.axis([0, 30, -1, 1])
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("wykres sin i cos")
    plt.show()


def zadanie4():
    pass


zadanie1()
zadanie2()
zadanie3()