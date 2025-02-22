# Task 1
# The user types in a number from 1 to 100. 
# If the number is a multiple of 3 (divisible by 3 without remainder), 
# print the word Fizz. 
# If the number is a multiple of 5, print the wordBuzz. 
# If the word is a multiple of 3 and 5, print Fizz Buzz. 
# If the word is not a multiple of 3 and 5, print the number.
# If the user typed in a number out of the range, print an error message.

# n=1
# while n>=1 and n<=100:
#     n=int(input("n="))
#     mess="Fizz"
#     if n%3==0:
#         mess="Fizz"
#     if n%5==0:
#         mess="WorldBuzz"
#     if n%3==0 and n%5==0:
#         mess="Fizz Buzz"
#     if n%3!=0 and n%5!=0:
#         mess=n
#     print(mess)
# print("Out of the range.")


# Task 2
# Write a program that, at the user's choice, 
# raises the typed in number to the power of 0 through 7.

# n=int(input("number="))
# p=int(input("power (0 to 7)="))
# if p<0 or p>7:
#     print("Power out of interval.")
# else:    
#     pi=p
#     ni=1
#     while pi>0:
#         ni=ni*n
#         pi-=1
#     print(ni)


# Task 3
# Write a program that calculates the cost of a call 
# for different mobile phone operators. 
# The user types in the cost of the call 
# and chooses operators for the outgoing and incoming calls. 
# Print the cost.

# print("We have 3 operators: Telekom, Digi and Vodafone.")
# prices={ 
#     "Telekom to Digi":0.12,
#     "Telekom to Vodafone":0.13,
#     "Digi to Telekom":0.13,
#     "Digi to Vodafone":0.07,
#     "Vodafone to Telekom":0.11,
#     "Vodafone to Digi":0.08
# }

# callDuration=int(input("Duration of the call (minutes):")) 
# outOperator=input("Outgoing operator:")
# inOperator=input("Incoming operator:")

# callConnection=outOperator+" to "+inOperator

# costPerMinute=float(prices[callConnection])
# totalCost=round(costPerMinute*callDuration,2)
# print(f"You made a call from {callConnection}",
#       f"with a cost per minute of ${costPerMinute}.\n",
#       f"The duration of your conversaton was {callDuration} minutes."
#       f"The total cost of your call was ${totalCost}.")



# Task 4
# The salary of a salesperson is $200 + percentage of sales as follows: 
# up to $500 — 3%, from 500 to 1000 — 5%, over 1000 — 8%. 
# The user types in the sales for three salespersons. 
# Determine their salary, the best salesperson, 
# give him or her a $200 bonus, print the result.

# def determineVarSalary(sales):   
#     if sales<500:
#         salary=0.03*sales
#     elif sales>=500 and sales<=1000:
#         salary=0.05*sales
#     else:
#         salary=0.08*sales
#     return salary
# fix=200
# ciolacuSales = int(input("Hom much did Ciolacu made in sales from donuts?"))
# simionSales = int(input("How much did Simion made in sales from cheap apartments?"))
# ciucaSales = int(input("How much did Ciuca make from selling his book?"))

# ciolacuVar=determineVarSalary(ciolacuSales)
# simionVar=determineVarSalary(simionSales)
# ciucaVar=determineVarSalary(ciucaSales)

# dict={"ciolacu":ciolacuVar,
#       "simion":simionVar,
#       "ciuca":ciucaVar
#       }

# max=max(dict.values())
# result=[key for key, val in dict.items() if val==max]


# if len(result)==1:
#     total=fix+max+200
#     print(f"The best con artist was: {result[0]}!\n"
#             f"He got a total of ${total}\n"
#             f"\tHis fix salary was ${fix}.\n"
#             f"\tThe revenue from sales was ${max}\n "
#             f"\tExtra bonus for being the best con artist: $200.\n")
# if len(result)==2:
#     total=fix+max+100
#     print(f"We have a tie between {result[0]} and {result[1]}!")
#     print("Those two con artists split the 200$ bonus.")
#     print(f"Each of them got: ${total}\n"
#                f"\t${fix} as a fix salary.\n"
#                f"\t${max} revenue from sales.\n "
#                f"\t$100 extra bonus for being great con artists.")   
# if len(result)==3:
#     total=fix+max+67
#     print(f"{result[0]}, {result[1]} and {result[2]} made a deal and had equal sales.")
#     print("So they split the bonus.")
#     print(f"Each of them got: ${total}\n"
#                f"\t${fix} fix salary.\n"
#                f"\t{max} as revenue from sales.\n "
#                f"\t$67 Extra bonus for being great con artists.\n")  

