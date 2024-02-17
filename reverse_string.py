"""
Write a Python function that takes a string as input and returns a new string where the characters are reversed.

Here are some hints to help you get started:

 You can use Python's slicing feature to reverse the string. The syntax for slicing is [start:stop:step], where start and stop are the indices of the substring you want to extract, and step is the amount by which the index increases.
 If you set step to -1, you can reverse the string. Just use an empty start and stop values to specify that you want the entire string.
 Define a function that takes a string as input
 Use slicing with a step of -1 to reverse the string
 Return the resulting value

"""
def reverse(string):
    words = string.split(" ")
    words = words[-1::-1]
    output = ' '.join(words)
    print(output)


string_1 = "Welcome to python programming"
reverse(string_1)