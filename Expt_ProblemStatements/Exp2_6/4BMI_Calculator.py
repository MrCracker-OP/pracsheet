def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Ask user to input weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight, height)

# Categorize BMI
category = categorize_bmi(bmi)

# Print the results
print(f"Your BMI is: {bmi:.2f}")
print(f"Your BMI category is: {category}")
