import os
#Make an Failure dictionary to store in failed attempts
failure = {}
Blacklistfile = "blacklist.txt"

#Read Text-File Line By Line
blaclisted_ip = set()
if os.path.exists("Blacklistfile"):
    with open("blacklist.txt", "r") as f:
        blaclisted_ip = set(line.strip() for line in f)


with open("server_log_attempts.txt", "r") as file:
    #Loop Through For Failed Atttempts
    for line in file:
        line = line.strip()
        if not line: continue

        part = line.split()

        ip = part[0]
        status = part[1]

        #Loop Through Failuures
        if status == "FAILED":
            #cOUNTING OCURRENCES IN DICTIONARY
            failure[ip] = failure.get(ip, 0)+1

            #Count For Failed Attemts And Lock Account
            if failure[ip] >= 3 and ip not in blaclisted_ip:
                #add faled login to blacklisted file
                with open("blacklist.txt", "a") as f:
                    f.write(f"{ip}\n")
                    blaclisted_ip.add(ip)

                #Print results 
                print(f"\n SECURITY DETECTED")
                print(f"ADDRESS: {ip}")
                print(f"FAILED COUNT: {failure[ip]}")
                print(f"STATUS : PERMANENTLY BLACKLISTED")
                print(f"RECORD ADDED TO {Blacklistfile}")
                print("-"*30)

