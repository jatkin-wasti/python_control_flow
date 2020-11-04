# This lesson will cover control flow
## If statements, Elif, and Else statements
### If
- Syntax is
```
if condition:
    do_this
```
- Used to run code in certain situations i.e. when a condition is met
### Elif
- Syntax is 
```
elif condition:
    do_this
```
- Used to run code if the first if condition has not been met
### Else
- Syntax is
```
else:
    do_this
```
## For loops and While loops
- ```break``` will stop the loop
- ```continue``` will immediately start the next iteration of the loop
### For loops
- Will loop through data for a set range
- The maximum number of loops is defined before it is run
- Syntax is for variable_name in data_collection:
```
for items in shopping_list:  # loops through the shopping list
    print(items)  # prints the found item
    if items == "milk":  # checks if the item found is milk
        break  # if so it breaks out of the loop
```
- This next example is looping through keys and values in a dictionary
```
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
```
### While loops
- Will continue looping through data until a certain condition is met
- Useful for continuously prompting a user
- Can be problematic if 
- ```break``` and ```continue``` can be used to control the flow of the loop
- Not regularly used however it can be useful for monitoring
- Syntax for a while loop is while condition:   e.g. while number < 10:
- Task: Take user input with while loop
- isdigit() checks if the input is all digits
```
user_prompt = True
while user_prompt:  # Continues to loop until user_prompt is set to False
    age = input("Please enter your age:  ")  # Receives user's age
    if age.isdigit() and int(age) < 117:  # Checks if the user's age is a number or a reasonable value
        user_prompt = False  # If they have input a satisfactory age we can end the loop
    else:  # Otherwise we should continue looping
        print("Please provide age in digits")  # Prompt the user to input a more satisfactory value
print(f"Your age is {age}")  # Outputs their age 
```
- Task: Create a while loop
```
number = 0  # Defining the number variable
while number < 10:  # Checking a condition and running until the number is 10 or above
    print(f"It's working --> {number}")  # Prints out a string containing the current value of number
    if number == 4:  # Checks if the number is currently 4
        break  # If so it breaks out of the loop
    number += 1  # Iterate the number variable
```