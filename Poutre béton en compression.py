from math import *

f=input("Entrez la charge axiale en kN : ")
f=float(f)

c=-30+sqrt(900+2*f)
h=c/3/4
lMax=21*c

print("Le côté de la poutre est de : ",c," cm")
print("Distance maxi entre les armatures : ",h," cm")
print("La longueur maxi de la poutre : ",lMax," cm")

             
print("FINI")
