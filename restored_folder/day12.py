
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# num3=int(input("Enter num3: "))

# if(num1>num2):
#     if(num1>num3):
#         print("Gretest Number is:",num1)
#     else:
#         print("Gretest Number is:",num3)
# else:
#     if(num2>num3):
#         print("Gretest Number is:",num2)
#     else:
#         print("Gretest Number is:",num3)


# list1=[4,34,67,7,5,4,3,4]
# list1=[i for i in range(80) if i>50]
# print(list1)

# def addTwo(num1,num2):
#     return num1+num2

# addNum=lambda a,b:a+b

# print(addNum(7,5))

# square = lambda x: x * x
# print(square(4)) # Output: 16

# def square(x):
#     return x * x
from functools import reduce
l1=[3,5,6,7,8]

# squraredList=list(map(square,l1))

# squraredList=list(map(lambda x:x*x,l1))
# squraredList=list(map(lambda x:x+7,l1))
# print(squraredList)

# greterThan5=list(filter(lambda x:x>5,l1))
# print(greterThan5)
l1=[3,5,6,7,8]
sum=reduce(lambda x,y:x+y,l1)
print(sum)
