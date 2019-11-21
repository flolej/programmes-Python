from math import *

# Flexion-déversement des poutres T, L, U, I : charge de sécurité

limElast=input("Entrez la limité élastique de l'acier en kN/cm2 : ")
limElast=float(limElast)
coefSecu=input("Entrez le coefficient de sécurité : ")
coefSecu=float(coefSecu)
sigma=limElast/coefSecu
charge=input("La charge est 1:ponctuelle - 2: uniform répartie : ")
charge=int(charge)
appuis=input("Entrez les appuis : 1=2 rotules - 2=1 encastr - 3=2 encast - 4=1 encast+1 rotule : ")
appuis=int(appuis)
lgr=input("Entrez la longeur de la poutre en cm : ")
lgr=float(lgr)

if charge==1:
    f=input("Entrez la force sur la poutre en kN : ")
    f=float(f)
if charge==2:
    q=input("Entrez la charge unif répartie sur la poutre en kN/cm : ")
    q=float(q)

if appuis==1 and charge==1:
    momFlech=f*lgr/4
if appuis==1 and charge==2:
    momFlech=q*lgr*lgr/8
if appuis==2 and charge==1:
    momFlech=f*lgr
if appuis==2 and charge==2:
    momFlech=q*lgr*lgr/2
if appuis==3 and charge==1:
    momFlech=f*lgr/8
if appuis==3 and charge==2:
    momFlech=q*lgr*lgr/12
if appuis==4 and charge==1:
    momFlech=5*f*lgr/32
if appuis==4 and charge==2:
    momFlech=q*lgr*lgr/14
    
ixSv=momFlech/sigma
print("Le Ix/v doit être supérieur à : ",ixSv," cm3")
ixSv=input("Entrez le Ix/v du profil choisi en cm3 : ")
ixSv=float(ixSv)
iySv=input("Entrez le Iy/v du profil en cm3 : ")
iySv=float(iySv)
s=input("Entrez la section du profil en cm2 : ")
s=float(s)
ix=input("Entrez le ix du profil en cm4 : ")
ix=float(ix)
iy=input("Entrez le iy du profil en cm4 : ")
iy=float(iy)

if appuis==1 and charge==1:
    k=1
    fleche=f*lgr**3/48/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=f*lgr**3/48/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==1 and charge==2:
    k=1
    fleche=q*lgr**4/77/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=q*lgr**4/77/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==2 and charge==1:
    k=2
    fleche=f*lgr**3/3/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=f*lgr**3/3/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==2 and charge==2:
    k=2
    fleche=q*lgr**4/8/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=q*lgr**4/8/21500/fleche
        print("Le Ix mini est de : ",ix, " cm4")
if appuis==3 and charge==1:
    k=0.5
    fleche=f*lgr**3/192/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=f*lgr**3/192/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==3 and charge==2:
    k=0.5
    momFlech=q*lgr*lgr/12
    fleche=q*l**4/384/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=q*l**4/384/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==4 and charge==1:
    k=0.7
    fleche=f*lgr**3/107/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=f*lgr**3/107/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")
if appuis==4 and charge==2:
    k=0.7
    fleche=q*lgr**4/192/21500/ix
    if fleche>lgr/350:
        print("La flèche est trop élevée")
        ix=q*lgr**4/192/21500/fleche
        print("Le Ix mini est de : ",ix," cm4")

print("Remarque : les profils sont disposés selon leur Ixx")

fer=input("Entrez le type de profil 1:T - 2:U - 3:L - 4:I : ")
fer=int(fer)
larg=input("Entrez la largeur de l'aile en cm : ")
larg=float(larg)
haut=input("Entrez la hauteur du profil en cm : ")
haut=float(haut)
e=input("Entrez l'épaisseur des ailes en cm : ")
e=float(e)
ame=input("Entrez l'épaisseur de l'âme en cm : ")
ame=float(ame)

if fer==1:
    v=(haut*haut+larg*e*e-e*e)/2/(haut+larg-e)
    s=e*(haut+larg-e)
    ix1=e/3*(haut**3+larg*e*e-e**3)
    ix=ix1-s*v*v
    iy=e/12*(larg**3+(haut-e)*e*e)
    ixSv=ix/(haut-v)
    iySv=e*(larg**3+(haut-e)*e*e)/12
    i0=ix+iy
    it=e**3*(larg+haut-e)
    iw=((larg**3*e)+(haut-e)**3)/3

if fer==2:
    v=(2*haut*haut*e+(larg-2*e)*e*e)/2/(2*haut*e+(larg-2*e)*e)
    s=2*haut*e+(larg-2*e)*e**3
    ix1=(2*haut**3*e+(larg-2*e)*e**3)/3
    ix=ix1-s*v*v
    iy=(haut*larg**3-(haut-e)*(larg-2*e)**3)
    ixSv=ix/v
    iySv=iy/(haut-v)
    i0=ix+iy
    it=e**3/3*(2*larg+(haut-2*e))
    iw=((2*larg**3*e)+(haut-2*e)**3*e)/3

if fer==3:
    v=(haut*haut+haut*e-e*e)/2/(2*haut-e)
    s=e*(2*haut-e)
    ix=e*(haut**3+(haut-e)*e*e-s*v*v)
    iy=ix
    ixSv=ix/v
    iySv=ixSv
    iF=(haut**4-(haut-e)**4)/12
    iD=iF-(haut*haut*(haut-e)**2*e)/2/(2*haut-e)
    i0=iF+iD
    it=e**3/3*(2*larg-e)
    iw=e/3*(larg**3+larg-e)**3

if fer==4:
    v=haut/2
    s=2*larg*e+(haut-2*e)*ame
    ix=2*(larg*e*(haut/2)**2)+haut/2*ame*(haut/4)**2
    iy=larg**3*e/8
    ixSv=2*ix/haut 
    iySv=2*iy/larg
    i0=ix+iy
    it=(2*larg*e**3+(haut-2*e)*ame**3)/3
    iw=haut**2*ix/4

print("La section est de ",s," cm2")
print("ix = ",ix," cm4")
print("iy = ",iy," cm4")
print("Ix/v = ",ixSv," cm3")
print("Iy/v = ",iySv," cm3")
print("i0 (Inertie polaire) = ",i0," cm4")
print("it (Inertie de torsion) = ",it," cm4")
print("iw (Inertie de gauchissement) = ",iw," cm4")

Lk=k*lgr
fCrit=2650*s/i0*(lgr*it+27*iw/Lk/Lk)
tensionFlex=momFlech/ixSv
print("La tension de flexion = ",tensionFlex," kN/cm2")
if tensionFlex>limElast:
    ixSv=momFlech/limElast
    print("La tension est trop élevée, choisissez un Ix/v > à ",ixSv)

print("Vérification au déversement")

iySv=iy/larg/2

print("Le moment fléchissant de flexion = ",momFlech," kN.cm")
it=(2*larg*e**3+(haut-2*e)*ame**3)/3
momCrit=10750*iySv*haut/2/lgr/lgr*sqrt((haut-e)**2+1.51*lgr*lgr*it/iySv*larg/2)
print("Le mom fléch de déversement critique élastique = ",momCrit," kN.cm")
                 
print("FINI")
