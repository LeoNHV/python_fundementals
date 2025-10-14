greeting = "Hi"
name = "My sigma"
print(greeting, name)

# 0 1 2 3 4 
# H e l l o

# 0 1 2
# A d a

message = greeting + " " + name + "!!!!"
print("Concatenated message:", message)

print(greeting[1])

word = "supercalifragilisticexpialidocious"

print("first letter ", word[0])
print("Last letter ", word[-1])

print("Range of letter (not-inclusive):", word[-7:-2])
print(word[:-1])
print("skip through every second letter ", word[::-1])

country = "New Jersey" 
length_of_word = len(country)
print(length_of_word)

phrase = "SpOnGEBoB"
print("\nuppercase:", phrase.upper())

sentence = "Im a skibidi rizzler"
new_sentence = sentence.replace("Im", "You're")
print(new_sentence)

Name = "Leo"
age = 67
City = "New Rizzler"

print(f"Hello my name is {Name}. I am {age} years old. I live in {City}.")

print(f"Next year, I'll be {age + 1}. My name in uppercase is {name.upper()}.")

quote = input("Enter a quote: ")
length = len(quote)
print(f"The quote, {quote}, has {length} characters!")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name")
print(first_name.upper(), ", ", last_name.lower())



word = input("Enter a random word: ")
uppercase = word("upper")


