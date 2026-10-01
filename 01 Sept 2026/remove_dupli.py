#remove the duplicate numbers from a list input from user
def remove_duplicates(input_list):
    return list(set(input_list))

user_list = input("Enter a list of numbers separated by spaces: ").split()
user_list = [int(x) for x in user_list]
unique_list = remove_duplicates(user_list)
print("List with duplicates removed:", unique_list)