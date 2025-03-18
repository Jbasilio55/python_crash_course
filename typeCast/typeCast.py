#type casting = covert the data type of a value to another data type

x = 1   #int
y = 2.0 #float
z = "3" #str

x = float(x)
y = int(y) # changed float to int
z = int(z) # this will change the string to int

print(x)
print(y)
print(z * 3) #since the str has been change to int, it can now be multiplied by 3

y = str(y)
print(y)