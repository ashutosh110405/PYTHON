#take input from user and find out how much input is digits onlu count digit not char or any symbol
n = int(input("Enter a number: "))
num = sum(1 for i in str(n) if i.isdigit())
print(f"Number of digits in the input: {num}")