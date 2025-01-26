"""
This script will ask user for name, favorite color, pets name,
mothers maiden name, and elementry school
"""



# function to collect user information
def collect_user_data():
    print('Please answer the following questions')
    name = input('what is your name?: ')
    favorite_color = input('what is your favorite color?: ')
    pet = input('what is your pets name?: ')
    mother = input('what is your mothers maidens name?: ')
    school = input('what was your elementry school you attended?: ')

    # Return collected info as dictionary
    return {
        "Name":name,
        "color":favorite_color,
        "pet":pet,
        "mother":mother,
        "school":school

    }


# Function to save information in a file
def save_to_file(data, filename='hackme.txt'):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
    print(f"information has been saved to {filename}. ")
   


# Collect and save user information 
save_to_file(collect_user_data())

