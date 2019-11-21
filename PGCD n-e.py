from math import *

# Recherche des racines d'une équation

delta=0.0001
i=1
while i<100 and i**5+i**4-7*i**3-22*i**2+i+1<delta:
    i=i+delta

print("La racine est ",i)
    
    

print("FINI")
