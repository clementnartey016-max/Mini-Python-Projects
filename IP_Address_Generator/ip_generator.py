import random

def generate_ip(amount):
    print(f"---Generating {amount} Random Attackers IPs---")

    for i in range(amount):
        octet1 = random.randint(0, 255)
        octet2 = random.randint(0, 255)
        octet3 = random.randint(0, 255)
        octet4 = random.randint(0, 255)

        #dot added to strings between numbers
        ip_address = f"{octet1}.{octet2}.{octet3}.{octet4}"

        print(f"Attacker{i+1}: {ip_address}")
generate_ip(5)