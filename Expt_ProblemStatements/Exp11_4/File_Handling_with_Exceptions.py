def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: The file does not exist."
    except Exception as e:
        return f"Error: An unexpected error occurred. {str(e)}"

read_file('/content/timeseries.csv')