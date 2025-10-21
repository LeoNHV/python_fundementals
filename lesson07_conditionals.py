print(3==2)
print(7 != 4)
print(4 > 5)

#if 
num = 10
if num == 10: print("Your number is equal to 10")
num = 5
if num <= 12:
    print("Your number is less or equal to 12")
else: 
    print("you rnumber is greater than 12")
#if elif else

temperature = 72
if temperature > 80:
    print("Its hot!")
elif temperature >= 60:
    print("Its nice.")
else:
    print("Its cold!")

    x = 2
    y = 20

    if x == y:

     print("x is equal to y")
    elif x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
         print("error")

    age = 16
    has_permission = True
    if age >= 17 and has_permission:
        print("You can drive")
    else:
        print("cant drive yet")

        print("---Using 'or' ---")
        day = "Monday"

        if day=="Saturday" or day == "Sunday":
        
             print("Its the weekend!")
        else:
            print("Its the weekday")

input = int(input("Enter a number:"))
if input % 2 == 1:
    print("your number is odd")
else: 
    print("even")
password = "ChickenStars"
input = int("Enter a password")
if password == input:
    print("Acess Granted")
else:
    print("Acess Denied")

input = int("Enter your grade:")
grade = int("You got an A")