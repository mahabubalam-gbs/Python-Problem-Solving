# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# length = float(input("Enter the length: "))
# print(name, age, length)

# expression1 = eval(input("Enter any equation here: "))
# print(expression1)
#
# expression2 = eval(input("Enter any equation here: "))
# print(expression2)
#
# f_name = "John"
# n_age = 32
# print(type(f_name), type(n_age))


# Type casting

# a = 123
# b = 12.3
#
# print(type(a))
# print(type(b))
# print(type(a + b))

# x = "123"
# y = 234
#
# z = x + y
# print(z)
# print(type(z))

# p = 12
# q = 15
# p,q = q, p
# print(p, q)
#
# stu_name = input("Enter the student name: ")
# grade = input("Enter the grade of the student: ")
# stu_age = int(input("Enter the age of the student: "))
# email = input("Enter your email: ")
# ph_number = int(input("Enter the phone number: "))
# print("Student Identity Card")
# print("Name: ", stu_name)
# print("Grade: ",grade)
# print("Age: ",stu_age)
# print("Email: ",email)
# print( "Phone: ",ph_number)


# Arithmetic Operator (exponentiation (**) --> Power), (floor division(//))

# power = 5**2
# print(power)
#
# modulus = 15 % 2
# print((modulus))
#
# floor_division = 15 // 2
# print(floor_division)
#
#
#
# a = 1234
# b = "1234"
# print(a is not b)
#
# c = 1234
# d = 1234
#
# print(c is d)
# print(bin(155))


# print(115 & 155)
# a = 10
# b = 8
# print(a & b)

# x = 2
# y = x
# 
# print(x is y)
# 
# a = 10
# b = 8
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(10 >> 2)
# print(10 >> 1)
# print(10 << 1)
# print(10 << 2)


# membership operators
# word = "hello"
# print("e" in word)
# print("f" in word)
# print("x" not in word)
# print("o" not in word)

# marks = 50
#
# if marks >= 90:
#     print("You will get a mobile phone")
# print("Thank you")
#
# if marks >=90:
#     print("You will get a phone")
# else:
#     print("no for 1 week")
# print("Thank you")
#
# if marks >= 90:
#     print("You can go to a trip")
# elif marks >= 80 and marks <90:
#     print("you will get a new phone")
# elif marks >=70 and marks <80:
#     print("You will get a new book")
# else:
#     print("You will not get your phone back")

# marks = 95
#
# if marks >=80:
#     print("You will get a new phone")
#     if marks >=95:
#         print("You can go to a trip")
# else:
#     print("no phone for a month")

# short hand if statement

# marks = 95
# if marks >=90: print("you will get a new phone")


# short hand if-else statement
# marks = 90
# print("you will get a new camera") if marks >= 95 else print("you will have to study hard")


# num = int(input("enter a number here: "))
# if num >0:
#     print(num, "is a positive number")
# else:
#     print(num, "is a negative number")

# number = int(input("enter a number here: "))
# if number % 2 == 0:
#     print(number, "is an even number")
# else:
#     print(number, "is a odd number")

# area calculator
#
# print("***** AREA CALCULATOR*****")
# print("""Press 1 to get the area of square
# Press 2 to get the area of rectangle
# Press 3 to get the area of circle
# Press 4 to get the area of triangle""")
#
# choice = int(input("enter a number between 1-4: "))
#
# if choice == 1:
#     side = float(input("enter the length of one side: "))
#     area = side**2
#     print("The area of the square is ", area)
#
# elif choice == 2:
#     length = float(input("enter the length of the rectangle: "))
#     width = float(input("enter the width of the rectangle: "))
#     area = length * width
#     print("The are of the rectangle is ", area)
#
# elif choice == 3:
#     radius = float(input("enter the radius of the circle: "))
#     area = (22/7) * (radius**2)
#     print("The area of the circle ", area)
# elif choice == 4:
#     base = float(input("enter the base of the triangle: "))
#     height = float(input("enter the height of the triangle: "))
#     area = 0.5 * base * height
#     print("The area of the triangle is ", area)
#
# else:
#     print("Invalid input")

# letter = input("enter a letter: ")
# if letter in "aeiou" or letter in "AEIOU":
#     print(letter, "is a vowel")
# else:
#     print(letter, "is not a vowel")

# identify the digits of a number

# num = int(input("enter a number here upto 5 digits: "))
#
# if num >=0 and num <=9:
#     print("It is a single digit number")
# elif num >=10 and num <=99:
#     print("It is a double digits number")
# elif num >=100 and num <=999:
#     print("It is a three digits number")
# elif num >=1000 and num <=9999:
#     print("It is a four digits number")
# else:
#     print("It is a five digits number")


