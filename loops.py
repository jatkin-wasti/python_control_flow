# Loops: For and While
# For loops are used to iterate through data for a set number of iterations
# Syntax is for variable_name in data_collection:

shopping_list = ["eggs", "milk", "supermalt"]
print(shopping_list)

for items in shopping_list:  # loops through the shopping list
    if items == "milk":  # looks for milk in the shopping list
        print(items)  # prints the found item

for items in shopping_list:  # loops through the shopping list
    print(items)  # prints the found item
    if items == "milk":  # checks if the item found is milk
        break  # if so it breaks out of the loop

# We use this dictionary to test looping through its keys and values
trainee_dictionary = {
    "name": "Dave Smith",
    "date_of_birth": "14/03/19994",
    "address": "78b Hilltop Street XL7 G8Y",
    "course": "DevOps",
    "grades": [80, 68]
}
# We are looping through the dictionary's keys and printing them out
for keys in trainee_dictionary.keys():
    print(keys)
# We are looping through the dictionary's values and printing them out
for values in trainee_dictionary.values():
    print(values)

# While loops are used to iterate through data infinitely until a condition is met
