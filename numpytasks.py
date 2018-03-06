import numpy as np
from scipy.integrate import odeint
from scipy import integrate
import matplotlib.pyplot as plt

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
    print("11. DIFFERENTIAL CALCULUS: \n")
    new_line()
    # function that returns dy/dt
    def model(y,t,k):
        dydt = -k * y
        return dydt

    # initial condition
    y0 = 5

    # time points
    t = np.linspace(0,20)

    # solve ODEs
    k = 0.1
    y1 = odeint(model,y0,t,args=(k,))
    k = 0.2
    y2 = odeint(model,y0,t,args=(k,))
    k = 0.5
    y3 = odeint(model,y0,t,args=(k,))

    # plot results
    plt.plot(t,y1,'r-',linewidth=2,label='k=0.1')
    plt.plot(t,y2,'b--',linewidth=2,label='k=0.2')
    plt.plot(t,y3,'g:',linewidth=2,label='k=0.5')
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.legend()
    plt.show()


# 12.Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
    x2 = lambda x: x**2
    int_def = integrate.quad(x2, 0, 4)
    print("12. INTEGRAL (DEFINITE): \n", int_def)
    new_line()

# end of tasks
def new_line():
    print()
    print('************************************************')
    print()


if __name__ == "__main__":
    test_run()