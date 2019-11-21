from math import *

# Calcul des réactions et moments d'une poutre continue

largrPont=input("Entrez la largeur du pont en m : ")
largrPont=float(largrPont)
q=9*largrPont
p=q*10
mMax=0.1*p*1000
sigmaB=12

# Calcul de la poutre principale

c=sqrt(8*mMax/4/sigmaB)
print("Le côté de la poutre est de : ",c," cm")
print("Les barres de 4 cm sont espacées de ",c/12," cm")

# Recalcul du côté de la poutre avec le poids propre

q2=240*6*c
q=q+q2
p=p*10
mMax=0.1*p*1000
c=sqrt(8*mMax/4/sigmaB)
       
print("Le côté de la poutre est de : ",c," cm")
print("Les barres de 4 cm sont espacées de ",c/12," cm")


             
print("FINI")
