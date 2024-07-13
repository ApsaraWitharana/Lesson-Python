
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

# Ex-01

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

print("==============")

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
     print("Sorry!!!!")

print("==============")

# Ex-02

for x in range(10):
 print("Sorry!!!!:",x)

print("==============")

# Ex-03

for strings in range(10):
 print("Good Night!!")

print("==============")

# EX-04
x = 20*20
y = 20*20

big_list = x+y

if x == 400 and y == 400:
 print("Sorry...")

 # if big_list.count(x) == 400 and big_list.count(y) == 400:
 #  print("hiiii...")

 print("==============")

# EX-05

for strings in range(10):
 print("Sorry!!!!")

 print("==============")

 # Day 4 ---> String Formatting

 # This prints out "Hello, John!"
 name = "John"
 print("Hello, %s!" % name)

 print("==============")

 # This prints out "John is 23 years old."
 name = "Done"
 age = 23
 print("%s is %d years old." % (name, age))

 print("==============")
 # Here are some basic argument specifiers you should know:
 #
 # %s - String (or any object with a string representation, like numbers)
 #
 # %d - Integers
 #
 # %f - Floating point numbers
 #
 # %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
 #
 # %x/%X - Integers in hex representation (lowercase/uppercase)


 # Exercise

 data = ("Done", "The", 53.44)
 format_string = "Hello %s %s. Your current balance is Rs%s."

 print(format_string % data)

 print("==============")

 # Day 5 ---> Basic String Operations

 # That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from
 # the first character. Notice how there are actually two o's in the phrase - this method only recognizes the first.

 astring = "Hello world!"
 print(astring.index("o"))

 print("==============")

 astring = "Hello world!"
 print(astring[3:7])

 print("==============")

 # There is no function like strrev in C to reverse a string. But with the above
 # mentioned type of slice syntax you can easily reverse a string like this

 astring = "Hello world!"
 print(astring[::-1])


 print("==============")

 # These make a new string with all letters converted to uppercase and lowercase, respectively.

 astring = "Hello world!"
 print(astring.upper())
 print(astring.lower())

 print("==============")

 # Exercise

 s = "Strings are awesome!"
 # Length should be 20
 print("Length of s = %d" % len(s))

 # First occurrence of "a" should be at index 8
 print("The first occurrence of the letter a = %d" % s.index("a"))

 # Number of a's should be 2
 print("a occurs %d times" % s.count("a"))

 # Slicing the string into bits
 print("The first five characters are '%s'" % s[:5]) # Start to 5
 print("The next five characters are '%s'" % s[5:10]) # 5 to 10
 print("The thirteenth character is '%s'" % s[12]) # Just number 12
 print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
 print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

 # Convert everything to uppercase
 print("String in uppercase: %s" % s.upper())

 # Convert everything to lowercase
 print("String in lowercase: %s" % s.lower())

 # Check how a string starts
 if s.startswith("Str"):
     print("String starts with 'Str'. Good!")

 # Check how a string ends
 if s.endswith("ome!"):
     print("String ends with 'ome!'. Good!")

 # Split the string into three separate strings,
 # each containing only a word
 print("Split the words of the string: %s" % s.split(" "))
