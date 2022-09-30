
"""
III. MODELO DE ABSORCI�N DE DROGAS EN 
�RGANOS O C�LULAS. Un problema importante en el 
campo de la medicina consiste en determinar la absorci�n 
de qu�micos (tales como drogas) por c�lulas u �rganos. 
Supongamos que un l�quido transporta una droga dentro de 
un �rgano de volumen cm3
a una tasa de cm3
/seg y sale 
a una tasa de cm3
/seg. La concentraci�n de la droga en el 
l�quido que entra es cm3
/seg. La ecuaci�n diferencial que 
modela tal problema es:
    
    vdx/dt=ac-bx 
    
    """

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Funci�n principal

def fodemed(t,x):
    a=1  #Cm3/seg  #Tasa de entrada
    b=0.5  #cm3/seg  #Tasa de salida
    c=2  #cm3/seg #Concentraci�n de la droga en el l�quido que entra
    v=1  #cm3 volumen de �rgano a c�lula
    
    dxdt=((a*c)/v)-(b*x)/v
    
    return (dxdt)

#Par�metros de entrada

xi=0
yi=2
n=8

#Creaci�n de vectores

xtime=np.linspace(0,n)

#Condici�n inicial
y0=2
#Soluci�n de la EDO

y=odeint(fodemed,y0,xtime)

ymax=np.max(y)
print("El valor m�ximo de absorci�n es de ",ymax)

plt.plot(xtime,y)
plt.title("Absorci�n de qu�micos en c�lulas")
plt.xlabel("Tiempo (s)")
plt.ylabel("Absorci�n (cm3/seg)")
plt.grid()


















