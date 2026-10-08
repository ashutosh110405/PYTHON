# create a list of no and string and accept the value from user, separate the list from the max number. display the names in a sorted order.(without using f placeholder)
numbers = []
strings = []

for i in range(int(input("Enter the number of elements you want to input: "))):

    value = input("Enter a number or string: ")
    if value.isdigit():
        numbers.append(int(value))
    else:
        strings.append(value)

max_number = max(numbers) if numbers else None
print("Maximum number:", max_number)

print("Names in sorted order:")
for s in sorted(strings):
    print(s)