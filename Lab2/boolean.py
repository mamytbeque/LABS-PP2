print(10==10)

print(10 > 9)
print(10 == 9)
print(10 < 9)
#returns boolean value

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))


x = "Hello"
y = 15
print(bool(x))
print(bool(y))


'''Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones. '''
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


'''In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", 
the number 0, and the value None. And of course the value False evaluates to False.'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


'''One more value, or object in this case, evaluates to False, 
and that is if you have an object that is made from a class with a __len__ function 
that returns 0 or False'''
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#You can create gunctions that returns noolean value
def myFunction() :
  return True

print(myFunction())

#You can execute code based on the Boolean answer of a function
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


# isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int)) #True,cuz x is int type data


#ex 1
print(10>9) #True

#ex2
print(10==9) #False

#ex3
print(10<9) #False

#ex4
print(bool("abc")) #True

#ex5
print(bool(0)) #False,cuz 0 is false value in boolean

