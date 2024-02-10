#addition
x = 5
y = 3
print(x + y)


#substraction
x = 5
y = 3
print(x - y)


#multiplication
x = 5
y = 3
print(x * y)


#division
x = 12
y = 3
print(x / y)


#modulus
x = 5
y = 2
print(x % y)


#exponentiation
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2


#floor division
x = 15
y = 2
print(x // y) #the floor division // rounds the result down to the nearest whole number


#compares each numbers binary values with AND operation
x = 5
x &= 3
print(x)
#compares by or
	x |= 3
#compares by XOR
x ^= 3


# It's same as negation in Discrete Math.Reverse the result, returns False if the result is true
x=5
print(not(x < 5 and x < 10))


#is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#is not
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)


x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list


print(~3)
"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
"""


#ex1
print(10*5)
#ex2
print(10/2)
#ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
#ex4
if 5 != 10:
  print("5 and 10 is not equal")
#ex5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
