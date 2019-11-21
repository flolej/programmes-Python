from math import *

# Recherche des racines d'une équation du 5ième degré

coef5=input("Entrez le coefficient du 5ième degré : ")
coef5=int(coef5)
coef4=input("Entrez le coefficient du 4ième degré : ")
coef4=int(coef4)
coef3=input("Entrez le coefficient du 3ième degré : ")
coef3=int(coef3)
coef2=input("Entrez le coefficient du 2ième degré : ")
coef2=int(coef2)
coef1=input("Entrez le coefficient du 1ier degré : ")
coef1=int(coef1)
coef0=input("Entrez le terme indépendant : ")
coef0=int(coef0)

pas=10
i=-100
while i<100:
    y=coef5*i**5+coef4*i**4+coef3*i**3+coef2*i**2+coef1*i+coef0
    print("x= ",i,"// y= ",y,"// Pas= ",pas)
    div=input("retour et division du pas par 10 = 'r' ou sinon 'Enter' ")
    if div=="r":
        i=i-1.1*pas
        pas=pas/10
    i=i+pas
             
print("FINI")
