import shutil
import os

def backup_file(source_file, backup_file):
    try:
        # Check if source file exists
        if not os.path.isfile(source_file):
            return "Error: Source file not found."

        # Attempt to copy the file
        shutil.copy2(source_file, backup_file)
        return "Backup created successfully."

    except PermissionError:
        return "Error: Permission denied."

    except IOError as e:
        return f"Error: I/O error occurred - {str(e)}"

    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
source = '/content/Data_source.csv'
backup = '/content/Data_backup.csv'
print(backup_file(source, backup))
