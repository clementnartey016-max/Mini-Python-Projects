# Password Strength Checker v2.0 (The Debugging Edition)

## Project Overview
A Python-based security utility designed to analyze password complexity. Version 2.0 marks a significant milestone in my development journey, introducing **External File Handling** and advanced **Validation Logic**. 

This project isn't just about code; it’s about the lessons learned while transitioning from basic syntax to functional programming.

## Key Improvements in v2.0
- **Database Integration:** The script now cross-references user input against `weak_password.txt` and `strong_password.txt`.
- **Requirement Tracking:** Dynamically identifies missing security components (Uppercase, Numbers, etc.).
- **Weighted Scoring:** Implements a 0–100 scoring system based on character diversity.

## Problems I Faced (Debugging Log)
To be a professional, you have to be truthful. Version 2.0 required fixing several "no-excuse" errors that initially broke the system:

1. **Treating Variables as Functions**
   - **The Error:** Writing `symbols()` instead of `symbols`.
   - **The Lesson:** You cannot "call" a string or a boolean. I learned to distinguish between an object and a function to resolve `TypeError: 'str' object is not callable`.

2. **File Reading Logic**
   - **The Error:** Writing `if password in "weak_password.txt"`. 
   - **The Lesson:** This only checked if the password was part of the *filename*. I learned to open the file, iterate through lines, and use `.strip()` to compare actual data.

3. **Open() Syntax Errors**
   - **The Error:** Missing commas in `open("filename" "r")`.
   - **The Lesson:** Python requires precise argument separation. I standardized my code to use `with open("file.txt", "r") as f:`.

4. **Logic & Variable Confusion**
   - **The Error:** Using `if len >= 8`.
   - **The Lesson:** `len` is a built-in function, not the result. I fixed this by using the variable `length` where the value was already stored.

## The v2.0 Logic Snippet
```python
# Cross-referencing external files
weak_list = []
with open("weak_password.txt", "r") as f:
    for line in f:
        weak_list.append(line.strip())

# Logic check for compromised passwords
if password in weak_list:
    print("Found In Weak Password Database")

# Categorization Logic
if length >= 8 and not missing:
    final_strength = "Very Strong Password"
elif length >= 6 and len(missing) <= 1:
    final_strength = "Strong Password"
else:
    final_strength = "Weak Password"