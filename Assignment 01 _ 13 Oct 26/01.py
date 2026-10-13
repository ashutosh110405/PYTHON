#Write a program to read a file and count how many vowels are present in its content.
with open("01.txt", "r") as file:
    content = file.read()
    vowels = "aeiouAEIOU"
    count = 0

    for char in content:
        if char in vowels:
            count += 1

print("Number of vowels in the file:", count)
