
l1=[4,7,2,7,9,6,78,56,5,98,34,90]

# # print()
# max=l1[0]
# for item in l1:
#     if(item<max):
#         max=item  # max=7

# print(max)

# l1=[4,7,2,7,7,7,5,4,90]

# s1=set(l1)
# l1=list(s1)
# print(l1)
# unique=[]
# for item in l1:
#     if item not in unique:
#         unique.append(item)

# print(unique)
# i=0
# while (i<5):
#     inp1=int(input("Enter the value: "))
#     unique.append(inp1)
#     i+=1

# print(unique)

# def fibb(num):
#     if(num==0):
#         return 0
#     if(num==1):
#         return 1
    
#     return fibb(num-1)+fibb(num-2)

# term=7
# # num=
# print(fibb(term))

# Write a program to check whether a number is an Armstrong number.

# import math
# num=1635
# temp=num
# # count=0
# digit=0

# while(num>0):
#     num//=10
#     digit+=1

# # print(digit)

# armNum=0
# num=temp

# while(temp>0):
#     lastDigit=temp%10
#     armNum=math.pow(lastDigit,digit)+armNum
#     temp//=10

# if(num==armNum):
#     print("Number is ArmStrong")
# else:
#     print("Number is not Armstrong")
