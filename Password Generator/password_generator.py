import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

# 1. Start with an empty string
user_input = ""

# 2. Check the string BEFORE converting to int
while user_input == "":
    user_input = input("Enter password length: ")
    if user_input == "":
        print("Error: You Did Not Enter Your Length")

# 3. Now that we have data, convert it safely
length = int(user_input)

characters = lowercase + uppercase + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated password:", password)