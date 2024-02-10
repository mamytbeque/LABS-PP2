a = 33
b = 200
if b > a:
  print("b is greater than a")
  
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
a = 33
b = 200
if b > a:
  pass

#ex1
a = 50
b = 10
if a > b:
  print("Hello World")
#ex2
a = 50
b = 10
if a != b:
   print("Hello World")
#ex3
a = 50
b = 10
if a==b:
    print("Yes")
else:
    print("No")
#ex4
a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")
#ex5
c=40
d=40
if a==b and c==d:
    print("Hello")
#ex6
if a==b or c==d:
    print("Hello")
#ex7
if 5>2:
    print ("YES")
#ex8
a = 2
b = 5
print("YES") if a==b else print("NO")
#ex9
if a==c or b==c:
    print("YES")
