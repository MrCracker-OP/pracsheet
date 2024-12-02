# Define the decorator to add a greeting message
def add_greeting(func):
    def wrapper(name):
        print("Hello!")  # Print greeting before executing the function
        func(name)  # Execute the original function
    return wrapper

# Apply the decorator to a function that prints the user's name
@add_greeting
def print_name(name):
    print(f"My name is {name}")

# Call the decorated function with a sample name
print_name("Alice")
