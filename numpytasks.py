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
    b = np.tile([1, 2, 3], 5)
    print("2. CYCLE: \n", b)
    new_line()

# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
    c = np.arange(10)[1::2]
    print("3. ODD: \n", c)
    new_line()

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
    d = np.zeros((10, 10), dtype=int)
    d[0].fill(1)
    d[9].fill(1)
    print("4. 10x10 ZEROS: \n", d)
    new_line()
#-

# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
    e = np.zeros((8, 8), dtype=int)
    e[::2,::2].fill(1)
    e[1::2,1::2].fill(1)
    print("5. CHESS: \n", e)
    new_line()
    # [start:end:step]

# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j

#-

# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
    f = np.random.rand(3, 5)
    print("7. 3x5 RANDOM.RAND: \n", f)
    fsum = f.sum()
    print("Sum of all array elements: \n", fsum)
    frowsum = np.sum(f, axis=1).tolist()
    print("Sums of array rows: \n", frowsum)
    fcolsum = np.sum(f, axis=0).tolist()
    print("Sums of array columns: \n", fcolsum)
    new_line()
# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
    g = np.random.rand(5, 5)
    print("8. 5x5 RANDOM.RAND: \n", g)
#-
    new_line()

# 9. Atvirkštinę matricą
    h = np.array([[1,4],[-3,9]])
    print("9. NORMAL: \n", h)
    h_inv = np.linalg.inv(h)
    print("INVERSION: \n", h_inv)
    new_line()

# 10.Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
    i = np.array([[0,1],[-2,-3]])
    print("10. MATRIX: \n", i)
    i_w, i_v = np.linalg.eig(i)
    print("EIGENVALUES: \n", i_w)
    print("EIGENVECTORS: \n", i_v)
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