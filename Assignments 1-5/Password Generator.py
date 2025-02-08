"""
We want to build a complex password generator based on multiple inputs
"""

import random
import string


# Function is gather password criteria 
def get_password_criteria():
    while True:
        try:
            length = int(input("Enter password length (minimum 8 characters)"))
            if length < 8:
                print("Password must be 8 characters long")
                continue
            break
        except ValueError:
            print("Please enter a valid number")


    include_uppercase = input("Include uppercase letters (y/n): ").strip().lower() == 'y'
    include_lowercase = input("Include lowercase letters (y/n): ").strip().lower() == 'y'
    include_numbers = input("Include numbers (y/n): ").strip().lower() == 'y'   
    include_specials = input("Include special characters (y/n): ").strip().lower() == 'y'
    
    if not (include_uppercase or include_lowercase or include_numbers or include_specials):
        print("You must select at least one character type")
        return get_password_criteria()
    return length, include_uppercase, include_lowercase, include_specials, include_numbers


#Function generate our password

def generate_password(length, uppercase, lowercase, specials, numbers):
    char_sets = ""
    guranteed_chars = []

    if uppercase:
        char_sets += string.ascii_uppercase
        guranteed_chars.append(random.choice(string.ascii_uppercase))
    if lowercase:
        char_sets += string.ascii_lowercase
        guranteed_chars.append(random.choice(string.ascii_lowercase))
    if numbers:
        char_sets += string.digits
        guranteed_chars.append(random.choice(string.digits))
    if specials:
        char_sets += string.punctuation
        guranteed_chars.append(random.choice(string.punctuation))

    remaining_length = length - len(guranteed_chars)
    password_chars = guranteed_chars + random.choices(char_sets, k=remaining_length)   
    random.shuffle(password_chars)

    return ''.join(password_chars)

#main function
def main():
    while True:
        length, uppercase, lowercase, numbers, specials = get_password_criteria()
        password = generate_password(length, uppercase, lowercase, numbers, specials)
        print(f"\nGenerated Password: {password}\n")

        retry = input("Generate another password y/n ").strip().lower
        if retry != 'y':
            print("goodbye")
            break

main()
        