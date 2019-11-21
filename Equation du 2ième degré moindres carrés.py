from math import *

# Etablissement d'une équation de secon degré par la méthode des moindres carrés
# y = ax2 + bx +c    a=?  b=?  c=?

sxi,xi2,xi3,xi4,syi,yixi,yixi2=0,0,0,0,0,0,0

n=input("Nombre de points : ")
n=int(n)
i=0
while i<n:
    print("Entrez le point x",i+1)
    xi=input("Entrez xi : ")
    xi=float(xi)
    sxi=sxi+xi
    xi2=xi2+xi*xi
    xi3=xi3+xi**3
    xi4=xi4+xi**4
    
    print("Entrez le point y",i+1)
    yi=input("Entrez yi : ")
    yi=float(yi)
    syi=syi+yi
    yixi=yixi+yi*xi
    yixi2=yixi2+yi*xi*xi
    i=i+1

a11,a12,a13=xi4,xi3,xi2
a21,a22,a23=xi3,xi2,sxi
a31,a32,a33=xi2,sxi,n
lam1,lam2,lam3=yixi2,yixi,syi

deltaP=a11*(a22*a33-a32*a23)-a12*(a21*a33-a31*a23)+a13*(a21*a32-a31*a22)
if deltaP==0:
    print("L'équation n'a pas de solution")
else:
    deltaA=lam1*(a22*a33-a32*a23)-lam2*(a12*a33-a32*a13)+lam3*(a12*a23-a22*a13)
    a=deltaA/deltaP
    deltaB=a11*(lam2*a33-lam3*a23)-lam1*(a21*a33-a31*a23)+a13*(a21*lam3-a31*lam2)
    b=deltaB/deltaP
    deltaC=a11*(a22*lam3-a32*lam2)-a12*(a21*lam3-a31*lam2)+lam1*(a21*a32-a31*a22)
    c=deltaC/deltaP
    print("L'équation est Y= ",a," X2 + ",b," X + ",c)
            
print("FINI")
