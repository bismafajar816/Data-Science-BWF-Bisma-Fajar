#Simple print
print("Bytewise FellowShip")
#Variable print
number = 7
print(number)
#Case change
name = "bisma fajar"
print(name.title())
print(name.upper())
print(name.lower())
#Concatenation
first_name = "Bisma"
last_name = "Fajar"
full_name = first_name + " " + last_name
print(full_name)
#Tab and new line
print("\t" + full_name)
print("Hello, " + full_name + "!")
#Remove whitespace
name = " Bisma Fajar "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#String and integer
age = 19
print("My age is " + str(age) + " years old.")
#Comments
#This is a comment
print("This is not a comment")
#Multiple line comments
#Operators
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
#Conditions
age = int(input("Enter your age: "))
if age!=18:
    print("You are not 18.")
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Multiple conditions
#Else if
if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You are a teenager.")
else:
    print("You are a child.")
    
#List
#Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)
#Accessing elements
print(fruits[1])
#Changing elements
fruits[1] = "orange"
print(fruits)
#Adding elements
fruits.append("banana")
print(fruits)
#Removing elements
fruits.remove("banana")
print(fruits)
#Looping through a list
for fruit in fruits:
    print(fruit)



