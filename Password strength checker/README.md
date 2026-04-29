# Password Checker CLI

A simple Python command-line tool to check the strength of passwords.  
This project is designed for learning Python, practicing cybersecurity concepts, and building CLI tools.

---

## Features

- Checks for the presence of:
  - Uppercase letters  
  - Lowercase letters  
  - Numbers  
  - Symbols (`!@#$%^&*`)  
- Detects missing character types for stronger passwords  
- Evaluates password strength as:
  - Weak  
  - Strong  
  - Very Strong  
- Optional: warns if a password is common (`123456`, `password`, `abc123`, `qwerty`)  
- Scores passwords based on character variety (0–4 scale)  

---

## How to Run

1. Make sure you have Python installed (version 3.8+ recommended).  
2. Open your terminal and navigate to the project folder.  
3. Run the script:

```bash
python password_checker.py