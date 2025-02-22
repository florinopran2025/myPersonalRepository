# task 1: buy 4$ flowers with a $30 budget
print(f"With 30$ you can buy {int(30/4)} flowers. You'll receive a ${30%4} change.")

# task 2: average of 3 numbers
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
average=(a+b+c)/3
print(f"Average={round(average,2)}")

# task 3: translate months
english=["january","february","march","april","may","june",
         "july","august","september","october","november","december"]
romanian=["ianuarie","februarie","martie","aprilie","mai","iunie",
         "iulie","august","septembrie","octombrie","noiembrie","decembrie"]

exit=False
while exit==False:
    print("Type exit if you get bored")
    month=input("Month (english to romanian): ")
    if month in english:
        id=english.index(month)
        print(id)
        print(f"{english[id]}={romanian[id]}")
    elif month!="exit":
        print("There's no such month")
    else:
        print("Bye")
        exit=True

