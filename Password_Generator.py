# Import necessary modules
import string  # Provides a collection of string constants (letters, digits, punctuation)
import random  # Used for generating random values


# Function to generate a random password of a given length
def generate_password(length):
    # Check if the length is less than 8, and if so, print a warning and return None
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Define the set of characters allowed in the password (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the allowed set to form the password
    password = "".join(random.choice(characters) for i in range(length))

    # Return the generated password
    return password


# Function to get a valid password length from the user
def get_input():
    while True:
        try:
            # Prompt user for the password length and attempt to convert it to an integer
            length = int(input("Enter the desired password length: "))

            # If the length is less than 8, ask the user to try again
            if length < 8:
                print("Password length must be at least 8 characters. Try again.")
            else:
                return length  # Return the valid length
        except ValueError:
            # Handle case where input is not a valid integer
            print("Invalid input! Please enter an integer.")


# Main program starts here
password_length = get_input()  # Get the password length from the user
password = generate_password(password_length)  # Generate the password using the provided length

# If a valid password is returned, print it
if password:
    print(f"Generated password: {password}")
