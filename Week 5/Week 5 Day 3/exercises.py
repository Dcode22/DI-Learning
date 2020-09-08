# class Currency:
#     def __init__(self, amount, currency_type):
#         self.amount = float(amount)
#         self.currency_type = currency_type

#     def __str__(self):
#         return f"This is {self.amount} {self.currency_type}"
    
#     def __repr__(self):
#         return f"{self.currency_type}:{self.amount}"
    
#     def __add__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 return self.amount + other.amount, self.currency_type
#             else:
#                 raise ValueError
#         except:
#             print("You cannot add two different currencies")
#     def __sub__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 return self.amount - other.amount, self.currency_type
#             else:
#                 raise ValueError
#         except:
#             print("You cannot subtract two different currencies")
        
#     def __iadd__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 self.amount += other.amount
#                 return "your first variable now equals:", self.amount, self.currency_type
#             else:
#                 raise ValueError
#         except:
#             print("You cannot add two different currencies")

    
#     def __isub__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 self.amount -= other.amount
#                 return "your first variable now equals:", self.amount, self.currency_type
#             else:
#                 raise ValueError
#         except:
#             print("You cannot subtract two different currencies")
    
#     def __mul__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 return self.amount * other.amount, self.currency_type
                
#             else:
#                 raise ValueError
#         except:
#             print("You cannot multiply two different currencies")
    
#     def __imul__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 self.amount *= other.amount
#                 return "your first variable now equals:", self.amount, self.currency_type
#             else:
#                 raise ValueError
#         except:
#             print("You cannot multiply two different currencies") 
    
#     def __div__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 return (self.amount / other.amount), self.currency_type
                
#             else:
#                 raise ValueError
#         except:
#             print("You cannot divide two different currencies")
    
#     def __idiv__(self, other):
#         try:
#             if other.currency_type == self.currency_type:
#                 self.amount /= other.amount
#                 return "your first variable now equals:", self.amount, self.currency_type
                
#             else:
#                 raise ValueError
#         except:
#             print("You cannot divide two different currencies")




# def list_methods(object):
#     object_methods = [method_name for method_name in dir(object)]
#     print(object_methods) 


# def main():
#     list_methods(Currency)
#     ilssix = Currency(6.25, "ILS")
#     ilsseven = Currency(7, "ILS" )
#     usdthree = Currency(3, "USD")
#     new = ilssix * ilsseven
#     print(ilssix / ilsseven)
    
#     print(new)
# main()


# exercise 2
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __repr__(self):
#         return str(self.radius)

#     def __str__(self):
#         return f"This circle has a radius of {self.radius}"

#     def get_radius(self):
#         return self.radius
    
#     def get_diameter(self):
#         return self.radius*2
    
#     def get_area(self):
#         return (self.radius**2)*math.pi

    
    
#     def __add__(self, other):

#         return self.radius + other.radius 
    
#     def __gt__(self, other):
#         if self.radius > other.radius:
#             return True
        
#         else:
#             return False

#     def __eq__(self, other):
#         if self.radius == other.radius:
#             return True

#         else:
#             return False
    
# def main():
#     circle_1 = Circle(1)
#     circle_2 = Circle(2)

#     print(circle_1.get_diameter())

#     print(circle_2)

#     print(circle_2.get_area())

#     print(circle_2.get_diameter())

#     print(circle_2 + circle_1)

#     print(circle_2 > circle_1)

#     print(circle_1 == circle_2)

#     list = [circle_2, circle_1]

#     print(list)

#     list.sort()

#     print(list)


# main()


# exercise 3 

# first import randint to be able to select a random integer from a range
from random import randint

# the following function returns a random number between 1 and 10
def get_num():
    # the number variable is assigned to a random number between 1 and 10
    number = randint(1,10)
    # the random number in the number variable gets returned when the get_num fuction is called
    return number


# the following function is supposed to print the return of the function entered times itself
def pwr(func): 
    # the value of the entered function is assigned to the variable number
    number = func()
    # the value of the function is printed, as well as the value of the function squared
    print(number, number*number)
# the pwr function is now called with the get_num function from above passed into it, so that it will return a random number and that random number squared
pwr(get_num)


        
    




