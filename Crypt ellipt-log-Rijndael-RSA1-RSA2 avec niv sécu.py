from math import *
import random
randInf=1019
randSup=4813

nbrPrem=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,1013,1019,1021,1031,1033,1039,1049,1051,1061,1063,1069,1087,1091,1093,1097,1103,1109,1117,1123,1129,1151,1153,1163,1171,1181,1187,1193,1201,1213,1217,1223,1223,1229,1231,1237,1249,1259,1277,1279,1283,1289,1291,1297,1301,1303,1307,1319,1321,1327,1361,1367,1373,1381,1399,1409,1423,1427,1429,1433,1439,1447,1451,1453,1459,1471,1481,1483,1487,1489,1493,1499,1511,1523,1531,1543,1549,1553,1559,1567,1571,1579,1583,1597,1601,1607,1609,1613,1619,1621,1627,1637,1657,1663,1667,1669,1693,1697,1699,1709,1721,1723,1733,1741,1747,1753,1759,1777,1783,1787,1789,1801,1811,1823,1831,1847,1861,1867,1871,1873,1877,1879,1889,1901,1907,1913,1931,1933,1949,1951,1973,1979,1987,1993,1997,1999,2003,2011,2017,2027,2029,2039,2053,2063,2069,2081,2083,2087,2089,2099,2111,2113,2129,2131,2137,2141,2143,2153,2161,2179,2203,2207,2213,2221,2237,2239,2243,2251,2267,2269,2273,2281,2287,2293,2297,2309,2311,2333,2339,2341,2347,2351,2357,2371,2377,2381,2383,2389,2393,2399,2411,2417,2423,2437,2441,2447,2459,2467,2473,2477,2503,2521,2531,2539,2543,2549,2551,2557,2579,2591,2593,2609,2617,2621,2633,2647,2657,2659,2663,2671,2677,2683,2687,2689,2693,2699,2707,2711,2713,2719,2729,2731,2741,2749,2753,2767,2777,2789,2791,2797,2801,2803,2819,2833,2837,2843,2851,2857,2861,2879,2887,2897,2903,2909,2917,2927,2939,2953,2957,2963,2969,2971,2999,3001,3011,3019,3023,3037,3041,3049,3061,3067,3079,3083,3089,3109,3119,3121,3137,3163,3167,3169,3181,3187,3191,3203,3209,3217,3221,3229,3251,3253,3257,3259,3271,3299,3301,3307,3313,3319,3323,3329,3331,3343,3347,3359,3361,3371,3373,3389,3391,3407,3413,3433,3449,3457,3461,3463,3467,3469,3491,3499,3511,3517,3527,3529,3533,3539,3541,3547,3557,3559,3571,3581,3583,3593,3607,3613,3617,3623,3631,3637,3643,3659,3671,3673,3677,3691,3697,3701,3709,3719,3727,3733,3739,3761,3767,3769,3779,3793,3797,3803,3821,3823,3833,3847,3851,3853,3863,3877,3881,3889,3907,3911,3917,3919,3923,3929,3931,3943,3947,3967,3989,4001,4003,4007,4013,4019,4021,4027,4049,4051,4057,4073,4079,4091,4093,4099,4111,4127,4129,4133,4139,4153,4157,4159,4177,4201,4211,4217,4219,4229,4231,4241,4243,4253,4259,4261,4271,4273,4283,4289,4297,4327,4337,4339,4349,4357,4363,4373,4391,4397,4409,4421,4423,4441,4447,4451,4457,4463,4481,4483,4493,4507,4513,4517,4519,4523,4547,4549,4561,4567,4583,4591,4597,4603,4621,4637,4639,4643,4649,4651,4657,4663,4673,4679,4691,4703,4721,4723,4729,4733,4751,4759,4783,4787,4789,4793,4799,4801,4813]
# 4817	4831	4861	4871	4877	4889	4903	4909	4919	4931
# 4933	4937	4943	4951	4957	4967	4969	4973	4987	4993
# 4999	5003	5009	5011	5021	5023	5039	5051	5059	5077
# 5081	5087	5099	5101	5107	5113	5119	5147	5153	5167
# 5171	5179	5189	5197	5209	5227	5231	5233	5237	5261
# 5273	5279	5281	5297	5303	5309	5323	5333	5347	5351
# 5381	5387	5393	5399	5407	5413	5417	5419	5431	5437
# 5441	5443	5449	5471	5477	5479	5483	5501	5503	5507
# 5519	5521	5527	5531	5557	5563	5569	5573	5581	5591
# 5623	5639	5641	5647	5651	5653	5657	5659	5669	5683
# 5689	5693	5701	5711	5717	5737	5741	5743	5749	5779
# 5783	5791	5801	5807	5813	5821	5827	5839	5843	5849
# 5851	5857	5861	5867	5869	5879	5881	5897	5903	5923
# 5927	5939	5953	5981	5987	6007	6011	6029	6037	6043
# 6047	6053	6067	6073	6079	6089	6091	6101	6113	6121

