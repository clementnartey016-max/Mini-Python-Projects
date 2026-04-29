# Dictionary of usernames and passwords
users = {
    "admin": "1234",
    "clement": "CleNart016",
    "asarf": "nixalabs",
    "root": "12345",
    "user": "1987",
    "george": "maxgeor",
    "john": "abc123",
    "mary": "secure99"
}

# Set attempts for login
attempts = {user: 0 for user in users}

max_attempts = 3

while True:

    # Name Input
    name = input("Enter Your Name: ")
    while name == "":
      print("Username Cannot Be Empty")
      name = input("Enter Your Name: ")

     # Check if username exists
    if name in users:

     # Check if account is locked
     if attempts[name] >= max_attempts:
        print(f"Account '{name}' is locked. Contact admin.")
        continue  # back to the start
 
      #Password input
    password = input("Enter Your Password: ")
    while password == "":
        print("Password Cannot Be Empty")
        password = input("Enter Your Password: ")

    # Check for names in users
    if name in users:

        # Check password
        if users[name] == password:
            print(f"Login Successful {name}")
            break
        else:
         attempts[name] += 1
         remaining = max_attempts - attempts[name]
        print(f"Incorrect password. Attempts left: {remaining}")
        if attempts[name] >= max_attempts:
         print(f"Account '{name}' is now locked.")

else:
    print("Username not found.")