
#Definici�n de funciones
import numpy as np
import matplotlib.pyplot as plt


def funcomp(x,y):
    dydx=np.array(((0.025-0.005*y[0])-8*10**12*np.exp(-22500/(1.987*y[1]))*y[0],(0.005)*(300-y[1])+8*10**13*(np.exp(-22500/(1.987*y[1]))*y[0])-(1*10**-3)*(y[1]-330)))
    return dydx
    
    
def meulermj(xi,yi,h,f):
    x=xi+h
    y1=yi+h*f(xi,yi)
    y2=yi+h*((f(xi,yi)+f(x,y1))/2)
    
    return(x,y2)

def rk3(xi,yi,h,f):
    x=xi+h
    k1=h*f(xi,yi)
    k2=h*f(xi+0.5*h,yi+0.5*k1)
    k3=h*f(xi+h,yi-k1+2*k2)
    y=yi+(k1+4*k2+k3)/6
    
    return (x,y)


#Calcule la temperatura T y la concentraci�n Ca

f=10 #ml/s #Gasto de alimentaci�n al reactor
v=2000 #ml #Volumen del reactor
cao=5 #gmol/L #Concentracion del reactante A en el flujo de alimentaci�n
To=300 #k #Temperatura del flujo de alimentaci�n
H=-10000#cal/gmol #Calor de reacci�n
U=100 #Cal/�Csm2 #Coeficiente global de transmisi�n de calor 
A=0.02#�rea de transmisi�n de calor 
Ti=330#k
Cp=1 #Calor espec�fico 
p=1 #Peso espec�fico 

xi=0
yi=5
yi1=300

xf=4000
n=10000
h=(xf-xi)/(n-1)

#M�todo de euler mejorado
x=np.zeros(n)
ynum=np.zeros(shape=(n,2))#Matriz soluci�n

#Valor inicial

yi=np.array([5,300])

ynum[0,0]=yi[0]
ynum[0,1]=yi[1]

for i in range(1,n):
    x[i],ynum[i,:]=meulermj(x[i-1],ynum[i-1,:],h,funcomp)
    
#M�todo de rk3
x3=np.zeros(n)
yrk3=np.zeros(shape=(n,2))#Matriz soluci�n

#Valor inicial

yrk3[0,0]=yi[0]
yrk3[0,1]=yi[1]

for i in range(1,n):
    x3[i],yrk3[i,:]=rk3(x3[i-1],yrk3[i-1,:],h,funcomp)
     
#Gr�ficos meuler mejorado
plt.figure(1,figsize=(17,8))
plt.subplot(1,2,1)
plt.plot(x,ynum[:,0],label="M�todo de euler mejorado")
plt.legend(loc="best")
plt.xlabel("Tiempo (s)")
plt.ylabel("Concentraci�n (gmol/L)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(x,ynum[:,1],label="M�todo de euler mejorado")
plt.legend(loc="best")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (k)")
plt.grid()

#Graficos rk3
plt.figure(2,figsize=(17,8))
plt.subplot(1,2,1)
plt.plot(x3,yrk3[:,0],label="Rk3")
plt.legend(loc="best")
plt.xlabel("Tiempo (s)")
plt.ylabel("Concentraci�n (gmol/L)")
plt.grid()

plt.subplot(1,2,2)
plt.plot(x3,yrk3[:,1],label="Rk3")
plt.legend(loc="best")
plt.xlabel("Tiempo (s)")
plt.ylabel("Temperatura (k)")
plt.grid()
print("Para el r�gimen permanente:\n")
print("Una concentaci�n de ", ynum[-1,0],"gmol/L")
print("Temperatura de ",ynum[-1,1],"K")

