# Practice problems

# def addTwoNum(num1,num2):
#     print("The sum is:",(num1+num2))

# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))

# addTwoNum(num1,num2)
# addTwoNum(6,5)


# def addTwoNum():
#     num1=int(input("Enter num1: "))
#     num2=int(input("Enter num2: "))
#     print("The sum is:",(num1+num2))

# addTwoNum()

# Swap two numbers using third varibale

# a=8
# b=5

# temp=a
# a=b
# b=temp

# a=a+b
# b=a-b
# a=a-b

# b,a=a,b

# print(a,b)

# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# opt=input("Enter the operator: +,-,*,/:  ")

# if(opt=="+"):
#     print("The sum is: ",(num1+num2))
# elif(opt=="-"):
#     print("The diff is: ",(num1-num2))
# elif(opt=="*"):
#     print("The mul is: ",(num1*num2))

# for i in range(10,-5,-1):
#     print(i)

# num=765

# reverse=0

# while(num>0):
#     ld=num%10
#     reverse=reverse*10+ld
#     num//=10

# print(reverse)

# str1="Aniket"
# count=0

# for i in str1:
#     # if i in "aeiouAEIOU":
#     count+=1
# print(count)

def checkPrime(num):
    for i in range(2,num):
        if (num%i==0):
            return True
n=11
if(checkPrime(n)):
    print("Not a Prime")
else:
    print("Is Prime")