
import numpy as np
import matplotlib.pyplot as plt
from math import sin


from IPython import get_ipython
ipython=get_ipython()
ipython.magic("%clear")

"""
#Funciones
"""

#Función del problema sin rozamiento
def fode (x,y):
    dydx=np.array([y[1],-g/(L*m)*sin(np.radians(y[0]))])
    
    return dydx

#Función del problema con rozamiento
def foder (x,y):
    dydx=np.array([y[1],(-g/(L*m))*sin(np.radians(y[0]))-a*y[1]])
    
    return dydx
   
#Función euler
def meuler(xi,yi,h,f):
    x=xi+h
    y=yi+h*f(xi,yi)
    
    return(x,y)

#Runge kutta orden 2
def rk2(xi,yi,h,f):
    x=xi+h
    k1=h*f(xi,yi)
    k2=h*f(xi+0.5*h,yi+0.5*k1)
    y=yi+((k1+2*k2)/2)
    
    return (x,y)

#Runge kutta orden 3
def rk3(xi,yi,h,f):
    x=xi+h
    k1=h*f(xi,yi)
    k2=h*f(xi+0.5*h,yi+0.5*k1)
    k3=h*f(xi+h,yi-k1+2*k2)
    y=yi+(k1+4*k2+k3)/6
    
    return (x,y)

#Runge Kutta orden 4
def rk4(xi,yi,h,f):
    x=xi+h
    
    k1=h*f(xi,yi)
    k2=h*f(xi+0.5*h,yi+0.5*k1)
    k3=h*f(xi+0.5*h,yi+0.5*k2)
    k4=h*f(xi+h,yi+k3)
    
    y=yi+(k1+2*k2+2*k3+k4)/6
    
    return x,y

"""
Main del programa
"""

#Parámetros iniciales

xi=0
xf=10
n=100
g=9.81 #m/s2
L=1
m=0.1 #kg
a=1 #rozamiento

h=(xf-xi)/(n-1)

yi=np.array([90,0.0]) #Condición inicial

#Definiendo vectores

x=np.zeros(n)
ynumrk4=np.zeros(shape=(n,2))#Matriz solución

#Valores iniciales
ynumrk4[0,0]=yi[0]
ynumrk4[0,1]=yi[1]

#rk4
for i in range(1,n):
    x[i],ynumrk4[i,:]=rk4(x[i-1],ynumrk4[i-1,:],h,fode)
    
#rk3
x2=np.zeros(n)
ynumrk3=np.zeros(shape=(n,2))
ynumrk3[0,0]=yi[0]
ynumrk3[0,1]=yi[1]
for i in range(1,n):
    x2[i],ynumrk3[i,:]=rk3(x[i-1],ynumrk3[i-1,:],h,fode)
#rk2
x3=np.zeros(n)
ynumrk2=np.zeros(shape=(n,2))
ynumrk2[0,0]=yi[0]
ynumrk2[0,1]=yi[1]
for i in range(1,n):
    x3[i],ynumrk2[i,:]=rk2(x[i-1],ynumrk2[i-1,:],h,fode)
    
#meuler
x4=np.zeros(n)
yeul=np.zeros(shape=(n,2))
yeul[0,0]=yi[0]
yeul[0,1]=yi[1]
for i in range(1,n):
    x4[i],yeul[i,:]=meuler(x[i-1],yeul[i-1,:],h,fode)
    
##############################################################

#Vectores pendulo con rozamiento rk4
#Rk4 con rozamiento
x1=np.zeros(n)
ynumrk4con=np.zeros(shape=(n,2))
ynumrk4con[0,0]=yi[0]
ynumrk4con[0,1]=yi[1]

for i in range(1,n):
    x1[i],ynumrk4con[i,:]=rk4(x[i-1],ynumrk4con[i-1,:],h,foder)
    
#Rk3
x6=np.zeros(n)
ynumrk6con=np.zeros(shape=(n,2))
ynumrk6con[0,0]=yi[0]
ynumrk6con[0,1]=yi[1]

