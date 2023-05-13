####  Dictionaries  ####

user = {"first_name":"Ada"}
print(user)

# or if you are going to be adding the contents of the dictionary later, you can 
# declare an empty dictionary. You can create an empty dictionary in two ways:

# Assigning {} to a variable, for example:

account_details = {}

# or use the dict() constructor:

account_details = dict()

#### Read ####

# To read the value associated with a key, you need to provide the name of the 
# dictionary and the the value of the key inside square brackets.
user = {"first_name":"Ada"}
print(user["first_name"])

#####  Update  ####

# Add a key-value

# Dictionaries are mutable, which means they can be changed after you create them. 
# You can add, update or delete the key-value pairs in a dictionary.

# To add an additional key-value to a dictionary, provide the dictionary name, 
# the new key in [] and a value after an = sign.

user["family_name"] = "Bryon"
print(user)

#### Modify a value ####

# To modify a value in a similar way to adding it. You provide the new value 
# after the = sign.

user ["family_name"] = "Lovelace"
print(user)

#### Delete a Key-Value Pair ####

# To remove a key-value pair you use the del statement with the name of the 
# dictionary and the key you want to delete.
del user["family_name"]
print(user)


