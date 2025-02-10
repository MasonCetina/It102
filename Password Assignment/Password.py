"""
This is brute force script to compare sha 512 hashes to a wordlist
"""

from passlib.hash import sha512_crypt # library for hashes


#Define Files to utilize on brute force
SHADOW_FILE = r'/home/justincase/Desktop/It102/It102/Password Assignment/Password.txt'
PASSWORD_FILE = r'/home/justincase/Desktop/It102/It102/Password Assignment/Shadow.txt'


def guess_password(shadow_file, password_file):
    successful_attempts = []

    try:
        with open(shadow_file, 'r', encoding='utf-8') as sf, open(password_file, 'r', encoding='utf-8') as pf:
            shadows = sf.readlines()
            passwords = [pw.strip() for pw in pf.readlines()]


        for shadow in shadows:
            parts = shadow.split(":")
            if len(parts) < 2 or '!' in parts [1] or '*' in parts [1]:
                continue
            username, hash_password = parts[0], parts[1].strip()

            for password in passwords:
                try:
                    if sha512_crypt.verify(password, hash_password):
                        successful_attempts.append(username, password)
                        print(f'[+] cracked {username}: {password}')
                        break
                except ValueError:
                    continue

              
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return


    if successful_attempts:
        print("\n=== CRACKED PASSWORD ===")
        for username, password in successful_attempts:
            print(f'User: {username}, Password: {password}')
    else:
        print("\nNo passwords were found or cracked")

#run the function
guess_password(SHADOW_FILE, PASSWORD_FILE)

    
                