import numpy as np
from sympy import *
#from scipy.integrate import odeint
#from scipy import integrate
#import matplotlib.pyplot as plt

def test_run():
# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
    a = np.linspace(-1.3, 2.5, 64)
    print("\n\n 1. 64 PIECES: \n", a)
    new_line()

# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
    n = 6
    b = np.tile([1, 2, 3], n)
    print("2. CYCLE: \n", b)
    new_line()

# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
    c = np.arange(20)[1::2]
    print("3. ODD: \n", c)
    new_line()

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
    d = np.zeros((10, 10), dtype=int)
    d[::9].fill(1)
    d[::,::9].fill(1)
    print("4. 10x10 FRAME: \n", d)
    new_line()

# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
    e = np.zeros((8, 8), dtype=int)
    e[::2,::2].fill(1)
    e[1::2,1::2].fill(1)
    print("5. CHESS: \n", e)
    new_line()
    # [start:end:step]

# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
    n = 6
    f = np.indices((n,n))
    f_indexed = np.add(f[0], f[1])
    print("6. i+j = POSITIONS: \n", f_indexed)
    new_line()

# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
    g = np.random.rand(3, 5)
    print("7. 3x5 RANDOM.RAND: \n", g)
    gsum = g.sum()
    print("Sum of all array elements: \n", gsum)
    growsum = np.sum(g, axis=1).tolist()
    print("Sums of array rows: \n", growsum)
    gcolsum = np.sum(g, axis=0).tolist()
    print("Sums of array columns: \n", gcolsum)
    new_line()
# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
    h = np.random.rand(5, 5)
    print("8. 5x5 RANDOM.RAND: \n", h)
    h_sort = h[h[:,1].argsort()]
    print("SORTED: \n", h_sort)
    new_line()

# 9. Atvirkštinę matricą
    i = np.array([[1,4],[-3,9]])
    print("9. NORMAL: \n", i)
    i_inv = np.linalg.inv(i)
    print("INVERSION: \n", i_inv)
    new_line()

# 10.Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
    j = np.array([[0,1],[-2,-3]])
    print("10. MATRIX: \n", j)
    j_w, j_v = np.linalg.eig(j)
    print("EIGENVALUES: \n", j_w)
    print("EIGENVECTORS: \n", j_v)
    new_line()

# 11.Pasirinktos funkcijos išvestinę
    x, y = symbols('x y')
    init_printing(use_unicode=True)
    deriv = diff(cos(x), x)
    print("11. DERIVATIVE (of function  'cos(x)') :  \n", deriv)
    new_line()

# 12.Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
    '''
    x2 = lambda x: x**2
    int_def = integrate.quad(x2, 0, 4)
    '''
    int_def = integrate(cos(x), x)
    print("12. INTEGRAL (DEFINITE) (of function 'cos(x)') : \n", int_def)
    int_indef = integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
    print("INTEGRAL (INDEFINITE) (of function 'exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)') : \n", int_indef)
    new_line()

# end of tasks
def new_line():
    print()
    print('************************************************')
    print()


if __name__ == "__main__":
    test_run()