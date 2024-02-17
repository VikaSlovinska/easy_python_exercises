"""

Can you write a Python program to loop through a list of numbers and only print out the even numbers?
Here are some hints:
To loop through a list of numbers, you can use a for loop.
The modulo operator (%) can be used to determine if a number is even. If a number is divided by 2 and there is no remainder, then it is even.
To check if a number is even in your loop, use an if statement to check if the number is divisible by 2. If it is, then print the number.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,876,989,990]


"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 876, 989, 990]


def even(numbers):
    even_number = []
    for i in numbers:
        if i % 2 == 0:
            even_number.append(i)
    print(f"Even number are : {even_number}")


even(numbers)

