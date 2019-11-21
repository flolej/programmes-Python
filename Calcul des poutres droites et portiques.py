from math import *

# Calcul des poutres droites et portiques encastrés

limElast=input("Entrez la limite élastique de l'acier en kN/cm2 : ")
limElast=float(limElast)
coefSecu=input("Entrez le coefficient de sécurité : ")
coefSecu=float(coefSecu)
sigma=limElast/coefSecu
poutre=input("Choisissez le calcul : 1-Poutres droites ou 2-Portiques encastrés : ")
poutre =int(poutre)
if poutre==1:
    print("Vous avez choisi le calcul d'une poutre droite sur appuis")
    appuis=input("Appuis : 1)simples -  2)2encastrem - 3)1 appuis+1 encastrem - 4)1 encastrem : ")
    appuis=int(appuis)
    charge=input("La charge est 1)ponctuelle - 2)uniformément répartie : ")
    charge=int(charge)
    if appuis==1 and charge==1:
        f=input("Entrez l'effort centré en kN : ")
        f=float(f)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=f*lgr/4
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=f*lgr**3/48/21000/fleche
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",f*lgr**3/48/21000/ix2," cm") 


    if appuis==2 and charge==1:
        f=input("Entrez l'effort centré en kN : ")
        f=float(f)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=f*lgr/8
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=f*lgr**3/192/21000/fleche
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",f*lgr**3/192/21000/ix2," cm") 

    if appuis==3 and charge==1:
        f=input("Entrez l'effort centré en kN : ")
        f=float(f)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=f*lgr/32
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm3 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=f*lgr**3/48/21000/fleche/sqrt(5)
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",f*lgr**3/48/21000/ix2," cm")

    if appuis==4 and charge==1:
        f=input("Entrez l'effort centré en kN : ")
        f=float(f)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=f*lgr
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=f*lgr**3/3/21000/fleche
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",f*lgr**3/3/21000/ix2," cm")

    if appuis==1 and charge==2:
        q=input("Entrez l'effort uniformément réparti en kN/cm : ")
        q=float(q)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=q*lgr*lgr/8
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre en cm3 : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=5*q*lgr**4/384/21000/fleche
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",5*q*lgr**4/384/21000/ix2," cm")

    if appuis==2 and charge==2:
        q=input("Entrez l'effort uniformément réparti en kN/cm : ")
        q=float(q)
        lgr=input("Entrez la longeur du portique en cm : ")
        lgr=float(lgr)
        momFlech=q*lgr*lgr/12
        iSv=momFlech/sigma
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        iSv2=input("Entrez le I/v de la poutre en cm3 : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=q*lgr**4/384/21000/fleche
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",q*lgr**4/384/21000/ix2," cm")

    if appuis==3 and charge==2:
        q=input("Entrez l'effort uniformément réparti en kN/cm : ")
        q=float(q)
        lgr=input("Entrez la longeur du portique en cm : ")
        lgr=float(lgr)
        momFlech=9*q*lgr*lgr/128
        iSv=momFlech/sigma
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        iSv2=input("Entrez le I/v de la poutre en cm3 : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=q*lgr**4/192/21000/fleche
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",q*lgr**4/192/21000/ix2," cm")

    if appuis==4 and charge==2:
        q=input("Entrez l'effort uniformément réparti en kN/cm : ")
        q=float(valCharge)
        lgr=input("Entrez la longeur de la poutre en cm : ")
        lgr=float(lgr)
        momFlech=q*lgr*lgr/2
        iSv=momFlech/sigma
        print("Le I/v de la poutre doit être supérieur à ",iSv," cm3")
        iSv2=input("Entrez le I/v de la poutre : ")
        iSv2=float(iSv2)
        ix=input("Entrez le moment d'inertie de la poutre en cm4 : ")
        ix=float(ix)
        fleche=lgr/350
        ix2=q*lgr**4/8/21000/fleche
        print("Le Ix de la poutre doit être supérieur à ",ix2," cm4")
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        print("La flèche est de :",q*lgr**4/8/21000/ix2," cm")

        

if poutre==2:
    print("Vous avez choisi le calcul d'un portique simple encastré à la base avec I1=I2")
    charge=input("La charge est 1)ponctuelle centrée - 2)ponctuelle à gauche - 3)uniformément répartie - 4)uniformément répartie à gauche ")
    charge=int(charge)
    if charge==1:
        p=input("Entrez l'effort centré en kN : ")
        p=float(p)
        lgr=input("Entrez la longueur du portique en cm : ")
        lgr=float(lgr)
        haut=input("Entrez la hauteur du portique en cm : ")
        haut=float(haut)
        k=haut/lgr
        alpha=1/(k+2)
        momFlech=alpha*p*lgr/4
        iSv=momFlech/sigma
        print("Le I/v minimum est de ",iSv," cm3")
        iSv2=input("Entrez le I/v en cm3 : ")
        iSv2=float(iSv2)
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        

    if  charge==2:
        f=input("Entrez l'effort centré en kN : ")
        f=float(f)
        lgr=input("Entrez la longueur du portique en cm : ")
        lgr=float(lgr)
        haut=input("Entrez la hauteur du portique en cm : ")
        haut=float(haut)
        k=haut/lgr
        alpha=-0.0115*k+0.363
        momFlech=alpha*f*haut
        iSv=momFlech/sigma
        print("Le I/v minimum est de ",iSv," cm3")
        iSv2=input("Entrez le I/v en cm3 : ")
        iSv2=float(iSv2)
        print("La tension est de : ",momFlech/iSv2," kN/cm2")


    if charge==3:
        q=input("Entrez l'effort uniform réparti en kN/cm : ")
        q=float(q)
        lgr=input("Entrez la longueur du portique en cm : ")
        lgr=float(lgr)
        haut=input("Entrez la hauteur du portique en cm : ")
        haut=float(haut)
        k=haut/lgr
        alpha=4/3/(k+2)
        momFlech=alpha*q*lgr**2/8
        iSv=momFlech/sigma
        print("Le I/v minimum est de ",iSv," cm3")
        iSv2=input("Entrez le I/v en cm3 : ")
        iSv2=float(iSv2)
        print("La tension est de : ",momFlech/iSv2," kN/cm2")

    if charge==4:
        q=input("Entrez l'effort uniform réparti à gauche en kN/cm : ")
        q=float(q)
        lgr=input("Entrez la longeur du portique en cm : ")
        lgr=float(lgr)
        haut=input("Entrez la hauteur du portique en cm : ")
        haut=float(haut)
        k=haut/lgr
        alpha=-0.181*k+0.523
        momFlech=alpha*q*haut**2/2
        iSv=momFlech/sigma
        print("Le I/v minimum est de ",iSv," cm3")
        iSv2=input("Entrez le I/v en cm3 : ")
        iSv2=float(iSv2)
        print("La tension est de : ",momFlech/iSv2," kN/cm2")
        
                               
print("FINI")
