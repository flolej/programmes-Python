from math import *

# Etablissement d'une équation de secon degré
# y = ax2 + bx +c    a=?  b=?  c=?

a=0
b=0
c=0


x1=input("Enrez x1 : ")
x1=float(x1)
y1=input("Entrez y1 : ")
y1=float(y1)
x2=input("Enrez x2 : ")
x2=float(x2)
y2=input("Entrez y2 : ")
y2=float(y2)
x3=input("Enrez x3 : ")
x3=float(x3)
y3=input("Entrez y3 : ")
y3=float(y3)

a=(y3*(x2-x1)-y2*x3-y1*(x2-x1))/(x3*x3*x2-x3*x3*x1-x2*x2*x3+x1*x1*x3-x1*x1*x2+x1**3)
b=(y2-a*(x2*x2-x1*x1))/(x2-x1)
c=y1-a*x1*x1-b*x1

print("L'equation est Y = ",a,"X2 + ",b,"X + ",c)

             
print("FINI")
