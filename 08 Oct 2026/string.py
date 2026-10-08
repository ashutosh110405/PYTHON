# use basic string operation using accepting string from user and print the length of string, reverse of string, upper case and lower case of string.
string = input("Enter a string: ") # accept string
print("Length of the string:", len(string))
print("Reverse of the string:", string[::-1])
print("Upper case of the string:", string.upper())
print("Lower case of the string:", string.lower())