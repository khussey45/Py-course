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


# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are too old")
# elif age >= 18:
#     print("you are an adult")
# elif age < 0:
#     print("You haven't been born yet! ")
# else:
#     print("You are a child!") 

# logical operators (and, or, not) = used to check if two or more conditional statements are true

# temp = int(input("What is the temperature outside?: "))

# if not(temp >=0 and temp <= 30): 
#     print("the temperature is good today!")
#     print("go outside!")
# elif not(temp < 0 or temp >30):
#     print("the temperature is bad today!")
#     print("stay inside!")

# while loop = a statement that will execute it's block of code, as long as it's condition remains true

# name = ""

# while len(name) == 0:
#     name = input("Enter your name: ")

# print("Hello " + name)


# for loop = a statement that will execute it's block of code a limited amount of times

# for i in range(10):
#     print(i + 1)

# for i in range(50,100 +1,2):
#     print(i)


# for i in "Bro Code":
#     print(i)

# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end ="")
#     print()



# Loop control statements = change a loops execution from its normal seqeunce 

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break
