import numpy as np
def funkcja1():
    a = np.arange(12).reshape((3,4))
    print(a)
    print(a.sum())
    print()
    print(a.sum(axis=0)) # suma kazdej z kolumn
    print()
    print(a.min(axis=1)) # min kazdego rzedu
    print()
    print(a.cumsum(axis=1)) # skumulowana suma dla rzedu


def funkcja2():
    b=np.arange(3)
    print(b)
    print()
    print(np.exp(b))
    print()
    print(np.sqrt(b))
    print()
    c = np.array([2.,-1.,4.])
    print(c)
    print(np.add(b,c))

def funkcja3():
    a=np.arange(6).reshape((3,2))
    print(a)

    for b in a.flat:
        print(b)
        print()
    c=np.arange(1,10)
    print(c)
    print(a.flat)


def funkcja4():
    a=np.arange(6)
    print(a)
    print(a.shape)
    b=a.reshape((2,3))
    print(b)
    print(b.shape)
    c=b.reshape((3,2))
    print(c)
    print(c.shape)
    print()
    d = c.ravel()
    print(d)
    print(d.shape)




# funkcja1()
# funkcja2()
funkcja3()
funkcja4()