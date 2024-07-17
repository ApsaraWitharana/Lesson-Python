
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

 print("==============")

 # Day 5 ---> Conditions

 # Notice that variable assignment is done using a single equals operator "=",
 # whereas comparison between two variables is done using the double equals operator "==". The "not equals" operator is marked as "!=".

 x = 2
 print(x == 2) # prints out True
 print(x == 3) # prints out False
 print(x < 3) # prints out True

 print("==============")

 # Boolean operators

 name = "Dusvi"
 age = 23
 if name == "Dusvi" and age == 23:
     print("Your name is Dusvi, and you are also 23 years old.")

 if name == "Dusvi" or name == "Hero":
     print("Your name is either Dusvi or Hero.")

print("==============")

 # The "in" operator -The "in" operator could be used to check if a specified object exists within an iterable object container

name = "Dusvi"
if name in ["Dusvi","Hero"]:
 print("Your name is either Dusvi or Hero.")

 print("==============")

 # The 'is' operator =>Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.

 x = [1,2,3]
 y = [1,2,3]
 print(x == y)
 print(x is y)

 print("==============")

 # The "not" operator =>Using "not" before a boolean expression

 print(not False) # Prints out True
 print((not False) == (False)) # Prints out False

 print("==============")

 # Exercise

 number = 16
 second_number = 0
 first_array = [1,2,3]
 second_array = [1,2]

 if number > 15:
     print("1")

 if first_array:
     print("2")

 if len(second_array) == 2:
     print("3")

 if len(first_array) + len(second_array) == 5:
     print("4")

 if first_array and first_array[0] == 1:
     print("5")

 if not second_number:
     print("6")


print("==============")

#Day 6 ---> Loops

 # The "for" loop ->> For loops iterate over a given sequence.

primes = [2, 3, 5, 7]
for prime in primes:
 print(prime)

print("==============")

# Prints out the numbers 0,1,2,3,4
for x in range(5):
     print(x)

# Prints out 3,4,5
for x in range(3, 6):
     print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

print("==============")

# "while" loops

count = 0
while count < 5:
     print(count)
     count += 1
#This is the same as count = count + 1

print("==============")

 # Day -07- Loop
# "break" and "continue" statements =>break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement.

count = 0
while True:
     print(count)
     count += 1
     if count >= 5:
         break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
     # Check if x is even
     if x % 2 == 0:
         continue
     print(x)

print("==============")



#"else" clause for loops=== Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
     print(count)
     count +=1
else:
 print("count value reached %d" %(count))

 # Prints out 1,2,3,4
 for i in range(1, 10):
     if(i%5==0):
         break
     print(i)
 else:
     print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# example
 numbers = [
     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
     743, 527
 ]

 # your code goes here
 for number in numbers:
     if number == 237:
         break

     if number % 2 == 1:
         continue

     print(number)

# ex2

 names = [
     "sachini", "apsara", "duvi", "thathsara", "anu", "sapsara"
 ]

 # Loop through the names list
 for index, name in enumerate(names):
     if name == "anu":
         break

     # Skip every second name
     if index % 2 == 1:
         continue

     print(name)
 print("==============")

# day-08==>>.Functions =>>>Functions are a convenient way to divide your code into useful blocks,
 # allowing us to order our code, make it more readable, reuse it and save some time.
 # Also functions are a key way to define interfaces so programmers can share their code.

 def my_function():
     print("Hello From My Function!")


 print("==============")


 def my_function_with_args(username, greeting):
     print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

 print("==============")

 def sum_two_numbers(a, b):
     return a + b

 print("==============")

 # Define our 3 functions
 def my_function():
     print("Hello From My Function!")

 def my_function_with_args(username, greeting):
     print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

 def sum_two_numbers(a, b):
     return a + b

 # print(a simple greeting)
 my_function()

 #prints - "Hello, Dusvi Till, From My Function!, I wish you a great year!"
 my_function_with_args("Dusvi Till", "a great year!")

 # after this line x will hold the value 3!
 x = sum_two_numbers(1,2)