
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.


user_input = input("Enter a list of integers separated by spaces: ") # Get user input for list of integers

int_list = [int(x) for x in user_input.split()] # Convert the input string into a list of integers

total_sum = sum(int_list) # Calculate the sum of all integers in the list

print("The sum of the integers is:", total_sum) # Output the result


#OR

def addList(int_num):
    total_sum = 0
    for num in int_num:
        total_sum += num
    return total_sum

def user_input():
    int_num = []
    while True:
        num = input("Enter an integer (or 'q' to quit): ")
        if num.lower() == 'q':  # Check for 'q' to quit
            break
        try:
            int_num.append(int(num))  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return int_num

# Get stored user input
int_num = user_input()

# Calculate and print the sum
total_sum = addList(int_num)
print("The sum of the integers is:", total_sum)

