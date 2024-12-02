import time

# Define the decorator to measure the execution time
def simple_timer(func):
    def wrapper():
        start_time = time.time()  # Record the start time
        func()  # Execute the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
    return wrapper

# Apply the decorator to a function that performs a small delay
@simple_timer
def perform_task():
    print("Task is being performed...")
    time.sleep(2)  # Simulate a delay of 2 seconds

# Call the decorated function and display the execution time
perform_task()
