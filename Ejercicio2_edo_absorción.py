
"""
III. MODELO DE ABSORCIÓN DE DROGAS EN 
ÓRGANOS O CÉLULAS. Un problema importante en el 
campo de la medicina consiste en determinar la absorción 
de quí­micos (tales como drogas) por células u órganos. 
Supongamos que un lí­quido transporta una droga dentro de 
un órgano de volumen cm3
a una tasa de cm3
/seg y sale 
a una tasa de cm3
/seg. La concentración de la droga en el 
lí­quido que entra es cm3
/seg. La ecuación diferencial que 
modela tal problema es:
    
    vdx/dt=ac-bx 
    
    """

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Función principal

def fodemed(t,x):
    a=1  #Cm3/seg  #Tasa de entrada
    b=0.5  #cm3/seg  #Tasa de salida
    c=2  #cm3/seg #Concentración de la droga en el lí­quido que entra
    v=1  #cm3 volumen de órgano a célula
    
    dxdt=((a*c)/v)-(b*x)/v
    
    return (dxdt)

#Parámetros de entrada

xi=0
yi=2
n=8

#Creación de vectores

xtime=np.linspace(0,n)

#Condición inicial
y0=2
#Solución de la EDO

y=odeint(fodemed,y0,xtime)

ymax=np.max(y)
print("El valor máximo de absorción es de ",ymax)

plt.plot(xtime,y)
plt.title("Absorción de quí­micos en células")
plt.xlabel("Tiempo (s)")
plt.ylabel("Absorción (cm3/seg)")
plt.grid()


