nbrPremMax=nbrPrem[-1]
lgrNbrPrem=len(nbrPrem)

print("Entrez ci-dessous le système de cryptage puis 'enter'")
sys=input("1 = Logarithmique, 2 = Rijndael, 3 = RSA : ") 
sys=int(sys)

choix=""
choix=input("Crypter = 'c' - Décrypter = 'd' : ")

if sys==1 and choix=="c":
    text=""
    text=input("Entrez le texte à crypter sans CR : ")
    lgrText=len(text)
    
    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)
    
    textCrypt=[]    
    i=0
    while i<lgrText:
        chifCrypt=ord(text[i])
        textCrypt.append(chifCrypt)
        i=i+1
    lgrTextCrypt=len(textCrypt)

    if nivSecu==3:
        i=0
        while i<lgrTextCrypt:
            ordText=int(ord(text[i])+nivSecu*i)
            textCrypt[i]=int(round(exp((64/9*ordText*log(ordText))**(1/3))))        
            i=i+1
    if nivSecu==4:
        i=0
        while i<lgrTextCrypt:
            ordText=int(ord(text[i])+nivSecu*i)
            textCrypt[i]=int(round(exp((64/9*ordText*log(ordText))**(1/3))))        
            i=i+1
    if nivSecu==5:
        i=0
        while i<lgrTextCrypt:
            ordText=int(ord(text[i])+nivSecu*i)
            textCrypt[i]=int(round(exp((64/9*ordText*log(ordText))**(1/3))))        
            i=i+1
    if nivSecu==6:
        i=0
        while i<lgrTextCrypt:
            ordText=int(ord(text[i])+nivSecu*i)
            textCrypt[i]=int(round(exp((64/9*ordText*log(ordText))**(1/3))))        
            i=i+1
    if nivSecu==7:
        i=0
        while i<lgrTextCrypt:
            ordText=int(ord(text[i])+nivSecu*i)
            textCrypt[i]=int(round(exp((64/9*ordText*log(ordText))**(1/3))))        
            i=i+1

    lgrTextCrypt=len(textCrypt)
    textCrypt2=""
    i=0
    while i<lgrTextCrypt:
        textCrypt2=textCrypt2+str(textCrypt[i])+","
        i=i+1

    f=open("textCrypt.txt","w")
    f.write(textCrypt2)
    f.close()
                
    print("Le texte crypté est dans le fichier textCrypt")
    input()

