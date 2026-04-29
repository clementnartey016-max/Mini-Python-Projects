#Get Password From User
password = input("Enter Your Password: ")

#length of password
length = len(password)

symbol = "!@£$%^&*"
has_symbol = False
has_upper = False
has_lower = False
has_number = False

#Check if characters are in password
for letter in password:
    if letter.isupper():
        has_upper = True
    if letter.islower():
        has_lower = True
    if letter.isdigit():
        has_number = True
    if letter in symbol:
        has_symbol = True

#Check For Missing letters - REMOVED the () because these are variables, not functions
missing = []
if not has_symbol:
    missing.append("Symbols")
if not has_lower:
    missing.append("Lowercase")
if not has_upper:
    missing.append("Uppercase")
if not has_number:
    missing.append("Numbers")

#Calculate a score for the password - Changed =+ to += so it actually adds up
score = 0
if length >= 8: score += 20
if has_lower: score += 20
if has_number: score += 20
if has_upper: score += 20
if has_symbol: score += 20

#Check Data Breach Function
def check_breach(password):
    try:
        with open("common_password.txt", "r") as f:
            for line in f:
                if password == line.strip():
                    return True
    except FileNotFoundError:
        return "File Not Found"
    return False

#Final Decision - FIXED the red line by adding 'and' and correcting the missing len check
if length >= 8 and not missing:
    final_strength = "Very Strong Password"
elif length >= 6 and len(missing) <= 1: # Added 'and' here to fix your red line
    final_strength = "Strong Password"
else:
    final_strength = "Weak Password"

#Show results
print("\n" + "="*30)
print("PASSWORD SECURITY REPORT")
print("="*30)
print(f"Password Length: {length}")
print(f"Security Score:  {score}/100")

if missing:
    print(f"Missing Requirements: {', '.join(missing)}")
else:
    print("Requirements: All met! ✅")

print(f"Complexity Rank: {final_strength}")

# --- THE BREACH PRINT PART ---
breach_status = check_breach(password)

if breach_status == True:
    print("\n🚨 BREACH ALERT: This password was found in the common list!")
    print("RESULT: COMPROMISED (Do not use this password)")
elif breach_status == "File Not Found":
    print("\n⚠️ ERROR: 'common_password.txt' not found. Create the file to check breaches.")
else:
    print("\n✅ BREACH STATUS: No matches found in the common list.")
print("="*30)

