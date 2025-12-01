'''
__init__()

'''
#automatically calls methods after object is created

class Car:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    

c1 = Car("audi","red")
print(c1)
print(c1.brand)
print(c1.color)