# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start: strop: step]

name = "Jorge Basilio"

first_name = name[0:5] # you can also write name[:5], leaving start blank will automatically start at 0
print(first_name)

last_name = name[6:] # you can also do name[6:13]
print(last_name)

even_digit_letters = name[::2]
print(even_digit_letters)

reversed_string = name[::-1]
print(reversed_string)

website = "https://google.com"
website2 =  "https://wikipedia.com"

slice = slice(8, -4)
print(website[slice])
print(website2[slice])