# variable = a container for a value. Behaves as the value that it contains

# Much like algebra - solving for x
# Algebra ->    10 = 5^x 
#               x = 2 
#               
# But for variables they are not limited by just numbers
# They can be numbers, booleans, words / letters and so on..

first_name = "Jorge"  # <-- String = a series of characters denoted by using single quotes ' ... ' or double quotes " ... "
last_name = "Basilio"
full_name = first_name + " " + last_name # <-- this is referred to as string concatenation | adding string together
number = 8      # <-- 

print(first_name) # print variable containing name
print(type(last_name)) # <-- type() will tell you the type of object you are using | ex. <class: 'str'>
print("Hello " + full_name) # you can print string literal "Hello" + variable containing string
print(full_name)

age = 35 # <-- regular non decimal numbers are called integers (int). they can not have quotes or they will be considered a string
age = age + 1 # <-- you can add to integer by using addition sign (+) and adding an integer
age += 1 # <-- this would be the short form of the line above | age += 1 | age = age + 1

print(type(age))
print(age) # <-- the variable of int cant not be added to string

height = 177.8 # <-- float data type is a floating point number (a decimal number)
print(height)
print(type(height))

is_human = True # <-- boolean can only be true or false | true can also represent (1) and false can represent (0)
print(is_human)
print(type(is_human))