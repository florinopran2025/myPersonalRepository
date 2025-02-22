

print("Iggle has 3 coins (x, y, z)")
print ("Set the data entry for Iggle.")

valueX=float(input("How much martian lei does a Xcoin value?"))
valueY=float(input("How much martian lei does a Ycoin value?"))
valueZ=float(input("How much martian lei does a Zcoin value?"))

print("Perfect. Now disclose how much money does Iggle have.")

walletX=float(input("Number of X coins in Iggle's wallet:"))
walletY=float(input("Number of X coins in Iggle's wallet:"))
walletZ=float(input("Number of X coins in Iggle's wallet:"))

walletTotal=valueX*walletX+valueY*walletY+valueZ*walletZ

if walletTotal>0:
    print("Iggle is a rich martian guy. He has:", walletTotal, "martian lei.")
else:
    print ("Iggle is broke. His net worth is zero!")


