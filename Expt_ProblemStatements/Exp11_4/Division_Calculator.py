def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Invalid input type. Both inputs must be numbers."
