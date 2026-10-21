# 'w+' mode: Opens a file for both writing and reading.
# Overwrites the existing file if it exists, or creates a new file if it does not.

with open("demo.txt", "w+") as file:
    file.write("Hello from w+ mode!\n")
    file.seek(0)  # Move file pointer back to the beginning to read
    content = file.read()
    print("Content read after writing:")
    print(content)