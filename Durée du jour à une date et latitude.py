from math import *

# Calcul de la durée du jour à une latitude donnée

print("Calcul de la durée du jour à une latitude donnée")
print("Chosissez un endroit approximatif : ")
endroit=input("1 : Arctique Nord (Inuit : habité) - 2 : Arctique Sud (Mourminsk : habité) : 3 : Stockholm - 4 : Belgique - 5 : Paris - 6 : Lyon - 7 : Marseille - 8 : Valence - 9 : Madrid - 10 : Alger - 11 : Senegal : ")
endroit=int(endroit)
if endroit==1:
    lat=67.151742
    ville="Arctique Nord (Inuit : habité)"
if endroit==2:
    lat=66.55
    ville="Arctique Sud (Mourmisk : habité)"
if endroit==3:
    lat=59.77
    ville="Stockholm"
if endroit==4:
    lat=50.8466
    ville="Belgique"
if endroit==5:
    lat=48.8534
    ville="Paris"
if endroit==6:
    lat=45.75
    ville="Lyon"
if endroit==7:
    lat=43.3
    ville="Marseille"
if endroit==8:
    lat=39.4698
    ville="Valence"
if endroit==9:
    lat=37.7167
    ville="Madrid"
if endroit==10:
    lat=36.7529
    ville="Alger"
if endroit==11:
    lat=17.533
    ville="Sénégal"
an=input("Entrez l'année (>2012) : ")
an=int(an)
mois=input("Entrez le n° du mois : ")
mois=int(mois)
jour=input("Entrez le n° du jour : ")
jour=int(jour)

jP=(an-2013)*365.25+mois*30.44+jour
deltaDeg=(0.38+23.26*sin((2*pi*jP/365.24)-1.395))+(0.395+0.375*sin((4*pi*jP/365.24)-1.47))
delta=pi*deltaDeg/180
lamb=pi*lat/180
dJ=(24*(1-acos(tan(delta)*tan(lamb))/pi))+0.5
dJheures=int(dJ)
dJmin=int((dJ-dJheures)*60)

print("La durée du jour le",jour,mois,an,"à",ville,"est de",dJheures,"heure(s)",dJmin,"minute(s)")
                
print("FINI")
