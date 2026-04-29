Password List Checker
Overview

The Password List Checker is a Python console application that verifies whether a user-provided password exists in a list of weak or common passwords. It is case-insensitive and allows continuous checking, making it a practical tool for beginners to learn Python input handling, loops, and list operations while simulating real-world security practices. The project focuses on simplicity, accuracy, and scalability.

Features
1.Case-insensitive password verification: Matches passwords regardless of capitalization.
2.Continuous checking: Test multiple passwords without restarting the program.
3.Empty input validation: Ensures the user cannot enter a blank password.
4.Optional file-based password list: Expandable to large datasets for more realistic testing.
5.Clean exit option: Users can type exit to terminate the program gracefully.


How It Works
1.The user runs the program.
2.The program prompts the user to enter a password.
3.The input is normalized to lowercase to ensure case-insensitive checking.
4.The password is compared against the weak password list (also normalized).
5.The program prints whether the password is found in the weak list or not.
6.The user can continue checking additional passwords or type exit to quit.


How to Use
1.Run the Python script.
2.Enter the password you want to check.
Example: 123456 → Weak password found
Example: MySecurePass → Password not found
3.Continue entering passwords as needed.
4.Type exit to close the program.