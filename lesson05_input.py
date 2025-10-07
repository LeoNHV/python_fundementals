# print("\n--- User Input Documentation---")
# name = input("Enter your name")
# print(name)

# age = int(input("Enter Your Age"))


# age_number = int(age)
# print("Next year, you will be:", age_number + 1)
# print(type(age_number))

# height = float(input("Enter your height in meters: "))
# print("You are", height, "meters tall.")
# print("Next year you will be ", age_number + 1)

# color = input("Enter your favorite color")
# print("Your favorite color is" , color)

# number1 = int(input("Enter 1 number:"))
# number2 = int(input("Enter another number:"))

# sum = number1 + number2

# print("The sum of both numbers is: ", sum)

# diameter = int(input("Enter a number:"))
# area = 3.14 * ((diameter / 2) ** 2) 
# print('The area is:', area)

import random
sides = int(input("How many sides do you want the die to have?"))
roll = random.randint(1, sides)
print("You rolled a", roll)