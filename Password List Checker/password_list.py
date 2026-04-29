weak_passwords = ["123456","123abc","abcde","abcd",
                  "clement","2468","querty","123abc",
                  "admin","welcome","password","incorrect",
                  "hi","eye","abcd","alpha","xyz","money","wifi","orange",
                  "banana","bamboo","pineapple","alert","error",
                  "security","key","lock","grind","hi","greetings"
                  "flip","offensive","defensive","analyst","cloud"]

# Normalize weak password list to lowercase
weak_passwords_lower = [pwd.lower() for pwd in weak_passwords]

password = input("Enter Your Password: ")
while password == "":
    print("You Did Not Enter Your Password!")
    password = input("Enter Your Password: ")

# Normalize input to lowercase
password_lower = password.lower()

# Minimum length check
if len(password) < 8:
    print("Warning: Password is too short (less than 8 characters).")

if password_lower in weak_passwords_lower:
    print("Password found in common password list. (WEAK PASSWORD)")
else:
    print("Password not found in common password list.")