# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

def set_input(set_name):
    # Get user input and convert it to a set of integers
    user_input = input(f"Enter the elements of set {set_name} separated by spaces: ")
    int_set = set(map(int, user_input.split()))
    return int_set

# store input for sets A and B
A = set_input("A")
B = set_input("B")

# Find the intersection of both sets
common_elements = A.intersection(B)

# Print the result
print(f"The common elements between set A and set B are:{common_elements}")
