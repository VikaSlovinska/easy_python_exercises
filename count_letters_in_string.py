"""
Can you write a Python program that counts the number of times a particular letter appears in a given string? Here are some hints:
- To count the number of times a specific character appears in a string, you can use the count() method.
- The count() method takes one argument, which is the character or substring you want to count.
- You can define a variable that contains the letter you want to count and pass it as an argument to the count() method.
- If you want your search to be case-insensitive (i.e. count both uppercase and lowercase instances of the given letter), use the lower() or upper() method to convert both the string and the search letter to either lowercase or uppercase before counting


Can you write a Python program that counts the number of vowels in a given string?
Here are some hints:
Vowels are commonly defined as the letters 'a', 'e', 'i', 'o', and 'u'. However, keep in mind that some languages have additional vowel sounds or different vowel characters.
To loop through a string, you can use a for loop.
To check if a character is a vowel, use an if statement to check if the character is one of the defined vowel characters.
Use a variable to keep track of the number of vowels you find during your loop. You can increment this variable each time you find a vowel
"""


def count_letter(string, letter):
    count = string.count(letter)
    return count


print(count_letter("Viktoriya is quality assurance analyst", "a"))


def count_vowels(string):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    for i in range(len(example)):
        if example[i] in vowels:
            count += 1
        return count
    print("Number of vowels in a given string is: ", count_vowels(example))




