# Input list of integers
input_list = [10, 20, 20, 30, 40, 10, 50]

if input_list:
    # Find the largest and smallest numbers in the list
    largest = max(input_list)
    smallest = min(input_list)

    # Calculate the sum and average of the numbers in the list
    total_sum = sum(input_list)
    average = total_sum / len(input_list)

    # Remove duplicates from the list
    unique_list = list(set(input_list))

    # Display the results
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Sum of the numbers: {total_sum}")
    print(f"Average of the numbers: {average:.2f}")
    print(f"List without duplicates: {unique_list}")
else:
    print("The list is empty.")
