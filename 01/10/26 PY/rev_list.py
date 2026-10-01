#reverse the list 
def reverse_list(input_list):
    return input_list[::-1]

user_list = input("Enter a list of elements separated by spaces: ").split()
reversed_list = reverse_list(user_list)
print("Reversed list:", reversed_list)