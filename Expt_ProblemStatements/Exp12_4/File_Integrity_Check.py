def check_file_integrity(file_path):
    try:
        # Attempt to open and read the file
        with open(file_path, 'r') as file:
            content = file.read()

            # Check if the file is empty
            if not content:
                return "Error: File is empty."

            # If the file has content, return success message
            return "File contains valid content."

    except FileNotFoundError:
        return "Error: File not found."

    except IOError as e:
        return f"Error: I/O error occurred - {str(e)}"

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
file_path = '/content/Data.csv'
print(check_file_integrity(file_path))
