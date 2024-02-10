thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

list1=["apple", "banana", "cherry"]
list1.append("orange")
print(list1)

list2=["apple", "banana", "cherry"]
list2.insert(1, "orange")
print(list2)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

mylist=["apple", "banana", "cherry"]
mytuple=("kiwi", "orange")
mylist.extend(mytuple)
print(mylist)

thislist=["apple", "banana", "cherry"]
thislist[1]="blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3]=["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

list1=["apple", "banana", "cherry", "kiwi", "mango"]
list1=[x for x in list1 if "a" in x]
print(list1)

newlist=[x for x in fruits if x!="apple"]
print(newlist)

list2=[x for x in list1]
print(list2)

mylist=[x for x in range (10)]
print(mylist)

li=[x for x in range(10) if x<5]
print(li)

newlist=[x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

thislist = ["apple", "banana", "cherry"]
print(thislist)

mylist= ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1=["apple", "banana", "cherry"]
list2=[1,5,6,3]
list3=[True, False, True]
list4=["abc", 34, True, 40, "main"]
print(list1, list2, list3, list4 )

print(type(list4))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist)

mylist= ["apple", "banana", "cherry", "apple", "cherry"]
print(mylist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1=["apple", "banana", "cherry"]
list2=[1,5,6,3]
list3=[True, False, True]
list4=["abc", 34, True, 40, "main"]
print(list1, list2, list3, list4 )

print(type(list4))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

list1 =["apple", "banana" ,"cherry"]
list1.remove("banana")
print(list1)

mylist=["apple", "banana", "cherry", "banana", "kiwi"]
mylist.remove("banana")
print(mylist)

list2=["apple", "banana", "cherry"]
list2.pop(1)
print(list2)

thislist=["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

list3=["apple", "banana", "cherry"]
del list3[0:2]
print(list3)
"""
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)"""

list4= ["apple", "banana", "cherry"]
list4.clear()
print(list4)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#ex1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#ex2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#ex3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#ex4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#ex5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#ex6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
