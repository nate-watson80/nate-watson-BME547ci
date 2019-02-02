
def main():
    string_input = input("Input test case: ")
    test = is_tachycardia(string_input)

    print(test)


def is_tachycardia(string_input):
    compare = "tachycardic"  # Word to compare strings
    string_input = string_input.casefold()  # Convert to lowercase


    return string_input


# Iterate main loop:
if (__name__ == "__main__"):
    main()