if sys==2 and choix=="c":
    text=input("Entrez le texte à crypter puis 'enter' : ")
    text=list(text)
    lgrText=len(text)

    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)
    
    ordText=[]
    i=0
    while i<lgrText:
        ordText.append(ord(text[i]))
        i=i+1
    text=ordText
   
    # Génération du PW original
    pw=[]
    i=0
    while i<lgrText:
        pw.append(random.randint(randInf,randSup))
        i=i+1
    lgrPw=len(pw)
    
    # Génération des 16 PW pour les 16 rondes
    # Première partie
    
    pw01=[]
    i=0
    while i<lgrPw:
        pw01.append(pw[i]+nivSecu*580)
        i=i+1
    pw02=[]
    i=0
    while i<lgrPw:
        pw02.append(pw01[i]+nivSecu*590)
        i=i+1
    pw03=[]
    i=0
    while i<lgrPw:
        pw03.append(pw02[i]+nivSecu*600)
        i=i+1
    pw04=[]
    i=0
    while i<lgrPw:
        pw04.append(pw03[i]+nivSecu*610)
        i=i+1
    pw05=[]
    i=0
    while i<lgrPw:
        pw05.append(pw04[i]+nivSecu*620)
        i=i+1
    pw06=[]
    i=0
    while i<lgrPw:
        pw06.append(pw05[i]+nivSecu*630)
        i=i+1
    pw07=[]
    i=0
    while i<lgrPw:
        pw07.append(pw06[i]+nivSecu*640)
        i=i+1
    pw08=[]
    i=0
    while i<lgrPw:
        pw08.append(pw07[i]+nivSecu*650)
        i=i+1
    
    # Deuxième partie
    pw01.reverse()
    pw09=pw01
    pw02.reverse()   
    pw10=pw02
    pw03.reverse()    
    pw11=pw03
    pw04.reverse()    
    pw12=pw04
    pw05.reverse()   
    pw13=pw05
    pw06.reverse()    
    pw14=pw06
    pw07.reverse()    
    pw15=pw07
    pw08.reverse()    
    pw16=pw08
                 
    # Les 16 rondes

    def rondes(lgrText,text,pw01):
       i=0
       while i<lgrText:
           text[i]=text[i]+pw01[i]
           i=i+1 
    
    rondes(lgrText,text,pw01)
    rondes(lgrText,text,pw02)
    rondes(lgrText,text,pw03)
    rondes(lgrText,text,pw04)
    rondes(lgrText,text,pw05)
    rondes(lgrText,text,pw06)
    rondes(lgrText,text,pw07)
    rondes(lgrText,text,pw08)
    rondes(lgrText,text,pw09)
    rondes(lgrText,text,pw10)
    rondes(lgrText,text,pw11)
    rondes(lgrText,text,pw12)
    rondes(lgrText,text,pw13)
    rondes(lgrText,text,pw14)
    rondes(lgrText,text,pw15)
    rondes(lgrText,text,pw16)
    
    f=open("pwCrypt","w")
    f.write(str(pw))
    f.close()
    f=open("textCrypt","w")
    f.write(str(text))
    f.close()

    print("Le PW et le texte crypté sont dans les fichiers 'pwCrypt.txt' et 'textCrypt.txt'")
    input()

if sys==3 and choix=="c":
    p=121343
    q=652153
    n=p*q
    phi=(p-1)*(q-1)        

    # Calcul du pgcd (e,phi) avec (3 < e < phi)
    pgcd=q-1
    flag=0
    x=int((q-1)/2)
    e=q-2
    while e>3 and e<q-1:
        i=4
        while i>3 and i<x:
            if phi%i==0:              
                if e%i==0:
                    pgcd=i
                    flag=1
                    i=3 
            i=i+1
            if flag==1:
                e=3
            e=3
        e=e-1
    e=pgcd
    pw=input("Entrez un mot de passe puis 'enter' : ")
    lgrPw=len(pw)
    pw2=0
    i=0
    while i<lgrPw:
        pw2=pw2+ord(pw[i])
        i=i+1
    pw1=int(e*pw2)
    text=""
    text=input("Entrez le texte à crypter sans CR puis 'enter' : ")
    lgrText=len(text)
    text2=""

    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)
    
    i=0
    while i<lgrText:
        if ord(text[i])<32:
            text2=text2+" "
        else:
            text2=text2+text[i]
        i=i+1
        
    textCrypt=[]
    i=0
    while i<lgrText:
        chifCrypt=ord(text[i])
        textCrypt.append(chifCrypt)
        i=i+1
    lgrTextCrypt=len(textCrypt)
    i=0
    while i<lgrTextCrypt:
        textCrypt[i]=int(round(textCrypt[i]**(e**(1/nivSecu))))
        i=i+1
    
    f=open("textCrypt.txt","w")
    f.write(str(pw1))
    f.write(" ")
    f.write(str(textCrypt))
    f.close()

    print("Le texte crypté est dans le fichier 'textCrypt.txt'")
    input()

