# logical operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside? (°F): "))

if temp >= 50 and temp <= 75: #both conditions must be true
    print("The temperature is good today!")
    print("Enjoy the weather.")
elif not(temp < 110):
    print("Do not exit, it is terrible outside. ")
elif temp < 50 or temp > 75: # only one needs to be true
    print("The weather is bad today!")
    print("Stay in doors.")