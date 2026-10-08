#create a list of 10 elements (string), print the sum of last 4 elemets of the list. find the difference between max and min elements of the list. 
#inser a number at 6th position of the list. this number must be 1/3 of number stored at 4th position of the list. print the updated list.
#different functions on the list - length, sum, sorted, reverse. without using f placeholder, print the length, sum, sorted and reverse of the list.

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


#sum of last 4 ele
sum_last_4 = sum(list1[-4:])
print("Sum of last 4 elements:", sum_last_4)

# diff between max and min elements
diff = max(list1) - min(list1)
print("Difference between max and min elements:", diff)

#insert a number at 6th position
#this number must be 1/3 of the number stored at 4th position
list1.insert(5, list1[3] / 3)
print("Updated list:", list1)

#different functions on the list
print("Length of the list:", len(list1))
print("Sum of the list:", sum(list1))
print("Sorted list:", sorted(list1))
print("Reversed list:", list1[::-1])