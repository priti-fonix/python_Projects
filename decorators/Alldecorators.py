
# class textile:

#     name = 'Wooden'
    
#     @staticmethod 
#     def __init__(self,name):  #------------- used for simple method change within the class methods-----------------
#         self.name = name

#     @classmethod
#     def Classname(self , name):  # ------------- used for class level  properties -----
#         self.name = name

#     @property #-------------- to make any attribute dynamic------------
#     def percentage(self):
#         return  str((self.phy + self.chem + self.math) /3)
    
# decorators with args and kwargs
def logger(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))


#-------------------decorators with parameters-----------------
# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat(3)
# def hello():
#     print("Hello!")

# hello()

#-------------------decorators -----------------
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello!")

# greet()
