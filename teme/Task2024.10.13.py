# task 1 : Sa se verifice daca ambele numere introduse de utilizator 
# sunt pare sau daca amandoua sunt impare
a=int(input("a="))
b=int(input("b="))
pare=False
impare=False
if a%2==0 and b%2==0:
    pare=True
    print("Both numbers are even.")
if a%2==1 and b%2==1:
    impare=True
    print("Both numbers are odd.")

if pare or impare:
    print("Condition vfulfilled. Both numbers are the same (even/odd).")


# Sa se verifice daca ambele cifre ale unui numar intre 10 si 99 sunt pare sau daca ambele sunt impare
a=int(input("a="))
if a<10 or a>=100:
    print("Number is either to small or to big for this exercise.")
    exit()
a1=int(a/10)
a2=int(a%10)
print(a1,a2)
pare=False
impare=False
if a1%2==0 and a2%2==0:
    pare=True
    print("Both numbers are even.")
if a1%2==1 and a2%2==1:
    impare=True
    print("Both numbers are odd.")

if pare or impare:
    print("Condition fulfilled. Both numbers are the same (even/odd).")
else:
    print("Condition is not met.")

# Sa se determine cea mai mare cifra a unui numar cu 3 cifre
a=int(input("a="))
if a<100 or a>=1000:
    print("Number is either to small or to big for this exercise.")
    exit()
a1=int(a/100)
a2=int((a-100*a1)/10)
a3=int(a%10)
print(a1,a2,a3)
max=a1
if a2>max:
    max=a2
if a3>max:
    max=a3
print("Max=",max)
