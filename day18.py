# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         print("Person is Running")
    
#     def __str__(self):
#         return f"My name is: {self.name}"

#     def __len__(self):
#         return len(self.name)


# p1 = Person("Rohan",56)
# p1.run()

# print(dir(p1))

# print(p1)

# p2=Person("Aniket Kumar",89)

# print(p2)
# print(len(p2.name))
# print(len(p2))

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def pointsValue(self):
#         return f"{self.x}i + {self.y}j"
    
#     def addTwoPoint(self,other):
#         return (f"{self.x+other.x}i + {self.y+other.y}j")

# p1=Point(5,7)
# print(p1.pointsValue())

# p2=Point(3,4)
# print(p2.pointsValue())

# # print(p1+p2)
# print(p1.addTwoPoint(p2))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other): # Overloading +
#         return Point(self.x + other.x, self.y + other.y)
#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2 # This calls p1.__add__(p2)
# print(p3) # Output: (6, 8)

# for i in range(4000):
#     pass

# import time

# t1=time.time()

# for i in range(400000000):
#     pass

# t2=time.time()

# print(t2-t1)

# import time
# print(time.localtime())

# local=time.localtime()
# print("Formatted Date :", time.strftime("%Y-%m-%d %H:%M:%S", local))

# time_str = "2025-07-16 11:00:00"
# parsed = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
# print(parsed)

# print("CTime:", time.ctime())

# import argparse

# # Create parser
# parser = argparse.ArgumentParser(description="Simple calculatorutility")

# # Add arguments
# parser.add_argument("num1", type=float, help="First number")
# parser.add_argument("num2", type=float, help="Second number")
# parser.add_argument("--operation", "-o", choices=["add", "sub"],default="add", help="Operation to perform")

# # Parse arguments
# args = parser.parse_args()

# # Perform operation
# result=0
# if args.operation == "add":
#     result = args.num1 + args.num2
# else:
#     result = args.num1 - args.num2

# print("Result:", result)
