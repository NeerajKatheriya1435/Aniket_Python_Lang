
# class Human:
#     # name="Rohan"
#     # age=89
#     # id=101
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id

#     def details(self):
#         print(f"My name is: {self.name} and age is: {self.age}")




# h1=Human()
# print(h1.name)
# print(h1.age)


# h2=Human()
# print(h2.name)
# print(h2.age)

# h1=Human("Neeraj",45,101)
# # print(h1.name)
# h1.details()

# h2=Human("Rahul",95,102)
# # print(h2.name)
# h2.details()


# def greet(func):
#     func()
#     print("Hello Good Morning")
#     func()

# def username():
#     print("--------------------")

# greet(username)
# greet()

# def decorator(func):
#     def wrapper():
#         print("Welcome")
#         func()
#         print("Goodbye")
#     return wrapper

# @decorator
# def greet(name):
#     print("Hello", name)


# greet("Aniket")

# @decorator
# def addTwoNum():
#     print("The sum is 14")

# addTwoNum()


# class Human:
#     def run(self):
#         print("Human can run")

#     def walk(self):
#         print("Human can walk")

# class Teacher(Human):
#     def teach(self):
#         print("Human can teach")

# class Programmer(Human):
#     def program(self):
#         print("Human can program")


# class Hacker(Teacher,Programmer):
#     def hack(self):
#         print("You can hak the system")


# h1=Human()
# h1.run()
# h1.walk()
# h1.teach()

# h1=Teacher()
# h1.run()
# h1.walk()
# h1.teach()

# p1=Programmer()

# p1.run()
# p1.program()

# h1=Hacker()

# h1.program()
# h1.teach()
# h1.run()
# h1.hack()


# class Human:

#     def __init__(self,name,age):
#         self.__name=name
#         self._age=age
#         self.age=age

#     def run(self):
#         print(f"Human can run {self.__name}")

#     def walk(self):
#         print("Human can walk")
    

# h1=Human("Shubham",45)
# print(h1._Human__name)
# h1.run()

# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def show(self): # normal method
#         print("Value is:", self.value)

#     @staticmethod  # static method
#     def sum(num1,num2):
#         # print(self.value)
#         print(num1+num2)


# obj1 = MyClass(10)
# obj2 = MyClass(10)
# obj.show()
# obj.sum(4,6)
# MyClass.sum(obj1,8,5)
# MyClass.sum(obj2,7,5)
# obj2.show(3,6)
# MyClass.sum(4,7)
# obj1.sum(5,7)