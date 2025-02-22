# Task 1
# The user types in three numbers. 
# The program prints the sum or product of these numbers 
# based on the user's choice.
# Task 2
# The user types in three numbers. Based on the user's choice, the program prints a maximum of three, a minimum of three, or arithmetic mean of three numbers.


# lista=[]
# for i in range (0,3):
#     temp=int(input(f"Type no. {i+1}: "))
#     lista.append(temp)
#     print (lista[i])

# gameOn=True
# while gameOn:
#     print("Option 1: \"Product\"\n"
#           "Option 2: \"Sum\"\n"
#           "Option 3: \"Max\"\n"
#           "Option 4: \"Min\"\n"
#           "Option 5: \"Mean\"\n"
#           "Option 6: \"Exit\"")
#     opt=input("Choose: ")
#     if opt=="Product":
#         print(f"{lista[0]}*{lista[1]}*{lista[2]}=",
#               f"{lista[0]*lista[1]*lista[2]}")
#     elif opt=="Sum":
#         print(f"{lista[0]}+{lista[1]}+{lista[2]}=",
#               f"{lista[0]+lista[1]+lista[2]}")
#     elif opt=="Max":
#         print(f"Max of: {lista[0]}+{lista[1]}+{lista[2]} is:",
#               f"{max(lista[0],lista[1],lista[2])}")
#     elif opt=="Min":
#         print(f"Min of: {lista[0]},{lista[1]},{lista[2]}=",
#               f"{min(lista[0],lista[1],lista[2])}")
#     elif opt=="Mean":
#         print(f"Mean of: {lista[0]},{lista[1]},{lista[2]} is",
#               f"{(lista[0]+lista[1]+lista[2])/3}")
#     else:
#         print("Come back soon!")
#         gameOn=False


# Task 3
# The user types in the number of meters. 
# Based on the user's choice, the program converts 
# meters to miles, inches, or yards.

inputData=int(input("Number of meters:"))

gameOn=True
while gameOn:
    print("Option 1: \"Miles\"\n"
          "Option 2: \"Inches\"\n"
          "Option 3: \"Yards\"\n"
          "Option 6: \"Exit\"")
    opt=input("Choose: ")
    if opt=="Miles":
        print(f"{inputData} meters=",
              f"{inputData*0.000621371192} miles")
    elif opt=="Inches":
        print(f"{inputData} meters=",
              f"{inputData*39.3700787} inches")
    elif opt=="Yards":
        print(f"{inputData} meters=",
              f"{inputData*1.0936133} yards")
    else:
        print("Come back soon!")
        gameOn=False