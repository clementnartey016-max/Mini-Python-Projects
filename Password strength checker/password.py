# PASSWORD STRENGTH CHECKER
password = input("Enter Your Password: ")

length = len(password)
symbols = "!@#$%^&*"

has_upper = False
has_lower = False
has_number = False
has_symbol = False

# CHECK CHARACTER TYPES
for letter in password:
    if letter.isupper():
        has_upper = True
    elif letter.islower():
        has_lower = True
    elif letter.isdigit():
        has_number = True
    elif letter in symbols:
        has_symbol = True

# COLLECT MISSING INFO
missing = []
if not has_upper:
    missing.append("capital letter")
if not has_lower:
    missing.append("lowercase letter")
if not has_number:
    missing.append("number")
if not has_symbol:
    missing.append("symbol")


# CHECK COMMON PASSWORDS
common_passwords = ["123456","password","incorrect","abc123","querty"]
is_common = password in common_passwords


# FINAL DECISION
if length >= 8 and not missing and not is_common:
    final_strength = "Very Strong Password"
elif length >= 6 and len(missing) <= 1:
    final_strength = "Strong Password"
else:
    final_strength = "Weak Password"
#check score or score password
score = 0
if has_lower:
    score += 20
if has_symbol:
    score += 30
if has_upper:
    score += 25
if has_number:
    score += 25



# PRINT ONLY ONCE
print("\nPassword Analysis:")
print(f"Password Length: {length}")
print("Password Score:", score, "/100")
if missing:
    print("Missing:", ", ".join(missing))
if is_common:
    print("Warning: This password is too common!")
print("Final Strength:", final_strength)

