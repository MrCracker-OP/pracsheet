# Define the decorator to count function calls
def count_calls(func):
    count_calls.counter = 0  # Initialize the counter

    def wrapper():
        count_calls.counter += 1  # Increment the counter each time the function is called
        print(f"Function '{func.__name__}' has been called {count_calls.counter} time(s)")
        func()  # Execute the original function
    return wrapper

# Apply the decorator to a function that prints a message
@count_calls
def display_message():
    print("This is a sample message.")

# Call the decorated function multiple times
display_message()
display_message()
display_message()
