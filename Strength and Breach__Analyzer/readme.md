# Security and Breach Analyzer

### Project Overview
This tool is a specialized security utility designed to evaluate password strength. Unlike basic counters, this analyzer performs a deep scan of character composition and cross-references the input against a database of known leaked passwords. It is built on the philosophy that complexity without secrecy is a vulnerability.

---

### Core Technical Features
* **Complexity Scoring:** Analyzes passwords on a 100-point scale based on length and character diversity.
* **Requirement Tracking:** Identifies missing security elements (Uppercase, Numbers, Symbols).
* **Breach Verification:** Streams an external database to check if the password has been compromised.
* **Professional Reporting:** Generates a structured terminal output for immediate risk assessment.

---

### Development Stack & Logic
I utilized fundamental Python programming concepts to build this defensive tool:

* **input()**: Used to securely capture user data for analysis.
* **for Loops**: Iterates through every character in the password to analyze its composition.
* **if / elif / else Statements**: The "brain" of the project, used to calculate the score and determine the final security rank.
* **def (Functions)**: Used to create a modular check_breach function for cleaner, reusable code.
* **with open()**: Handles file I/O to read the common_password.txt database efficiently.
* **return Logic**: Implements "Early Return" to stop the search the moment a match is found, saving processing time.
* **Boolean Logic**: Tracks security flags like has_symbol and has_upper to manage state.

---

### The Build Process
1. **Requirement Gathering**: Defined the criteria for a "Strong" password (8+ characters, mixed casing, symbols).
2. **Logic Implementation**: Wrote the loop-based scanner to check for character types.
3. **Database Integration**: Built the breach checker to read from an external list of leaked credentials.
4. **Refactoring**: Optimized the code to remove unnecessary else statements and fix naming conflicts between variables and file lines.

---

### How to Run
1. Download the script and common_password.txt.
2. Place both files in the same folder.
3. Run the command: `python security_analyzer.py`.
4. Enter any password to receive a full security report.