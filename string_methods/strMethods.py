name = "jorge"

print(len(name)) # <-- this str method allows us to get the length of the string
print(name.find("j")) # <-- this method allows to to find a certain character in the string
print(name.capitalize()) # <-- this allows you to capitalize the string
print(name.upper()) # <-- this will allow you to change all the chars to uppercase
print(name.lower()) # <-- this will allow you to change all the chars to lowercase
print(name.isdigit()) # <-- this will allow you to know if the variable is a digit (returns a true or false)
print(name.isalpha()) # <-- this will allow you to know if the variable is a alphabetical characters (returns a true or false)
print(name.count("e")) # <-- this will allow you to know how many particular character is in the string
print(name.replace("r", "d")) # <-- this will allow you to change a particular letter wil another one

print(name * 3) # <-- this will allow you to display string, multiple times depending on number | ( __ * number )