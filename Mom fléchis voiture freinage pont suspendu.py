from math import *

mMax=0
i=0
while i<301:
    mf=86.77-84.375*0.001714*i
    print("Moment fléchiss = ",mf)
    mMax=mMax+mf
    input()
    i=i+10

print("Moment maxi = ",mMax)
             
print("FINI")
