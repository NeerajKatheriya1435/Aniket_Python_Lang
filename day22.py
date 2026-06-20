
# userName=input("Enter your name: ")

# i=0
# while(i<3):
#     pin=int(input("Enter the ATM Pin: "))
#     if(pin==3456):
#         balance=5000
#         str1=int(input("Enter the trasaction you want: " \
#         "\n1. Check Balance" \
#         "\n2. Deposit" \
#         "\n3. Withdraw" \
#         "\n4. Exit" \
#         "\n"))
#         match(str1):
#             case 1:
#                 print(f"{userName} Your Account balance is: {balance}")
#                 break
#             case 2:
#                 depositMoney=int(input("Enter the money you want deposit: "))
#                 print(f"You have Successfully Deposit Money: {depositMoney}")
#                 print(f"{userName} Your Account balance is: {balance+depositMoney}")
#                 break
#             case 3:
#                 withdrawMoney=int(input("Enter the money you want withdraw: "))
#                 print(f"You have Successfully Deposit Money: {withdrawMoney}")
#                 print(f"{userName} Your Account balance is: {balance-withdrawMoney}")
#                 break
#             case 4:
#                 print(f"You Chose Exit Option Be Happy Sir/Mam")
#                 break
#     else:
#         print("Incorrect Pin Try Again")
#     i+=1
# else:
#     print("Your ATM PIN has Blocked for 24 Hours")

# print("Thanku for Using Canara Bank")

import random
computerNumber=random.randint(1,4000)
count=1

while(True):
    userNumber=int(input("Enter your number: "))
    if(userNumber!=computerNumber):
        if(userNumber>computerNumber):
            print("Your number is BIGGGER than Computer")
        elif(userNumber<computerNumber):
            print("Your number is SMALLER than Computer")
    else:
        print(f"You figured out in {count} moves")
        break
    count+=1