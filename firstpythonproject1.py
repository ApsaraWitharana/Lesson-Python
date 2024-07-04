
 # Task 01 ==> print
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)


print("Starting the program")

def my_function():

  a, b = 3, 4
  if a > b:
   print("a is greater than b")
  else:
   print("b is greater than or equal to a")

my_function()

# Ex -01 -Variables and Types --->> string,float,int

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code

if mystring == "hello":
     print("String: %s" % mystring)
     print("String:" + mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
     print("Float: %f" % myfloat)
     # can not using this ->not all arguments converted during string formatting
     # print("String:" + myfloat)
if isinstance(myint, int) and myint == 20:
     print("Integer: %d" % myint)
     # can not using this ->not all arguments converted during string formatting
     # print("String:" + myint)

# Ex 02
def tree(height):
    length = height*2 -1
    stars =1
    for i in range(1,height+1):
        print(("*" * stars).center(length))
        stars += 2
        # print("*" .center(length))

tree(9)
tree(20)

# Day 2 ---> List

mylist = [1,2,3,4,5,6,7,8,9,10]
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)
mylist.append(7)
mylist.append(8)
mylist.append(9)
mylist.append(10)
print(mylist[10])

# prints out 1,2,3,4,5,6,7,8,9,10

for x in mylist:
 print(x)

# Ex--02

numbers = []
strings = []
names = ["Sachi", "Kanu", "Anu"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).

print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)