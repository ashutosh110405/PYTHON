#Take a sentence from the user, split it into words, and store them in a list. Print the longest word.
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)