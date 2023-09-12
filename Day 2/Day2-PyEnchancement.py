'''
Day 2
String manipulation
'''
name = input("What's your name? ").lower()
# Name at lowercase
print(name)

# Name to Capitalize
print("Hello " + name.capitalize() + "!")

# String manipulation
replaced_name = name.replace('a','x')
print(f"Name after replacing 'a' with 'x': {replaced_name}")

name_parts = name.split(" ")
if len(name_parts) > 1:
    print(f"Your name has been split into: {name_parts}")

