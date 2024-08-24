# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.



def user_input_dict():
    my_dict = {}
    
    print("Enter key-value pairs of your personal detail like name, age, and favourite color (type 'q' to quit):")
    
    while True:
        key = input("Enter key (or 'q' to quit): ")
        if key.lower() == 'q':
            break
        value = input(f"Enter value for key '{key}': ")
        my_dict[key] = value
    
    return my_dict

# Get user input for the dictionary
my_dict = user_input_dict()

# Print the resulting dictionary
print("Your personal detail is:", my_dict)
