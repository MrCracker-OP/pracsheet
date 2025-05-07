{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "UFk-ExmybNEw",
    "outputId": "d37d9196-f8e5-4ade-dc71-e87fd9c6fe67"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a single alphabetic character: U\n",
      "The character 'U' is a vowel.\n"
     ]
    }
   ],
   "source": [
    "def check_vowel_or_consonant(char):\n",
    "    vowels = 'aeiouAEIOU'\n",
    "    if char in vowels:\n",
    "        return \"vowel\"\n",
    "    else:\n",
    "        return \"consonant\"\n",
    "\n",
    "# Ask user to input a single character\n",
    "char = input(\"Enter a single alphabetic character: \")\n",
    "\n",
    "# Check if the input is valid\n",
    "if len(char) == 1 and char.isalpha():\n",
    "    result = check_vowel_or_consonant(char)\n",
    "    print(f\"The character '{char}' is a {result}.\")\n",
    "else:\n",
    "    print(\"Please enter a single alphabetic character.\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "auyMQcUigC5m"
   },
   "source": [
    "Vowel or Consonant ( without using a function )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "AcvDQHWjgCd6",
    "outputId": "9cd2cae6-1d02-4e84-b93c-4249ee62735d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a single alphabetic character: u\n",
      "u is a vowel.\n"
     ]
    }
   ],
   "source": [
    "# Take a single character as input\n",
    "char = input(\"Enter a single alphabetic character: \")\n",
    "\n",
    "# Convert the character to lower case for comparison\n",
    "char_lower = char.lower()\n",
    "\n",
    "# Check if the character is a vowel or a consonant\n",
    "if char_lower in ['a', 'e', 'i', 'o', 'u']:\n",
    "    print(f\"{char} is a vowel.\")\n",
    "else:\n",
    "    print(f\"{char} is a consonant.\")\n"
   ]
  }
 ],
 "metadata": {
  "colab": {
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
