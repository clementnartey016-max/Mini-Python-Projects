# Username List
username = ["Adam","Eve","Emmanuel","Clement","David","Sulley","Micheal","Microsoft","mary","clement","eve","david","microsoft"]

# Duplicates, Seen_Users and count
seen = set()
duplicate = set()
# We make this lowercase so it matches our "wierd" variable perfectly
suspicious_list = ["eve", "clement", "microsoft", "emmanuel"]
counts = {}

# Looping through usernames
for names in username:
    # Normalize Usernames
    wierd = names.lower()

    # Count duplicates - (This must be indented to count EVERY name)
    counts[wierd] = counts.get(wierd, 0) + 1

    # check suspicious user_names - (Indented to check EVERY name)
    if wierd in suspicious_list:
        print(f"WARNING USERNAME IS SUSPICIOUS: {wierd}")

    # Check for duplicate usernames - (Indented to process EVERY name)
    # Logic: If we have seen it before, it's a duplicate. If not, add to seen.
    if wierd in seen:
        duplicate.add(wierd)
    else:
        seen.add(wierd)

# Print Results
print("\n Name Analysis: ")
print(f"Unique Username: {seen}")
print(f"Duplicate Names Found: {duplicate}")
print(f"Full Count: {counts}")