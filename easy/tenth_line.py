# Read from the file file.txt and output the tenth line to stdout.
#!/bin/bash

solution = """
if [ -f file.txt ]; then
    if [ $(wc -l < file.txt) -ge 10 ]; then
        head -n 10 file.txt | tail -n 1
    fi
fi
"""

# Runtime 33 ms / Memory 3.70 mb
