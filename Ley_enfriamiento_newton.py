# -*- coding: utf-8 -*-
"""

Ejercicio de la Ley de enfriamiento de newton

"""
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
ipython=get_ipython()
ipython.magic("%clear")
#Funciones

def funt (y):
    dTdt=-kalcohol*(y-Ta) #Mejor conductor termico (Numerica) (Acero)
    
    
    return dTdt
    
def funt1 (y1):
    dTdt=-kagua*(y1-Ta) #Peor conductor termico (Numerica 2) (Agua)
    
    return dTdt


def meuler2 (xi,yi,h,f):
    x=xi+h
    y=yi+h*f(yi)

    
    return x,y


#Parámetros de entrada

xi=0.0
yi=300.0

y2=200.0
Ta=70.0
xf=120

kalcohol=0.19 #Constante de conductividad termica para el Alcohol #Ejercicio
kagua=0.58 #Constante de conductividad termica para el agua

n=3000


 
for n in [3000, 6000, 8000]:
    
    xnumalcohol=np.zeros(n)
    ynumalcohol=np.zeros(n)

    xnumagua=np.zeros(n)
    ynumagua=np.zeros(n)

    xnumagua[0]=xi
    ynumagua[0]=yi

    xnumalcohol[0]=xi
    ynumalcohol[0]=yi

    h=(xf-xi)/(n-1)


    for i in range (1,n):
        xnumalcohol[i],ynumalcohol[i]=meuler2(xnumalcohol[i-1],ynumalcohol[i-1],h,funt)
        xnumagua[i],ynumagua[i]=meuler2(xnumagua[i-1],ynumagua[i-1],h,funt1)
        
    yanalalcohol=(230)*np.exp(-kalcohol*xnumalcohol)+Ta
    yanalagua=230*np.exp(-kagua*xnumagua)+Ta

    #Error
    yerragua=np.zeros(n)
    yerralcohol=np.zeros(n)

    for i in range (0,n):
        yerragua[i]=np.abs((yanalagua[i]-ynumagua[i])/(yanalagua[i]))*100
        yerralcohol[i]=np.abs((yanalalcohol[i]-ynumalcohol[i])/(yanalalcohol[i]))*100
        

    #Analitica
    vectoranalagua=np.array([xnumagua,yanalagua])
    vectoranalalcohol=np.array([xnumalcohol,yanalalcohol])
    
    plt.figure(n)

    plt.plot(xnumalcohol,ynumalcohol,label="Solución numérica alcohol")
    plt.plot(xnumagua,ynumagua,label="Solución numérica agua")
    plt.plot(xnumalcohol,yanalalcohol,"g--",label="Solución analitica alcohol")
    plt.plot(xnumagua,yanalagua,"r--",label="Solución analítica agua")
    plt.xlabel("Tiempo (min)")
    plt.ylabel("Temperatura (°F)")
    plt.title("Gráfico de enfriamiento")
    plt.grid()
    plt.legend()

    plt.figure(n+1)

    plt.title("Error vs tiempo")
    plt.plot(xnumalcohol,yerralcohol,label="Error para el alcohol")
    plt.plot(xnumagua,yerragua,label="Error para el agua")
    plt.xlabel("Tiempo (min)")
    plt.ylabel("Error %")
    plt.legend()
    plt.grid()

plt.figure(3000)
plt.title("Grafico enfriamiento n=3000")

plt.figure(3001)
plt.title("Grafico de errores n=3000")

plt.figure(6000)
plt.title("Grafico enfriamiento n=6000")

plt.figure(6001)
plt.title("Grafico de errores n=6000")

plt.figure(8000)
plt.title("Grafico de enfriamiento n=8000")

plt.figure(8001)
plt.title("Grafico de errores n=8000")

#Numerica
vectoragua=np.array([xnumagua,ynumagua])
vectoralcohol=np.array([xnumalcohol,ynumalcohol])
print("                                INFORME                                      ")
print("\n")
print("Con una n de",n)
print("Para unos valores iniciales de: ")
print("Temperatura ambiente 70°F, conductividad termica del agua 0.58, conductividad termica del alcohol 0.19, Temperatura inicial de 300°F, temperatura final igual a la temperatura ambiente y con el modelo de enfriamiento de Newton")
print("\n")
print("Con el método numérico se tiene que:")
print("\n")
print("EL alcohol, llega a una temperatura ambiente en 80.46min")
print("EL agua, llega a una temperatura ambiente en 26.17min")
print("Posiblemente el alcohol fue el material utilizado en la modelación de la EDO")
print("\n")
print("Con el método analítico se tiene que:")
print("\n")
print("El alcohol, llega a una temperatura ambiente en 80.79min")
print("El agua,llega a una temperatura ambiente en 26.49min")
print("\n")
print("Si se toma el modelo analítico como un método exacto se tiene que al comparar el método numérico con el metodo analítico se encuentra el grafico de Error vs tiempo")
print("\n")
print("Finalmente, se observa que el modelo inicial de la EDO se ajusta a una constante k de 0.19 lo cual da una idea del posible material utilizado para este modelo.En este sentido, se tiene que al utilizar otro valor de k, el ajuste realizado no sigue completamente los parámetros de la EDO, pero, se mantiene un comportamiento similar como se muestra en el gráfico realizado")


