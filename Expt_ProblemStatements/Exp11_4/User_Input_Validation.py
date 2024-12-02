def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Define the prompt you want to use
prompt = "Enter an integer: "

# Now call the function with the defined prompt
get_integer_input(prompt)