def format_string(string):
    """
    Formats a string by replacing uppercase letters with lowercase letters,
    spaces with underscores, and removing dots.

    Parameters:
        string (str): The input string to be formatted.

    Returns:
        str: The formatted string.
    """
    return "".join("_" if char == " " else char.lower() if char != "." else "" for char in string)

input_string = "398. Random Pick Index"
formatted_string = format_string(input_string)
print(formatted_string)

# TASK 367
# Runtime 35 ms / Memory 16.66 mb
