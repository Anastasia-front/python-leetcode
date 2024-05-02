# Read from the file file.txt and output all valid phone numbers to stdout.
solution = "grep -P '^(\(\d{3}\) |\d{3}-)\d{3}-\d{4}$' file.txt"

# Runtime 67 ms / Memory 3.36 mb
