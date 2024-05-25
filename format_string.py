def format_string(string):
    """
    Formats a string by replacing uppercase letters with lowercase letters and spaces with underscores.

    Parameters:
        string (str): The input string to be formatted.

    Returns:
        str: The formatted string.
    """
    return "".join("_" if char == " " else char.lower() for char in string)


input_string = "Word Pattern"
formatted_string = format_string(input_string)
print(formatted_string)

# Runtime 35 ms / Memory 16.66 mb
