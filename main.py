# first_name = "Kieren "
# last_name = "Hussey"
# full_name = first_name + last_name

# print("Hello " + full_name)

# age = 21
# age += 1
# print("Your age is: "+str(age))

# height = 250.5
# print(height)
# # print(type(height))
# print("Your height is: " +str(height) + "cm" )

# human = False
# # print(type(human))
# print("are you a human: " +str(human))



# multiple assignment = allows us to assign multiple variables at the same time in one line of code


# name = "Bro"

# print(name.find("r"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("O"))
# print(name.replace("O", "a"))
# print(name*3)

# type casting = converting the data type of a value to another data type

# name = input("What is your name?: ") 
# age  = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))

# print("Hello " + name )
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + "cm tall")



# import math 

# pi = -3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(420))
# print(max(x,y,z))\
# print(min(x,y,z))




# slicing = create a substring by extracting elements from another string indexing[] or slice() [start:stop:step]

# name = "Bro Code"

# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[0:8:3]
# reversed_name = name[::-1]

# print(reversed_name) 

# website  = "http://google.com"

# slice  = slice(7,-4)

# print(website[slice])


age = int(input("How old are you?: "))
if age == 100:
    print("You are too old")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("You haven't been born yet! ")
else:
    print("You are a child!")

