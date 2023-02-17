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

# break     = used to terminate the loop entirely
# continue  = skips to the next iteration of the loop
# pass      = does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number: 
#     if i == "-":
#         continue
#     print(i)

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)


# list = used to store multiple items in a single variable 

# food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

# food[0] = "sushi"

# # food.append("ice cream")
# # food.remove("hotdog")
# # food.pop()
# # food.insert(0,"cake")
# # food.sort()
# # food.clear()

# for x in food: 
#     print(x)



# 2D lists = a list of lists(multi-demensional lists)

# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","hamburger","hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[2][2])


# tuple = collection which is ordered and unchangeable used to group together realted data

# set = collection which is unordered, unindexed. No duplicate values

# utensils  = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}

# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear()
# # dishes.update(utensils)
# # dinner_table = utensils.union(dishes)

# print(utensils.difference(dishes))


# for x in dinner_table:
#     print(x)

# dictionary = A changeable, unordered collection of unique key: value pairs, fast because they use hashing, allow us to access a value quickly 



# capitals = {'USA':'Washington DC',
#             'India':'New Dehli',
#             'China':'Beijing',
#             'Russia':'Moscow'}

# capitals.update({'Germany':'Berliin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# # print(capitals['Germany'])
# # print(capitals.get('Germany'))
# # print(capitals.keys())
# # print(capitals.values())
# # print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)


# index oeprator [] = gives access to as sequence's elemt (str,list,tuples)

# name = "bro Code!"

# # if (name[0].islower()):
# #     name = name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:].lower()
# last_character = name[-1]

# print(first_name)
# print(last_name)
# print(last_character)

# function = a block of code which is executed only when it is called

# def hello(name):
#     print("hello " + name)
#     print("Have a nice day!")

# hello("Bro")

# return statement = Functions send Python values/objects back to the caller. These values/objects are known as the functions's return value

# def multiply(number1, number2):
#     return number1 * number2

# x = multiply(6,8)

# print(x)

# keyword arguments = arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments Python knows the name of the arguments that our function receives 

# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)

# hello(last="code",middle="Dude",first="Bro")


# nested function calls = function calles inside other function calls. Innermost function calls are resolved first returned value is used as argument for the next outer function 

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num) 

# print(round(abs(float(input("Enter a whole positive number: ")))))


# scope = The region that a variable ir recognized. A variable is only available from inside he region it is created.  A global and locally scoped versions of a variable can be created

# name = "Bro" # global scope (available inside & outside functions)

# def display_name():
#     name = "Code" # local scope (available only inside this function)
#     print(name)

# display_name()
# print(name)


# *args  = paramter that will pack all arguments into a tuple useful so that a functon can accept a varying amount of arguments 

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum

# print(add(1,2,3,4,5,6,7,8))

# **kwargs = parameter that will pack all arguments into a dictionary useful so that a function can accept a varing amount of keyword arguments

# def hello(**kwargs):
#     print("Hello " + kwargs['first']+ " " + kwargs['last'])

# hello(first="Bro",middle="Dude",last="Code")

# str.format() = optional method that gives users more control when displaying output

# number = 1000

# # print("The number pi is {:.3f}".format(number)) 
# # print("The number is {:,}".format(number))
# # print("The number is {:b}".format(number))
# # print("The number is {:o}".format(number))
# # print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))

# import random

# x = random.randint(1,6)
# y = random.random()

# myList = ['rock','paper','scissors']
# z = random.choice(myList)

# cards = [1,2,3,4,5,6,7,8,9,"J","q","k","A"]

# random.shuffle(cards)

# print(cards)


# exception = events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input('Enter a number to divide by: '))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print("You can't divide by 0 idiot")
#     print(e)
# except ValueError as e:
#     print("Enter only numbers plz")
#     print(e)
# except Exception as e:
#     print("something went wrong")
#     print(e)
# else:
#     print(result)
# finally:
#     print("This will always execute")

    
# import os

# path = "C:\\Users\\kiere\\OneDrive\\Desktop\\Py-code"

# if os.path.exists(path):
#     print("That location exists!")
#     if os.path.isfile(path):
#         print("Thats a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("That location doesn't exist!")

# minipluating files