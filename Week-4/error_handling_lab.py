filename = input("Enter the name of the file to read: ")

try: 
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print("Error: FileNotFound.")
except PermissionError:
    print("Error: You don't have permission to read this file")
except Exception as e:
    print(f"Unexpected error: {e}")
