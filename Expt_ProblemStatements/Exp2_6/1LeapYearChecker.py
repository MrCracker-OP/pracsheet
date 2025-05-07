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
     "elapsed": 4852,
     "status": "ok",
     "timestamp": 1722606799263,
     "user": {
      "displayName": "Mangal Dandekar",
      "userId": "12136019235932552125"
     },
     "user_tz": -330
    },
    "id": "qK_WjUWRXYKG",
    "outputId": "d0309bd4-6f6e-449c-8783-0b3af9fec490"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a year: 2022\n",
      "2022 is not a leap year.\n"
     ]
    }
   ],
   "source": [
    "def is_leap_year(year):\n",
    "    if (year % 4 == 0):\n",
    "        if (year % 100 != 0) or (year % 400 == 0):\n",
    "            return True\n",
    "    return False\n",
    "\n",
    "# Ask user to input the year\n",
    "year = int(input(\"Enter a year: \"))\n",
    "\n",
    "# Check if the year is a leap year and print the result\n",
    "if is_leap_year(year):\n",
    "    print(f\"{year} is a leap year.\")\n",
    "else:\n",
    "    print(f\"{year} is not a leap year.\")\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "authorship_tag": "ABX9TyPg/fQFcWeLEBOWTWaK4cpC",
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
