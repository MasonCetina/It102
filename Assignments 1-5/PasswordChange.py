"""
This code is to be run to see ask users after they change their passwords to log it for timing and future knowledge
"""
#imports for the date when logging
import hashlib
import datetime

# defining the scripts for when it is used to ask for the changes and then how to log it amd encrypting it
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def log_password_change(username, new_password):
    hashed_password = hash_password(new_password)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {username} - {hashed_password}\n"
    
    with open("password_change_log.txt", "a") as log_file:
        log_file.write(log_entry)

#using the script
def main():
    username = input("Please enter your username: ")
    new_password = input("Please enter your new password: ")
    log_password_change(username, new_password)
    print("Thanks for logging your password change!")

if __name__ == "__main__":
    main()