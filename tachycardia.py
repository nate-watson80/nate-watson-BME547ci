# tachycardia.py
# Written by: Nate Watson
# 2.1.19
# Test if the word "tachycardic" is in user input


def is_tachycardia(string_input):
    compare = "tachycardic"  # Word to compare strings
    output = False

    string_input = str(string_input)  # Ensure input is a valid string
    updated_input = string_input.casefold()  # Convert to lowercase
    updated_input = updated_input.strip()  # Remove trailing/leading spaces
    updated_input = updated_input.replace("1", "i")

    # Find characters in common in both strings:
    counter = 0
    for i, c in enumerate(updated_input):
        if (c == compare[i]):
            counter = counter + 1

    # Identify if 1 or 2 characters are missing:
    storage_str = ""
    for i in updated_input:
        if (compare.find(i) != -1):
            storage_str = storage_str + i

    # Logic to determine if word is close enough
    if (len(storage_str)>= (len(compare)-2) or counter >= (len(compare)-2)):
        return True
    else:
        return False
