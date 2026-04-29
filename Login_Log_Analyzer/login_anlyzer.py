attempts = {}
failures = {}

# 1. Open log file
with open("login_log_analyzer.txt", "r") as f:
    for line in f:
        line = line.strip()        # FIXED: Use '=' to save the stripped string
        parts = line.split()       # FIXED: Use '.split()' to create a list of words
        
        # Safety check: skip lines that don't have enough data
        if len(parts) < 3:
            continue

        status = parts[1]          # FIXED: Use '=' for assignment
        username = parts[2]        # FIXED: Use '=' for assignment

        # 2. Update attempts dictionary
        if username not in attempts:
            attempts[username] = 1
        else:
            attempts[username] += 1 
        # 3. Update failures dictionary
        if status == "FAILED":
            if username not in failures:
                failures[username] = 1
            else:
                failures[username] += 1 

# --- OUTPUT SECTION ---

# Print login attempts
print("--- LOGIN ATTEMPTS ---")
for user, count in attempts.items():
    print(f"{user} : {count}")
    
# Print Failed login
print("\n--- FAILED ATTEMPTS ---")
for user, count in failures.items():
    print(f"{user} : {count}")

# Print brute force alert
print("\n--- BRUTE FORCE ALERTS ---")
for user, count in failures.items():
    if count >= 3: # FIXED: Added the logic to actually filter for 3+ failures
        print(f"ALERT: Possible brute force attack on {user} ({count} failures)")