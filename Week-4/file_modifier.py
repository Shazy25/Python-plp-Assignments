def modify_content(content):
    # Modify the content (e.g., convert to uppercase)
        return content.upper()

try:    
    with open('input.txt', 'r') as infile:
        content = infile.read()
        modified = modify_content(content)
      
        with open('output.txt','w') as outfile:
            outfile.write(modified)

            print("File modified and saved to output.txt")

except FileNotFoundError:
    print("Error: input.txt not found.")
except Exception as e:
    print(f"Unexpected error: {e}")

