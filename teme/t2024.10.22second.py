#Se dă un număr natural n. 
# Determinaţi câte cifre are suma cifrelor sale.

a=int(input("No="))
ai=a

sum=0
loop=0
while ai>0:
    digit=int(ai%10)
    sum+=digit
    ai=ai/10
    # print(sum)
    if ai<1:
        loop+=1
        # print(sum)
        if loop<=2:
            ai=sum
            sum=0
print(sum)
