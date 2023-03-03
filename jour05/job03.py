def take_input():
    return input("Enter a character string: ")


def length_string(char):
    if char == "":
        return 0
    else:
        return 1 + length_string(char[1:])


print("Character string length:", length_string(take_input()))
