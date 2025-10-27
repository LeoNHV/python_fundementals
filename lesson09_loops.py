# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
# 
print()
print("--- Loops in Python ---")
#Iteration
#Iterate
# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).
import time

animals = ["lamb", "sheep", "cow", "goose", "donkey" ]
animals[0]
print("\nOur animals:", animals)
print("\n--- For Loop: visiting each animal ---")

for animal in animals:
    print(animals)
    print("Now petting a", animal)
    time.sleep(0.1)

    if animal == "sheep":
        print("Hi shep!")
    print("\nNow I have petted all the animals.")
print("test")


for i in range(2, 11, 2):
    print("")

    names = ["john, bob"]
    for name in names:
        for num in range(2, 11, 2):
#     print("Even number:", num)
# print("Loop ended. Evens appreciated.")

            print("--- Iterating over strings ---\n")

fav_word = "Shenanigan"
letter_list = []


for letter in fav_word:
    print(letter, end="!")

print()

# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------

# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 

count = 0
while count < 5:
    print(f"We are loopin'. We are on a loop # {count}.")
    count += 1
    time.sleep(0.5)
print("We have escaped the loop!")

user_input = ""

while user_input != "exit":
    user_input = input("Type 'exit' to escape:")
    while user_input != "exit":
        if user_input == "exit":
            print("Exited")

count = 60
increment = 1

while count > 0:

    print(count)
    exincrement =+ 1
    if count < 0:
        break

    count -= increment
    increment += 1

   