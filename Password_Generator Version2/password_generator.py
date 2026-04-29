import re
import secrets
import string

def password_engineer_v2():
    print("--- Pro Password Generator V2 (Cyber-Ready) ---")
    desc = input("Describe your password: ").lower()

    # 1. Parsing Logic (The "One")
    length_match = re.search(r'\d+', desc)
    length = int(length_match.group()) if length_match else 12

    # Map keywords to character sets
    mapping = {
        "lower": string.ascii_lowercase,
        "upper": string.ascii_uppercase,
        "symbol": string.punctuation,
        "special": string.punctuation,
        "number": string.digits,
        "digit": string.digits
    }

    active_pools = [pool for key, pool in mapping.items() if key in desc]

    # Default if user is too vague
    if not active_pools:
        print("!! No specific requirements found. Using default secure set.")
        active_pools = [string.ascii_letters, string.digits, string.punctuation]

    # 2. Generation Logic (The "Two")
    # Guarantee at least one from every requested category
    password_list = [secrets.choice(p) for p in active_pools]

    # Fill the rest with a combined pool
    full_pool = "".join(active_pools)
    while len(password_list) < length:
        password_list.append(secrets.choice(full_pool))

    # Secure Shuffle
    secrets.SystemRandom().shuffle(password_list)
    final_password = "".join(password_list)

    # 3. The Self-Audit
    strength = "Strong" if len(final_password) >= 12 and len(active_pools) >= 3 else "Weak"
    
    print("-" * 30)
    print(f"Generated: {final_password}")
    print(f"Security Level: {strength}")
    print("-" * 30)

password_engineer_v2()
