# Define the decorator to log the function name
def simple_logger(func):
    def wrapper():
        print(f"Executing function: {func.__name__}")  # Log the function name
        func()  # Execute the original function
    return wrapper

# Apply the decorator to a function that prints a greeting message
@simple_logger
def greet():
    print("Hello, welcome!")

# Call the decorated function and display the logs
greet()
