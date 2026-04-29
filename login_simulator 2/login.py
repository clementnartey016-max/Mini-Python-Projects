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
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    # Ask for user input
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")

    # Check for names in users
    if name in users:

        # Check password
        if users[name] == password:
            print(f"Login Successful {name}")
            break
        else:
            print("Wrong Password")
            attempts += 1

    else:
        print("Username Not Found")
        attempts += 1

# If max attempts reached
if attempts == max_attempts:
    print("Account Locked")