if sys==1 and choix=="d":
    chaine=""
    cle=""

    f=open("textCrypt.txt","r")
    fichCrypt=f.read()
    f.close()
    
    blocCrypt=fichCrypt
    lgrBlocCrypt=len(blocCrypt)
    nbrVirg=0

    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)

    # Suppression des espaces
    blocCrypt2=""
    i=0
    while i<lgrBlocCrypt:
        if blocCrypt[i]!=" ":        
            blocCrypt2=blocCrypt2+blocCrypt[i]
        i=i+1
    blocCrypt=blocCrypt2
    lgrBlocCrypt=len(blocCrypt)
        
    # Décryptage de chaque bloc
    message=""
    n=0
    j=0
    k=0
    while k<lgrBlocCrypt:
        j=k
        nbrCrypt2=0
        textDecrypt=""    
        nbrCrypt=""
        while j<lgrBlocCrypt and blocCrypt[j]!=",":
                nbrCrypt=nbrCrypt+blocCrypt[j]
                j=j+1
        k=j
        if nivSecu==3:
            m=32
            while m<300:
                nbrCrypt=int(nbrCrypt)
                if nbrCrypt==int(round(exp((64/9*(m)*log(m))**(1/3)))):
                    message=message+chr(m-nivSecu*n)
                m=m+1
        if nivSecu==4:
            m=32
            while m<300:
                nbrCrypt=int(nbrCrypt)
                if nbrCrypt==int(round(exp((64/9*(m)*log(m))**(1/3)))):
                    message=message+chr(m-nivSecu*n)
                m=m+1
        if nivSecu==5:
            m=32
            while m<300:
                nbrCrypt=int(nbrCrypt)
                if nbrCrypt==int(round(exp((64/9*(m)*log(m))**(1/3)))):
                    message=message+chr(m-nivSecu*n)
                m=m+1
        if nivSecu==6:
            m=32
            while m<300:
                nbrCrypt=int(nbrCrypt)
                if nbrCrypt==int(round(exp((64/9*(m)*log(m))**(1/3)))):
                    message=message+chr(m-nivSecu*n)
                m=m+1
        if nivSecu==7:
            m=32
            while m<300:
                nbrCrypt=int(nbrCrypt)
                if nbrCrypt==int(round(exp((64/9*(m)*log(m))**(1/3)))):
                    message=message+chr(m-nivSecu*n)
                m=m+1
        n=n+1
        k=k+1
                      
    print("Le texte décrypté est : ",message)
    input()

