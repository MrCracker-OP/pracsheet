# Input strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Sort the characters in each string
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)

# Compare the sorted strings
if sorted_string1 == sorted_string2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
