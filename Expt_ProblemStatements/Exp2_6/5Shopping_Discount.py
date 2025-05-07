{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "executionInfo": {
     "elapsed": 9691,
     "status": "ok",
     "timestamp": 1722608674977,
     "user": {
      "displayName": "Mangal Dandekar",
      "userId": "12136019235932552125"
     },
     "user_tz": -330
    },
    "id": "UZp0izGPeeRr",
    "outputId": "88d4e519-0280-40aa-eb2e-5f9101e255bd"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the purchase amount: $600\n",
      "The final price after applying the discount is: $570.00\n"
     ]
    }
   ],
   "source": [
    "def calculate_discounted_price(purchase_amount):\n",
    "    if purchase_amount > 1000:\n",
    "        discount = 0.10\n",
    "    elif 500 <= purchase_amount <= 1000:\n",
    "        discount = 0.05\n",
    "    else:\n",
    "        discount = 0.0\n",
    "    final_price = purchase_amount * (1 - discount)\n",
    "    return final_price\n",
    "\n",
    "# Ask user to input the purchase amount\n",
    "purchase_amount = float(input(\"Enter the purchase amount: $\"))\n",
    "\n",
    "# Calculate the final price after applying the discount\n",
    "final_price = calculate_discounted_price(purchase_amount)\n",
    "\n",
    "# Print the final price\n",
    "print(f\"The final price after applying the discount is: ${final_price:.2f}\")\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyOhyP8nFJMRZ9z9DOAn1PzE",
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
