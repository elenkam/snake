
print("ahoj")
print(5)


a=10
b=1.1
c=1.0
d=1
e=a+b+c+d

print(e)
print("zvolte si zeleninu")
print("1. uhorku")
print("2. baklažán")
volba=int(input("napiste cislo\n")) # aby som si zapamatala moju odpoved, \n nový  riadok a \t tabulátor

#Moznost 1 - oskliva
#if volba==1:
#    print("vybrali ste si uhorku")
#else:
#    if volba==2:    
#        print("vybrali ste si baklažán")
#    else:
#        print("spatna volba")
#        
#Moznost 2 - mene oskliva      
#if volba==1 or volba==2:
#    if volba==1:
#        print("vybrali ste si uhorku")
#    else:
#        print("vybrali ste si baklažán")
#else:
#    print("spatna volba")

if volba==1:
    print("vybrali ste si uhorku")
elif volba==2:
    print("vybrali ste si baklažán")
else:
    print("spatna volba")
    
 
    
zoznam1=[1,"str",3,8,5/4,10%3]

for i in range(10):   # defaultne ide od nuly po 10 po jednotkách, tj range(0,10,1)
    print(i)

for i in range(5,10):
    print(i)


for i in range(5,16,2):
    print(i)


for i in range(101):
    if i%3==0:
        print(i)

for i in range(len(zoznam1)):
    print(zoznam1[i])






