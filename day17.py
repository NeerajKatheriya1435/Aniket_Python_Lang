# class Human:

#     company="Tesla"
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
    
#     @classmethod
#     def from_string(cls, data_str):
#         name, age, salary = data_str.split('-')
#         return cls(name, int(age),int(salary))

#     def printDetails(self):
#         print(f"My name is:",self.name)
#         print(f"My age is:",self.age)
#         print(f"My salary is:",self.salary)

# h1=Human("Rohan",56,29000)
# h2=Human("Keshav",45,34000)
# h3=Human("Aniket",72,56000)


# print(h1.name)
# print(h2.name)
# print(h3.name)

# h1.company="Hundai"

# Human.company="Zara"

# print(h1.company)
# print(h2.company)
# print(h3.company)

# str1="Rohan-78-56000"


# h1=Human.from_string("Keshav-89-56000")
# h1.printDetails()

# print(dir(h1))
# print(dir(h1))
# print(h1.__dict__)
# str1="Hello i am good"
# help(h1.__dict__)
# help(str1.upper)
# help(str1.lower)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("Person is Running")

class Employee(Person):

    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary=salary

    def run(self):
        super().run()
        print("Employee is running")
    def drink(self):
        print("Employee is drinking")


# p1=Person("Rohan",78)
# p1.run()
# p1.drink()

e1=Employee("Rohan",78,67000)
e1.run()