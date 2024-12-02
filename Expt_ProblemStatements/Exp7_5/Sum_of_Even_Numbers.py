from functools import reduce

# Input list of integers
numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]

# Filter even numbers using filter() and lambda
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Calculate the sum of even numbers using reduce() and lambda
sum_even_numbers = reduce(lambda acc, x: acc + x, even_numbers, 0)

# Display the resulting sum
print("Sum of all even numbers:", sum_even_numbers)