# For loop

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# for letter in "banana":
#     print(letter)
#
# fruit_lists = ["apple", "banana", "cherry"]
# for fruit in fruit_lists:
#     print(fruit)
#     if fruit == "banana":
#         break
#
# my_fruits = ["apple", "banana", "cherry"]
# for fruit in my_fruits:
#     if fruit == "banana":
#         break
#     print(fruit)
#
# fav_fruits = ["apple", "banana", "cherry"]
# for fruit in fav_fruits:
#     if fruit == "banana":
#         continue
#     print(fruit)
#
# for x in range(2, 11, 2):
#     print(x)
#
# for x in range(6):
#     print(x)
# else:
#     print("finally finished")
#
# for x in range(6):
#     if x == 3: break
#     print(x)
# else: print("finally finished")
#
# adj = ["red", "big", "tasty"]
# popular_fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in popular_fruits:
#         print(x, y)
#
# for x in [0, 1, 2]:
#     pass
#
# i = 1
# while i <6:
#     print(i)
#     i += 1
#
# j = 1
# while j < 6:
#     print(j)
#     if j == 3:
#         break
#     j += 1
#
# k = 0
# while k < 6:
#     k += 1
#     if k == 3:
#         continue
#     print(k)
#
# l = 1
# while l < 6:
#     print(l)
#     l += 1
# else:
#     print("l is no longer less than 6")

# n = 1
# a = int(input("enter a number here: "))
#
# while n <= 10:
#     print(a, "x", n, "=", n*a)
#     n +=1
# else:
#     print("multiplication has ended")

# while True:
#     num1 = int(input("enter a number here: "))
#     num2 = int(input("enter another number here: "))
#     print(num1 + num2)
#     repeat = input("If you want to stop the program, type - yes: ")
#     if repeat == "yes":
#         break

# for i in range(1,4):
#     for j in range(1,11):
#         print(j)
#     print("rep", i, "completed")
# print("congrates!, you have completed your target")
# 
# for i in range(1,3):
#     for j in range(1, 11):
#         print(j, end="")
#     print()

# Pattern
# for i in range(1,6):
#     for j in range(1,1+i):
#         print(j, end=" ")
#     print()

# For/while loop with conditional statements

# for i in range(1, 101):
#     if i%8 == 0 and i%12==0:
#         print(i)
#
# n = 1
# while n <=10:
#     if n == 3:
#         print("add this to favs")
#     else:
#         print(n)
#     n +=1

# continue = skip
# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i)
# # break = stop
# for i in range(1, 11):
#     if i == 7:
#         break
#     else:
#         print(i)
# print("Thank you")

# problem solving
# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         sum += i
# print("The sum of all the even numbers upto 50 is",sum)

# write a program to create a billing system at supermarket:

# while True:
#     name = input("enter customer's name: ")
#     total = 0
#     while True:
#         print("enter the amount and quantity")
#         amount = float(input("enter amount: "))
#         quantity = int(input("enter quantity: "))
#         total += amount * quantity
#         repeat = input("Do you want to add more items? (yes/no): ")
#         if repeat == "no" or repeat == "NO":
#             break
#     print("_"*40)
#     print("Name: ", name)
#     print("Amount to be paid: ", total)
#     print("_"*40)
#     print("******* Happy Shopping*******")
#     repeat1 = input("Do you want to go to the next customer? (yes/no): ")
#     if repeat1 == "no" or repeat1 == "NO":
#         break

# write a program to check how many times alphabet o is occurring.
# sentence = "Why fit in, When you are Born to Stand Out!"
# print(sentence.count("o"))
# print(sentence.lower())
# print(sentence.upper())
# print(sentence.title())
# # finding index number of "fit in"
# print(sentence.find("fit in"))

# Patterns
# for i in range(1, 6): # rows
#     for j in range(1, i + 1): # columns
#         print("*", end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1, i +1):
#         print(i, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(6, i, -1):
#         print(i, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()
#
# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# for k in range(1,5):
#     for l in range(5, k, -1):
#         print("*", end=" ")
#     print()

for i in range(1,9):
    for j in range(1, i+1):
        print(i*j, end=" ")
    print()
paragraph = """I am applying to the MSc in International Business and Trade because it aligns directly with my long-term goal of establishing an import-export consultancy business in my home country. With a strong academic foundation in finance, graduating with a CGPA of 3.83/4.0 and being placed five times on the Vice Chancellor’s List and twice on the Dean’s List, I have developed the analytical ability and discipline required for an advanced international programme.
Professionally, my experience has consistently centred on global engagement and international market coordination. As IT & International Partnership Manager at Asia Admission Center, I manage and expand partnerships with universities across different regions, lead CRM and digital process improvements, and monitor global education market trends to support strategic decisions. Previously, in my role as Digital Operations & Business Development Officer at Hai Education, I worked on market research, performance analytics, and international recruitment strategies. These roles have strengthened my understanding of cross-border operations, market dynamics, and relationship management — skills directly transferable to international trade and consultancy.
I am also building strong data and analytical abilities, which support evidence-based decision-making in global business environments. This combination of academic merit, international partnership experience, and analytical strengths has prepared me to contribute meaningfully to the programme.
The MSc in International Business and Trade will provide me with advanced knowledge of trade policies, global market structures, and international business strategy — expertise essential for advising firms on export opportunities, market entry, and competitive positioning. The diverse cohort and practical coursework will further help me develop a global perspective. I am confident that my motivation, international exposure, and goal-oriented mindset will allow me to be an asset to the programme while shaping my path toward building a successful import-export consultancy in the future.
"""
count = 0
for letters in paragraph:
    print(letters)