if sys==2 and choix=="d":
    f=open("pwCrypt","r")
    t1=f.readline()
    f.close()
    f=open("textCrypt","r")
    t2=f.readline()
    f.close()

    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)

    pw=t1
    lgrPw=len(pw)
    text=t2
    lgrText=len(text)

    # Calcul du nombre de mots de passe
    pwNbr=1
    i=0
    while i<lgrPw:
        if pw[i]==",":
            pwNbr=pwNbr+1
        i=i+1

    # Début d'automatisation pour le mot de passe crypté
    pw3=[]
    j=0
    while j<pwNbr:        
        pw2=0
        flag=1000
        i=j*6
        while i<lgrPw:
            if pw[i]=="[" or pw[i]=="," or pw[i]==" " or pw[i]=="]":
                i=i+1    
            else:
                pw2=pw2+(int(pw[i])*flag)
                flag=int(flag/10)
                i=i+1
        pw3.append(pw2)
        j=j+1
    
    # Début d'automatisation pour le texte crypté
    text3=[]
    j=0
    while j<pwNbr:
        text2=0
        flag=100000
        i=j*8
        while i<lgrText:
            if text[i]=="[" or text[i]=="," or text[i]==" " or text[i]=="]":
                i=i+1
            else:
                text2=text2+(int(text[i])*flag)
                flag=int(flag/10)
                i=i+1
        text3.append(text2)
        j=j+1
    # Fin d'automatisation
    

    pw=[]
    i=0
    while i<pwNbr:
        pw.append(pw3)
        i=i+1
        lgrPw=len(pw)
    text=[]
    i=0
    while i<pwNbr:
        text.append(text3)
        i=i+1
        lgrText=len(text)

    # Régénération des 16 PW pour les 16 rondes
    # Première partie    							
    pw01=[]
    i=0
    while i<lgrPw:
        pw01.append(pw3[i]+nivSecu*580)
        i=i+1
    pw02=[]
    i=0
    while i<lgrPw:
        pw02.append(pw01[i]+nivSecu*590)
        i=i+1
    pw03=[]
    i=0
    while i<lgrPw:
        pw03.append(pw02[i]+nivSecu*600)
        i=i+1
    pw04=[]
    i=0
    while i<lgrPw:
        pw04.append(pw03[i]+nivSecu*610)
        i=i+1
    pw05=[]
    i=0
    while i<lgrPw:
        pw05.append(pw04[i]+nivSecu*620)
        i=i+1
    pw06=[]
    i=0
    while i<lgrPw:
        pw06.append(pw05[i]+nivSecu*630)
        i=i+1
    pw07=[]
    i=0
    while i<lgrPw:
        pw07.append(pw06[i]+nivSecu*640)
        i=i+1
    pw08=[]
    i=0
    while i<lgrPw:
        pw08.append(pw07[i]+nivSecu*650)
        i=i+1
    
    # Deuxième partie
    pw01.reverse()
    pw09=pw01
    pw02.reverse()   
    pw10=pw02
    pw03.reverse()    
    pw11=pw03
    pw04.reverse()    
    pw12=pw04
    pw05.reverse()   
    pw13=pw05
    pw06.reverse()    
    pw14=pw06
    pw07.reverse()    
    pw15=pw07
    pw08.reverse()    
    pw16=pw08

    # Les 16 rondes

    def rondes16(lgrText,text3,pw16):
        i=0
        while i<lgrText:
            text3[i]=text3[i]-pw16[i]
            i=i+1

    rondes16(lgrText,text3,pw16)
    rondes16(lgrText,text3,pw15)
    rondes16(lgrText,text3,pw14)
    rondes16(lgrText,text3,pw13)
    rondes16(lgrText,text3,pw12)
    rondes16(lgrText,text3,pw11)
    rondes16(lgrText,text3,pw10)
    rondes16(lgrText,text3,pw09)
    rondes16(lgrText,text3,pw08)
    rondes16(lgrText,text3,pw07)
    rondes16(lgrText,text3,pw06)
    rondes16(lgrText,text3,pw05)
    rondes16(lgrText,text3,pw04)
    rondes16(lgrText,text3,pw03)
    rondes16(lgrText,text3,pw02)
    rondes16(lgrText,text3,pw01)
    
    text2=""
    i=0
    while i<lgrText:
        text2=text2+chr(text3[i])
        i=i+1
    
    print("Le texte décrypté est : ",text2)
    input()

if sys==3 and choix=="d":
    f=open("textCrypt.txt","r")
    t=f.readline()
    f.close()
    lgrT=len(t)

    chaine=""
    cle=""

    i=0
    while i<lgrT and t[i]!=" ":
        cle=cle+t[i]
        i=i+1
    lgrCle=len(cle)
    pw1=int(cle)
    pw=input("Entrez le mot de passe puis 'enter' : ")
    lgrPw=len(pw)

    nivSecu=input("Entrez le niveau de sécurité de 3 à 7 puis 'enter' : ")
    nivSecu=int(nivSecu)
    
    pw2=0
    i=0
    while i<lgrPw:
        pw2=pw2+ord(pw[i])
        i=i+1
    e=int(pw1/pw2)
    
    bloc=""
    i=lgrCle+2
    while i<lgrT-1 and (t[i]!="[" or t[i]!="]"):
        bloc=bloc+t[i]     
        i=i+1
    blocCrypt=bloc

    lgrBlocCrypt=len(blocCrypt)
    nbrVirg=0

    # Suppression des espaces
    blocCrypt2=""
    i=0
    while i<lgrBlocCrypt:
        if blocCrypt[i]!=" ":        
            blocCrypt2=blocCrypt2+blocCrypt[i]
        i=i+1
    blocCrypt=blocCrypt2
    lgrBlocCrypt=len(blocCrypt)
        
    # Décryptage de chaque bloc
    message=""
    j=0
    k=0
    while k<lgrBlocCrypt:
        j=k
        nbrCrypt2=0
        textDecrypt=""    
        nbrCrypt=""
        while j<lgrBlocCrypt and blocCrypt[j]!=",":
                nbrCrypt=nbrCrypt+blocCrypt[j]
                j=j+1
        k=j
        nbrCrypt2=int(round((int(nbrCrypt)**(1/(e**(1/nivSecu))))))
        message=message+chr(nbrCrypt2)    
        k=k+1
                      
    print("Le texte décrypté est : ",message)

print("FIN")
    
    


    
