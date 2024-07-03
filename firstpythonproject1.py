
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




