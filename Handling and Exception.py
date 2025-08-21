def modify_content(content):
    return content.upper()

def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            original_content = infile.read()
            print("File read successfully.")

        modified_content = modify_content(original_content)

        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You don’t have access to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()