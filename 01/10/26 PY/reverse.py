#reverse the string
def reverse_string(string):
    return string[::-1]

original_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(original_string)
print("Reversed string:", reversed_string)