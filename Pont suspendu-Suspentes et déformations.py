from math import *

a,b,c=0,0,0

lgrPont=input("Entrez la longueur du pont en m : ")
lgrPont=float(lgrPont)
h=lgrPont/10
x1=0
y1=0
x2=lgrPont/2
y2=h
x3=lgrPont
y3=0

a=(y3*(x2-x1)-y2*x3-y1*(x2-x1))/(x3*x3*x2-x3*x3*x1-x2*x2*x3+x1*x1*x3-x1*x1*x2+x1**3)
b=(y2-a*(x2*x2-x1*x1))/(x2-x1)
c=y1-a*x1*x1-b*x1

# Calcul des allongements des suspentes sous l'effet de la t°

yi2=0
l=0
i=1
while i<61:
    xi=10*i
    yi=0.05*xi+0.0005*xi*xi
    l=(h-yi)*100
    deltaL=0.00012*l*35
    print("La longueur de la suspente ",i," est de ",l," cm")
    print("Et son deltaL(posit et négat) de 35° à la t° est de est de : ",deltaL," cm")
    input()
    i=i+1

# Longueur de la parabole

lgrL=0
i=1
while i<30001:
    yi=0.05*xi+0.0005*xi*xi
    xi2=xi+1
    yi2=0.05*xi+0.0005*xi2*xi2
    deltaY=yi2-yi
    deltaL=sqrt(1+deltaY**2)
    lgrL=lgrL+deltaL
    i=i+1
    lgrSuspPrinc=2*lgrL/100

print("La longueur de la suspente principales est ",lgrSuspPrinc," cm")
print("Et son allongement sous t° est de :",0.0007272*lgrSuspPrinc," cm")

# Calcul des réactions et moments de la poutre continue

largrPont=input("Entrez la largeur du pont en m : ")
largrPont=float(largrPont)
q=9*largrPont/2
p=q*5
mMax=0.1*p*1000
sigmaB=12

# Calcul de la poutre principale

c=sqrt(8*mMax/4/sigmaB)

# Recalcul du côté de la poutre avec le poids propre

print("Recalcul de la poutre avec le poids propre")

q2=240*6*c
q=q+q2
p=q*5
mMax=0.1*p*1000
c=sqrt(8*mMax/4/sigmaB)
       
print("Le côté de la poutre est de : ",c," cm")
print("Les barres de 4 cm sont espacées de ",c/12," cm")

# Allongement des suspentes sous charge

ri=(9*largrPont/2)+(24*c*c/10000)
print("Le diamètre des suspentes est de : ",sqrt(ri)/3.07," cm")
l=0
i=1
while i<61:
    xi=50*i
    yi=0.05*xi+0.0005*xi*xi
    l=(h-yi)*50
    deltaL=0.00012*l*35
    a=50*lgrPont/16500+deltaL
    print("L'allongement de la suspentes ",i," sous q+poids propre est de : ",a," cm")
    input()
    i=i+1

# calcul de la charge sur le pilier de rive : fc=f x cos(alpha)

f=q*5
fc=0.26*q*5
print("L'effort de compression sur le pilier de rive est de ",fc," kN")

              
print("FINI")
