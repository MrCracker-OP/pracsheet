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
     "elapsed": 5820,
     "status": "ok",
     "timestamp": 1722608125960,
     "user": {
      "displayName": "Mangal Dandekar",
      "userId": "12136019235932552125"
     },
     "user_tz": -330
    },
    "id": "nWq-7cPBcWUU",
    "outputId": "d1c9354e-43db-45ab-c38b-b24bcee97356"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of units consumed: 54\n",
      "The total electricity bill for 54 units is: $27.00\n"
     ]
    }
   ],
   "source": [
    "def calculate_electricity_bill(units):\n",
    "    if units <= 100:\n",
    "        bill = units * 0.50\n",
    "    elif units <= 200:\n",
    "        bill = (100 * 0.50) + ((units - 100) * 0.75)\n",
    "    elif units <= 300:\n",
    "        bill = (100 * 0.50) + (100 * 0.75) + ((units - 200) * 1.20)\n",
    "    else:\n",
    "        bill = (100 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 300) * 1.50)\n",
    "    return bill\n",
    "\n",
    "# Ask user to input the number of units consumed\n",
    "units = int(input(\"Enter the number of units consumed: \"))\n",
    "\n",
    "# Calculate and print the total bill amount\n",
    "total_bill = calculate_electricity_bill(units)\n",
    "print(f\"The total electricity bill for {units} units is: ${total_bill:.2f}\")\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyNVnBMPKOhMfCOTNubwoI+/",
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
