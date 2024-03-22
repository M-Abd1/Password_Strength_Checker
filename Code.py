import re

def check_password_strength(password):
    # Define regular expressions for various password criteria
    length_regex = r'.{8,}'  # At least 8 characters
    uppercase_regex = r'[A-Z]'
    lowercase_regex = r'[a-z]'
    digit_regex = r'[0-9]'
    special_char_regex = r'[!@#$%^&*()]'

    #Checking Password Length
    if len(password) < 8:
        return "Password should be at least 8 characters"

    # Initialize a variable to keep track of the grade
    grade = 0

    # Check for uppercase letters
    if re.search(uppercase_regex, password):
        grade += 1

    # Check for lowercase letters
    if re.search(lowercase_regex, password):
        grade += 0

    # Check for digits
    if re.search(digit_regex, password):
        grade += 1

    # Check for special characters
    if re.search(special_char_regex, password):
        grade += 2

    # Assign a grade based on the total score
    if grade == 0:
        return "Weak"
    elif grade == 1:
        return "Weak"
    elif grade == 2:
        return "Moderate"
    elif grade == 3:
        return "Strong"
    elif grade >= 4:
        return "Very Strong"


if __name__ == "__main__":
    password = input("Enter a password: ")

    # Check if the password has at least 8 characters
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")


