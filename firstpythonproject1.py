
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
print("==============")
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
print("==============")
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
print("==============")
# prints out 1,2,3,4,5,6,7,8,9,10

for x in mylist:
 print(x)
print("==============")

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


print("==============")
# Day 3 ---> Basic Operators
# numbers --Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

number = 1 + 2 * 3 / 4.0
print(number)

print("==============")
# Another operator available is the modulo (%) operator, which returns the integer remainder of the division. dividend % divisor = remainder.

remainder = 11 % 3
print(remainder)

print("==============")

# Using two multiplication symbols makes a power relationship.

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

print("==============")
# strings using the addition operator

helloworld = "hello" + " " + "world"
print(helloworld)


print("==============")
# multiplying strings to form a string with a repeating sequence

lotsofhellos = "hello" * 10
for x in lotsofhellos:
    print(x)

for x in range(10):
 print("sorry:",x)

print("==============")
# Lists can be joined with the addition operators

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)