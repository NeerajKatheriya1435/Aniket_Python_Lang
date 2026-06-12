
class Human:
    # name="Rohan"
    # age=67
    def __init__(self,name,age):

        self.name=name
        self.age=age

    def detaits(self):
        print(f"My name is: {self.name}")
        print(f"My age is: {self.age}")

    @property
    def getname(self):
        return self.name
    
    @getname.setter
    def setname(self,secondName):
        if len(secondName) > 0:
            self.name = secondName
        else:
            print("Name cannot be empty")


# h1=Human()
# h1.name="Suman"
# h1.age=56
# h1.detaits()


# h2=Human()

# h2.detaits()

# h3=Human()
# print(h3.name)
# print(h3.age)

# h1=Human("Rohan",89)
# h1.detaits()

h2=Human("Rohit",56)
# h2.name="35467"
# print(h2.name)
# h2.detaits()
h2.setname="Rahul"
print(h2.getname)