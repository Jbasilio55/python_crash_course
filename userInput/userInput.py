name = input("What is your name?: ")
age = input("What if your age?: ")
height = float(input("What is your height?: "))

age = int(age) + 1  # when you are getting an input it will always be saved in string format
                    # so to get an int, you will need to type convert the str to int

print("Hello " + name)
print("You are " + str(age) + " years old.") # cast back to str to concatenate str
print("You are " + str(height) + " cm tall.")