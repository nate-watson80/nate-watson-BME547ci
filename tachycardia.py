# tachycardia.py
# Written by: Nate Watson
# 2.1.19
# Test if the word "tachycardic" is in user input


def is_tachycardia(string_input):
    compare = "tachycardic"  # Word to compare strings

    string_input = str(string_input)  # Ensure input is a valid string
    updated_input = string_input.casefold()  # Convert to lowercase
    updated_input = updated_input.strip()  # Remove trailing/leading spaces
    updated_input = updated_input.replace("1", "i")

    counter = 0  # Initialize counter variable
    # Find characters in common in both strings
    for i, c in enumerate(updated_input):
        if (c == compare[i]):
            counter = counter + 1

    if (counter >= 9):
        return True
    else:
        return False
