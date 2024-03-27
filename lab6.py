import numpy as np
a = np.arange(2)
print(a)
a = np.array([0, 1])
print(a)
print(type(a))
print(a.dtype)
a = np.arange(2, dtype='int64')
print(a.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)
print(a.ndim)
m=np.array([np.arange(2), np.arange(2)])
print(m.shape)
print(type(m))
print()
print()
# przyklad 2
zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2))
print(pusta)
poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)
print()
print()

macierz = np.array([[1,2],[3,4]])
print(macierz)

liczby=np.arange(1, 2, 0.1)
print(liczby)

liczby_lin = np.linspace(1,2,5)
print(liczby_lin)

z = np.indices((5,3))
print(z)


x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

print()
print()

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)

z=np.fromiter(range(5), dtype='int32')
print(z)

marcin = b'Marcin'
mar = np.frombuffer(marcin,dtype='S1')
print(mar)
mar_2 = np.frombuffer(marcin,dtype='S2')
print(mar_2)

marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_4 = np.array(list(marcin),dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin, dtype='S1')
mar_7 = np.fromiter(marcin, dtype='U1')

print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)

mat = np.ones((2, 2))
mat_1 = np.ones((2, 2))
mat = mat + mat_1

print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)