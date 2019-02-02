# tachycardia.py
# Written by: Nate Watson
# 2.1.19
# Test if the word "tachycardic" is in user input


def is_tachycardia(string_input):
    compare = "tachycardic"  # Word to compare strings

    string_input = str(string_input)  # Ensure input is a valid string
    updated_input = string_input.casefold()  # Convert to lowercase
    updated_input = updated_input.strip()  # Remove trailing/leading spaces

    if (updated_input == compare):  # Determine if input matches
        return True
    else:
        return False
