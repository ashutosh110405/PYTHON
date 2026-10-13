#Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.
with open("01.txt", "r") as file:
    lines = file.readlines()
    total_lines = len(lines)
    print("Total number of lines:", total_lines)
    if total_lines >= 4:
        print("2nd line:", lines[1])
        print("4th line:", lines[3])
    else:
        print("The file does not have enough lines.")