# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words =  ["apple", "banana", "cherry", "fig", "grape"]

fruits = [word for word in words]
if (len(fruits) % 2 != 0):
        print(f"Words with an odd number of characters are:{fruits}")
    