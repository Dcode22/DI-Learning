def reverse32(input):
    if not isinstance (input, int):
        raise TypeError("Invalid input. Integer required.")
    binary = "{:032b}".format(input)
    binary = binary[::-1]
    output = int(binary, 2)
    return output