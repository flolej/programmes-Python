from math import *

print("Calcul de PI par la méthode... : ")
n=50
pi2=0
pi2=float(pi2)
k=0
while k<=n:
    pi1=(2**k*(factorial(k)**2/factorial(2*k+1)))
    pi2=pi2+pi1
    k=k+1
print("...de Euler     : ",2*pi2)

pi2=0.0
k=0
while k<40:
    pi1=(-1)**k/(2*k+1)/3**k
    pi2=pi2+pi1
    k=k+1
print("...de Leibniz   : ",sqrt(12)*pi2)

pi1=log(640320**3+744)/sqrt(163)
print("...de Heegner   : ",pi1)

pi1=355/113*(1-0.0003/3533)
print("...de Ramanujan : ",pi1)

pi1=24*atan(1/8)+8*atan(1/57)+4*atan(1/239)
print("...de Machin    : ",pi1)

pi1=4*(12*atan(1/49)+32*atan(1/57)-5*atan(1/239)+12*atan(1/110443))
print("...de Yasumasa  : ",pi1)

print("...de Python    : ",pi)

print("FINI")
