####  Strings  ####

# In python a string, is shortened to str and refers to anything inside quotes. 
# The quotes can be double or single. The examples below are identical to python.
"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'

# If you want to include a direct quote in your sentence, then use single quotes 
# for the string and double quotes for the direct quote. For example:
'The error message was "Incorrect DataType"'

# This allows you the flexibility to use single quotes to wrap the string and 
# double quotes inside the string for a direct quote, without python getting confused.
# Strings, like all data types, can be assigned to a variable.
first_name = "Monty"
last_name = "Python"

# You can add strings together using variables. This concatenates them
print(first_name+last_name)

# You can see that there isn't a space in MontyPython. To include a space, you 
# need to either add it to the beginning or end of your word or add it as a 
# separate string. Fix the sentence below.
print(first_name + " " + last_name)

#### Using Variables in Strings ####

# Imagine we want to use the value of a variable in the middle of a string. 
# This can be done a few ways in python.

####  .format()   ####  

# In this method you can use the {} in your string to indicate where the 
# variable should go. Then use .format(variable_name) after the quotation marks. 
# If you have multiple variables, for each variable you use a {}. In the 
# .format() separate each variable with a comma. For example .format(variable_1,
# variable_2).
first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))

####   f strings  ####

# Since python version 3.6 it has been possible to use a format called f-strings 
# to include variables in your strings. Some people find this format easier to read.
firstname = "Jane"
surname = "Doe"

print(f"My firstname is {firstname}. My family name is {surname}")

#### New Lines and Indentation ####

# If you want your text to go over several lines you can use \n and \t. 
# The \ character is called an escape character.

# The n tells python to put the text on the next line.
# The t tells python to add a tab spacing.
string = "This is a string over\nthree lines\n\twith the third line indented"
print(string)


