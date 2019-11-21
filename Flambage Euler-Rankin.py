from math import *

# Flambage de poutres chargées

lgr=input("Entrez la longeur de la poutre en cm : ")
lgr=float(lgr)
appuis=input("Entrez les appuis : 1=2 rotules - 2=1 rotule+1 encastrem - 3=2 ancastr - 4=1 rotule : ")
appuis=int(appuis)
if appuis==1:
    k=1
if appuis==2:
    k=0.7
if appuis==3:
    k=0.5
if appuis==4:
    k=2
lk=k*lgr
f=input("Entrez la force de flambage en kN : ")
f=float(f)
rayGir=lk/91
print("Le rayon de giration mini est de ",rayGir," cm")
rayGir=input("Entrez le nouveau rayon de giration en cm : ")
rayGir=float(rayGir)
s=input("Entrez la section du profil en cm2 : ")
s=float(s)
sigma=f/s
print("La tension de compression est de : ",sigma," kN/cm2")
print("Vérification")

# Vérification

iy=input("Entrez le Iy en cm4 : ")
iy=float(iy)
rho=sqrt(iy/s)
lam=lk/rho
lamReel=lam/96
if lamReel<=0.2:
    khi=1
alpha=0.1*lamReel**2-0.64*lamReel+1.12
if alpha<=0.2:
    alpha=1
if alpha>=3:
    alpha=0.1
phi=0.5*(lamReel**2+alpha*(lamReel-0.2)+1)
khi=1/(phi+sqrt(phi**2-lamReel**2))
if khi>1:
    khi=1
sigma=f/khi/s
print("La tension de flambage est de ",sigma," kN/cm2")
                               
print("FINI")
