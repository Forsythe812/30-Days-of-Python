# Day 1
# Reviewing python basics
# 1. Python Syntax
# 2. Data Types 
#   int, str, float, bool

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

# Addition of both num 1 and num2
sum = num1 + num2

# Difference of both num 1 and num2
difference = num1 - num2

# Product of num 1 and num2
product = num1 * num2

# Divison of num 1 and num2
division = num1 / num2 if num2 != 0 else "Undefined (divison by zero)"

# Display result and data types
print(f"Sum : {sum}, Type : {type(sum)}")
print(f"Difference : {difference}, Type : {type(difference)}")
print(f"Product : {product}, Type : {type(product)}")
print(f"Division : {division}, Type : {type(division)}")

print("\n")

# Playing with strings

sample_string = "python programming is ezzz"

print(sample_string.capitalize())

print(sample_string.replace("ezzz","reported"))

sample_string_2 = "python!is!ez!gg"

words = sample_string_2.split("!")

print(words)

# Asking user for their first name, last name, age and favorite number
# first_name = input("Please enter your First name : ")
# last_name = input("Please enter your Last name : ")
first_name = "Barrack"
last_name = "Obama"

while True :
    try :
        age = int(input("Please enter your age : "))
        if age < 0 :
            raise ValueError
        break
    except ValueError :
        print("Input invalid")

while True :
    try :
        favorite_number = int(input("Please enter your favorite number : "))
        break
    except ValueError :
        print("Input invalid")

if (age < 20) :
    print("Hey",first_name+" "+last_name+" ,you're still a teenager")
elif (age >=20 and age < 30) :
    print("Hello",first_name+" "+last_name+" ,enjoying your twenties?")
else :
    print("Greetings",first_name+" "+last_name+" ,age is just a number")

print("Your favorite number squared is :", favorite_number*favorite_number)
