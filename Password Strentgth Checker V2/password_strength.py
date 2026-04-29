# Ask User To Input Password
password = input("Enter Your Password: ")

# Check The Length Of The Password
length = len(password)

# Define Checks
symbols = "!@#$%^&"
has_symbols = False
has_upper = False
has_lower = False
has_numbers = False

# Loop Through Password
for letter in password:
    if letter.isupper():
        has_upper = True
    elif letter.islower():
        has_lower = True
    elif letter.isdigit():
        has_numbers = True
    elif letter in symbols:
        has_symbols = True

# Check Missing Requirements
missing = []
if not has_upper:
    missing.append("Upper Case")
if not has_lower:
    missing.append("Lower Case")
if not has_symbols:
    missing.append("Symbols")
if not has_numbers:
    missing.append("Numbers")

# Score Calculation
score = 0
if has_lower:
    score += 25
if has_numbers:
    score += 30
if has_upper:
    score += 25
if has_symbols:
    score += 20

# Read Weak Passwords
weak_list = []
with open("weak_password.txt", "r") as f:
    for line in f:
        weak_list.append(line.strip())

# Read Strong Passwords
strong_list = []
with open("strong_password.txt", "r") as f:
    for line in f:
        strong_list.append(line.strip())

# Check Lists
if password in weak_list:
    print("Found In Weak Passwords")
elif password in strong_list:
    print("Found In Strong Passwords")

# Final Strength Logic
if length >= 8 and not missing:
    final_strength = "Very Strong Password"
elif length >= 6 and len(missing) <= 1:
    final_strength = "Strong Password"
else:
    final_strength = "Weak Password"

# Output
print("\nPassword Analysis:")
print(f"Password Length: {length}")
print(f"Password Score: {score}/100")

if missing:
    print("Missing:", ", ".join(missing))

print("Final Decision:", final_strength)