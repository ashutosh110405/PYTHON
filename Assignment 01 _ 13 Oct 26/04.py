#Read a file, split its content into words, and store them in a list.
#Print the total number of words.
#Print all unique words.
with open("01.txt", "r") as file:
    content = file.read()
    words = content.split()
    total_words = len(words)
    unique_words = set(words)

print("Total number of words:", total_words)
print("Unique words:", unique_words)