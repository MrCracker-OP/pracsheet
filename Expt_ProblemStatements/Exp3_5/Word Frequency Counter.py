#Problem 5: Character Frequency Analysis 
# Write a Python program that takes a string as input and returns a dictionary with the frequency of each character in the string. 
# The program should be case-insensitive and should include only alphabetic characters in the frequency count.

import re
String = "Btech In Artificial Intelligence"
a=len(re.findall("e",String))
print(a)

 