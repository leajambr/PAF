import numpy as np

def derivacija_točke(f,x, h = 0.01, metoda = 3):
    if metoda == 2:
        return (f(x + h) - f(x))/h             # two point
    else:
        return (f(x + h) - f(x - h))/(2*h)     # three point
    
def raspon_derivacije(f, donja, gornja, h = 0.01, metoda = 3 ):     # gornja i donja granica raspona deriv
    lista_točaka = []
    lista_derivacija_točaka = []
    točke = np.linspace(donja, gornja, 40)

    for i in točke:
        derivacija = derivacija_točke(f, i,h, metoda = 3)
        lista_točaka.append(i)                     
        lista_derivacija_točaka.append(derivacija)      # numerička derivacija
                                                             
    return lista_točaka,lista_derivacija_točaka              

def integracija(f, a, b, n):
    dx = (b - a)/n
    x = np.linspace(a,b,n)
    sumd = 0
    sumg = 0
    
    for i in range(n):
        sumg += f(x[i] + dx)*dx

        if x[i] < b - dx:
            sumd += f(x[i])*dx

    return sumd, sumg

def trapezna_integracija(f, a, b, n):     # k-1

    dx = (b - a)/n

    sumtrapez = (f(a)+f(b))/2

    for i in range(1,n):
        
        sumtrapez += f(a + i*dx)
    
    sumtrapez *= dx

    return sumtrapez










