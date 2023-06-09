#### Integers ####

# An integer is a whole number such as 50. The data type integer is abbreviated 
# to int.

#### Floating point numbers ####

# A floating point number is a number followed by a decimal point such as 50.5.

####  Using Number Variables in Strings  ####

# In the previous section on strings you learnt that you can use the + to add 
# strings together to form sentences. You also learned that you can insert 
# variables into a sentence using the {}.

# What happens if we try to use a number with these two different methods?
# Try the following code.
my_int = 50
sentance = "The total comes to: "
###   print(sentance + my_int)   ###

#### Answer:
### TypeError: can only concatenate str (not "int") to str ###

# TypeErrors are very common when you are learning python. Python is telling 
# you that you are trying to use a data type that will not work. In this case 
# you cannot add a string and a number together.

# Fix the error by converting the int data type to a str data type.
my_int = 50
sentance = "The total comes to: "

print(sentance + str(my_int))

# We have used the str() method to convert the variable from an integer to a 
# string. In most cases python will determine the type of data without having to 
# declare it. However, it can be useful to tell python exactly how you want to 
# treat the data type. Other examples are:

# str() returns a string object
# int() returns an integer object
# float() returns a floating point object
# bool() a boolean value of True or False
