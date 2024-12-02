def filter_odd_numbers(numbers):
    # Use filter() with lambda to keep only odd numbers
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    # Convert the filter object to a list
    return list(odd_numbers)

# Main function to execute the program
def main():
    # Take a list of integers as input from the user
    input_list = input("Enter a list of integers separated by spaces: ")
    # Convert the input string to a list of integers
    numbers = list(map(int, input_list.split()))

    # Get the filtered list of odd numbers
    result = filter_odd_numbers(numbers)

    # Display the resulting list of odd numbers
    print("List of odd numbers:", result)

# Run the main function
if __name__ == "__main__":
    main()
