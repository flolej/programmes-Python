from math import *

# Flambage de poutres chargées par une force transversale centrée suivant YY (précalcul rapide)

limElast=input("Entrez la limite élastique en kN/cm2 : ")
limElast=float(limElast)
coefSecu=input("Entrez le coefficien de sécurité : ")
coefSecu=float(coefSecu)
sigma=limElast/coefSecu
p=input("Entrez la charge de flambage : ")
p=float(p)
s=p/sigma
chT=input("La charge tranversale est 1:ponctuelle - 2:uniform répartie : ")
chT=int(chT)
if chT==1:
    f=input("Entrez la charge tranversale ponctuelle en kN : ")
    f=float(f)
    if f==0:
        f=0.00001
if chT==2:
    q=input("Entrez la charge tranversale uniform répartie en kN/m : ")
    q=float(q)
    if q==0:
        q=0.00001
print("La section approchée de la poutre est de ",s," cm2")

s=input("Entrez la section de la poutre en cm2 : ")
s=float(s)
sigma=p/s
iy=input("Entrez le moment d'inertie Iy en cm4 : ")
iy=float(iy)
iySv=input("Entrez le Iy/v de la poutre en cm3 : ")
iySv=float(iySv)
longr=input("Entrez la longueur de la poutre en cm : ")
longr=float(longr)
r=input("Entrez les appuis : 1=1 encastr ; 2=2 encastr ; 3=sur rotules ; 4=encast+rotule : ")
r=int(r)
iy2=iy
if chT==1 and r==1:
     mf=f*longr/2
     fl=f*longr**3/8/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=2
     lk=longr*k
if chT==1 and r==2:
     mf=f*longr/8
     fl=f*longr**3/192/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=0.5
     lk=longr*k
if chT==1 and r==3:
     mf=f*longr/4
     fl=f*longr**3/48/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=1
     lk=longr*k
if chT==1 and r==4:
     mf=5*f*longr/32
     fl=f*longr**3/107/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=0.7
     lk=longr*k
if chT==2 and r==1:
     mf=q*longr*longr/2
     fl=q*longr**4/8/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=2
     lk=longr*k
if chT==2 and r==2:
     mf=q*longr*longr/24
     fl=q*longr**3/384/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=0.5
     lk=longr*k
if chT==2 and r==3:
     mf=q*longr*longr/8
     fl=5*q*longr**3/384/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=l
     lk=longr*k
if chT==2 and r==4:
     mf=q*longr*longr/14
     fl=q*longr**3/185/21500/iy
     rap=longr/fl
     if rap<350:
         print("Le rapport longr/flèche de ",rap," est trop faible") 
         iy=f*longr**2/491
         print("Iy = ",iy)
         iy2=input("Entrez un iy supérieur en cm4 : ")
         iy2=float(iy2)
         s=input("Entrez la nouvelle section en cm2 : ")
         s=float(s)
     k=0.7
     lk=longr*k

# Vérification

rho=sqrt(iy2/s)
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
sigma=p/khi/s
print("La tension = ",sigma," kN/cm2")
fEy=215000*iy/lk/lk
flèche=fl*(1-fl/fEy)
print("La flèche approximative est de ",flèche," cm")
                               
print("FINI")
