# Define the decorator to convert the result to uppercase
def to_uppercase(func):
    def wrapper():
        result = func()
        return result.upper()  # Convert the result to uppercase
    return wrapper

# Apply the decorator to a function that returns a string
@to_uppercase
def greet():
    return "Hello, welcome to Python decorators!"

# Call the decorated function and display the result
result = greet()
print(result)

