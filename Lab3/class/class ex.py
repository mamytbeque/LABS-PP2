#ex1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

manipulator = StringManipulator()


manipulator.getString() = manipulator.printString()
#ex2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length * self.length

square = Square(5)
print("Area of the square:", square.area())
#ex3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 4)
print("Area of the rectangle:", rectangle.area())
#ex4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show() 
point2.show() 

distance = point1.dist(point2)
print("Distance between the points:", distance) 

point1.move(5, 7)
point1.show() 
#ex5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit of ${} accepted. Current balance is ${}".format(amount, self.balance))
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrawal of ${} accepted. Current balance is ${}".format(amount, self.balance))
            else:
                print("Insufficient funds. Withdrawal of ${} cannot be processed.".format(amount))
        else:
            print("Invalid withdrawal amount.")

#ex6
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)
