print("Let's play a math game. If you want to exit, just type exit.")

gameOn=True

while gameOn:    
    print("\n ----------------\n",
          "a% from x is y. Give me a and y",
          "\n(separated by \' is \'. e.g.: 18% is 20)",
          "\nand i'll give you the value of x.")
    opt=input("Type ?% is ?':")    
    if opt=="exit":
        gameOn=False        
    else:
        opt=opt.split(" is ")
        a=int(opt[0][:-1])/100        
        y=int(opt[1])        
        x=int(y/a)
        print(f"Cool. x is {x}")
        opt=input("continue? (yes/no)")
        if opt=="no":
            print("See you later!")
            exit()