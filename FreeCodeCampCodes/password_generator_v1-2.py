import re
import secrets
import string

length = 0
nums = 0
special_chars = 0
uppercase = 0
lowercase = 0

def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Defining the function arguments by the user:
    length = int(input('Enter the desired length of the password:\n'))
    nums = int(input('What is the desired amount of numbers in it?\n'))
    special_chars = int(input('What is the desired amount of symbols in it?\n'))
    uppercase = int(input('What is the desired amount of uppercase letters that you want in it?\n'))
    lowercase = int(input('What is the desired amount of lowercase letters that you want in it?\n'))

    # Combine all characters
    all_characters = letters + digits + symbols

    if length >= (nums + special_chars + uppercase + lowercase):
        while True:
            password = ''
            # Generate password
            for _ in range(length):
                password += secrets.choice(all_characters)

            constraints = [
                (nums, r'\d'),
                (special_chars, fr'[{symbols}]'),
                (uppercase, r'[A-Z]'),
                (lowercase, r'[a-z]')
            ]

            # Check constraints
            if all(
                    constraint <= len(re.findall(pattern, password))
                    for constraint, pattern in constraints
            ):
                break

        return password
    else:
        print('The sum of desired components of the password are greater than the desired length of it.')


if __name__ == '__main__':
    new_password = generate_password(length, nums, special_chars, uppercase, lowercase)
    print('Generated password:', new_password)
