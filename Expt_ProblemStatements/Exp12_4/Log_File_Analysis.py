def analyze_log_file(file_path):
    result = {}
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)
            error_count = sum(line.count("ERROR") for line in lines)

            result['total_lines'] = total_lines
            result['error_count'] = error_count
    except FileNotFoundError:
        result['error'] = 'File not found.'
    except IOError:
        result['error'] = 'Error reading file.'
    except Exception as e:
        result['error'] = str(e)

    return result