for i in range(1,n):
    x6[i],ynumrk6con[i,:]=rk3(x[i-1],ynumrk6con[i-1,:],h,foder)
    
#rk2
x7=np.zeros(n)
ynumrk7con=np.zeros(shape=(n,2))
ynumrk7con[0,0]=yi[0]
ynumrk7con[0,1]=yi[1]

for i in range(1,n):
    x7[i],ynumrk7con[i,:]=rk2(x[i-1],ynumrk7con[i-1,:],h,foder)
    
#Meuler
x8=np.zeros(n)
ynumrk8con=np.zeros(shape=(n,2))
ynumrk8con[0,0]=yi[0]
ynumrk8con[0,1]=yi[1]

for i in range(1,n):
    x8[i],ynumrk8con[i,:]=meuler(x[i-1],ynumrk8con[i-1,:],h,foder)
    
 
"""
Gráficos
"""

plt.figure(1,figsize=(8,14))
plt.grid()


plt.subplot(4,2,1)
plt.plot(x,ynumrk4[:,0])
plt.title("Posición Vs. Tiempo RK4")
plt.grid()


plt.subplot(4,2,2)
plt.plot(x,ynumrk4con[:,0],"g")
plt.title("Posicón Vs. Tiempo RK4 + rozamiento")
plt.grid()


plt.subplot(4,2,3)
plt.plot(x3,ynumrk3[:,0])
plt.title("Posición Vs. Tiempo RK3")
plt.grid()


plt.subplot(4,2,4)
plt.plot(x6,ynumrk6con[:,0],"g")
plt.title("Posición Vs. Tiempo RK3 + rozamiento")
plt.grid()


plt.subplot(4,2,5)
plt.plot(x3,ynumrk2[:,0])
plt.title("Posición Vs. Tiempo RK2")
plt.grid()


plt.subplot(4,2,6)
plt.plot(x7,ynumrk7con[:,0],"g")
plt.title("Posición Vs. Tiempo RK2 + rozamiento")
plt.grid()


plt.subplot(4,2,7)
plt.plot(x4,yeul[:,0])
plt.title("Posición Vs. Tiempo Euler")
plt.grid()


plt.subplot(4,2,8)
plt.plot(x8,ynumrk8con[:,0],"g")
plt.title("Posición Vs. Tiempo Euler + rozamiento")
plt.grid()

########################################################

plt.figure(2,figsize=(8,14))
plt.grid()


plt.subplot(4,2,1)
plt.plot(x,ynumrk4[:,1])
plt.title("Velocidad Vs. Tiempo RK4")
plt.grid()


plt.subplot(4,2,2)
plt.plot(x,ynumrk4con[:,1],"g")
plt.title("velocidad Vs. Tiempo RK4 + rozamiento")
plt.grid()


plt.subplot(4,2,3)
plt.plot(x3,ynumrk3[:,1])
plt.title("velocidad Vs. Tiempo RK3")
plt.grid()


plt.subplot(4,2,4)
plt.plot(x6,ynumrk6con[:,1],"g")
plt.title("velocidad Vs. Riempo RK3 + rozamiento")
plt.grid()


plt.subplot(4,2,5)
plt.plot(x3,ynumrk2[:,1])
plt.title("velocidad Vs. Tiempo RK2")
plt.grid()


plt.subplot(4,2,6)
plt.plot(x7,ynumrk7con[:,1],"g")
plt.title("Velocidad Vs. Tiempo RK2 + rozamiento")
plt.grid()


plt.subplot(4,2,7)
plt.plot(x4,yeul[:,1])
plt.title("velocidad Vs. Tiempo Euler")
plt.grid()


plt.subplot(4,2,8)
plt.plot(x8,ynumrk8con[:,1],"g")
plt.title("Velocidad Vs. Tiempo Euler + rozamiento")
plt.grid()


