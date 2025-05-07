{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 16199,
     "status": "ok",
     "timestamp": 1722608490336,
     "user": {
      "displayName": "Mangal Dandekar",
      "userId": "12136019235932552125"
     },
     "user_tz": -330
    },
    "id": "umJFUAUxdGkW",
    "outputId": "fef135a4-dbd4-44cb-91e9-4d9817ca069a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your weight in kg: 80\n",
      "Enter your height in meters: 1.6764\n",
      "Your BMI is: 28.47\n",
      "Your BMI category is: Overweight\n"
     ]
    }
   ],
   "source": [
    "def calculate_bmi(weight, height):\n",
    "    bmi = weight / (height ** 2)\n",
    "    return bmi\n",
    "\n",
    "def categorize_bmi(bmi):\n",
    "    if bmi < 18.5:\n",
    "        return \"Underweight\"\n",
    "    elif 18.5 <= bmi < 24.9:\n",
    "        return \"Normal weight\"\n",
    "    elif 25 <= bmi < 29.9:\n",
    "        return \"Overweight\"\n",
    "    else:\n",
    "        return \"Obesity\"\n",
    "\n",
    "# Ask user to input weight and height\n",
    "weight = float(input(\"Enter your weight in kg: \"))\n",
    "height = float(input(\"Enter your height in meters: \"))\n",
    "\n",
    "# Calculate BMI\n",
    "bmi = calculate_bmi(weight, height)\n",
    "\n",
    "# Categorize BMI\n",
    "category = categorize_bmi(bmi)\n",
    "\n",
    "# Print the results\n",
    "print(f\"Your BMI is: {bmi:.2f}\")\n",
    "print(f\"Your BMI category is: {category}\")\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyM8jZydVeDOcnKfQ7kmk4rJ",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
