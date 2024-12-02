import csv

def process_csv(file_path):
    result = {}
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Skip header if present
            if not header or len(header) < 2:
                raise ValueError("CSV file must have at least two columns.")

            values = []
            for row in reader:
                if len(row) < 2:
                    continue  # Skip rows with fewer than 2 columns
                try:
                    value = float(row[1])  # Convert second column to float
                    values.append(value)
                except ValueError:
                    continue  # Skip rows where the second column is not a number

            if not values:
                raise ValueError("No valid numerical data found in the second column.")

            average_value = sum(values) / len(values)
            result['average'] = average_value
    except FileNotFoundError:
        result['error'] = 'File not found.'
    except ValueError as ve:
        result['error'] = str(ve)
    except IOError:
        result['error'] = 'Error reading file.'
    except Exception as e:
        result['error'] = str(e)

    return result
