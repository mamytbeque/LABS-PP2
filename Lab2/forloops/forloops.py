for x in range(2, 6):
  print(x)
  
for x in range(2, 30, 3):
  print(x)
  

for x in range(6):
  print(x)
else:
  print("Finally finished!")
  

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
  

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
    
for x in [0, 1, 2]:
  pass

#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)
  
#ex3
for x in range(6):
    print(x)
    
#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x=="banana":
        break
    print(x)
